/**
 * laguna-search — a framework-free finding aid for transcribed genealogy plates.
 *
 *   import { mountSearch } from "./search.js";
 *   mountSearch(document.querySelector("#app"), { data });
 *
 * or, with no build step at all:
 *
 *   <laguna-search src="search-index.json"></laguna-search>
 *
 * `data` is the index emitted by build.py: { meta, people, identities,
 * relationships }. Nothing in this file knows about Parsons or Laguna — the
 * tables, clans, labels and link targets all come out of `meta` — so the same
 * widget can be pointed at another edition's index.
 *
 * ONE list, one set of state. The reference had two result lists with parallel
 * state that had already diverged; phase 1 reduced that to one class with two
 * instances, which still meant two copies of every filter and a search panel
 * that had to push its query into both. There is now a single list, and every
 * control — the name box, the table toggles, the number box, the column
 * filters, the sort — writes to the same `state` object and is readable back
 * out of the URL.
 *
 * Read-only by construction: nothing here writes, posts or mutates anything
 * but its own DOM and its own query string.
 *
 * Module-level code must stay free of `document`: build.py parses the FOLD map
 * out of this file and node imports it for the tests, so a top-level DOM
 * reference would break the build rather than the page.
 */

export const VERSION = "0.3.0";

const CHUNK = 60;            // rows rendered per pass
const DEBOUNCE_MS = 110;
const FUZZY_MIN_QUERY = 3;   // below this a typo tolerance matches everything

/* ------------------------------------------------------------------ text -- */

/**
 * The edition's own fold map, unioned across the four transcription modules.
 *
 * THIS IS THE ONLY COPY. build.py parses this literal to fold the record keys,
 * so the browser and the builder cannot drift apart.
 *
 * It is transcribed from `_FOLD` in the edition's `scripts/transcription*.py`,
 * merged across the four plates, and is not a reimplementation. NFKD looks
 * like the obvious way to do this and is wrong twice over: ʼ U+02BC is a
 * modifier LETTER, so it survives a `\p{L}` filter, and ᶦ U+1DA6 decomposes to
 * ɪ U+026A rather than to `i`. Either leaves a name a reader typing plain
 * ASCII can never reach.
 *
 * build.py's gate 3 catches a character this map has not been told about, and
 * it is the ONLY thing that does — it aborts the build rather than emit a key
 * no reader can type. This comment claimed until 2026-08-08 that
 * `tools/validate.py` re-checked the map against the edition; it does not, and
 * never has. That tool compares the published pages against the transcription
 * modules, field by field and relation by relation, and never reads this map.
 * See `fold_map()` in build.py for the hand comparison that was done instead.
 */
const FOLD = Object.entries({
  "ʼ": "", "ʽ": "", "˙": "", "˚": "", "˘": "",
  "ă": "a", "Ă": "A", "ĕ": "e", "ĭ": "i", "Ĭ": "I", "ŏ": "o", "ŭ": "u",
  "ä": "a", "ñ": "n", "ô": "o", "ó": "o", "ɪ": "i",
  "ᶦ": "i", "ᵘ": "u", "ᵃ": "a", "ᵉ": "e",
});

const ALNUM = /[\p{L}\p{N}]/u;

/** Diacritic-free lowercase key for matching Americanist transcription. */
export function fold(value) {
  let out = value || "";
  for (const [from, to] of FOLD) {
    if (out.includes(from)) out = out.split(from).join(to);
  }
  let key = "";
  for (const character of out) if (ALNUM.test(character)) key += character;
  return key.toLowerCase();
}

/**
 * Levenshtein distance, abandoned as soon as it cannot come in under `limit`.
 *
 * The bound is what makes typo tolerance affordable: without it every
 * keystroke builds a full matrix against all 713 names.
 */
export function distance(a, b, limit) {
  if (Math.abs(a.length - b.length) > limit) return limit + 1;
  const row = Array.from({ length: b.length + 1 }, (_, i) => i);
  for (let i = 1; i <= a.length; i += 1) {
    let previous = row[0];
    row[0] = i;
    let best = i;
    for (let j = 1; j <= b.length; j += 1) {
      const stored = row[j];
      row[j] = Math.min(row[j] + 1, row[j - 1] + 1,
        previous + (a[i - 1] === b[j - 1] ? 0 : 1));
      previous = stored;
      if (row[j] < best) best = row[j];
    }
    if (best > limit) return limit + 1;
  }
  return row[b.length];
}

/**
 * How well one person answers one folded query. 0 means "not a match".
 *
 * Scored against that person's own name — never against several people's
 * names concatenated, which is what makes an edit-distance similarity
 * meaningless the moment a row stands for more than one entry.
 */
export function score(person, query) {
  if (!query) return 1;
  const { key, altKey } = person;

  if (key && key === query) return 100;
  if (altKey && altKey === query) return 92;
  if (key && key.startsWith(query)) return 80;
  if (altKey && altKey.startsWith(query)) return 72;
  if (key && key.includes(query)) return 60;
  if (altKey && altKey.includes(query)) return 52;

  if (query.length >= FUZZY_MIN_QUERY && key) {
    const limit = Math.max(1, Math.floor(query.length / 4));
    const d = distance(query, key, limit);
    if (d <= limit) return 40 - d;
  }
  return 0;
}

/* ------------------------------------------------------------- formatting -- */

const SEX_LABEL = { F: "F.", M: "M." };

/** What the plate prints wins over the edition's reading, everywhere shown. */
const sexOf = (p) => p.sexPrinted || p.sex;
const clanOf = (p) => p.clanPrinted || p.clan;
const sexText = (p) => SEX_LABEL[sexOf(p)] || sexOf(p) || "";

function displayName(person) {
  if (!person.name) return "";
  return person.altName ? `${person.name} (${person.altName})` : person.name;
}

/**
 * The name, cut into the pieces a line may begin with.
 *
 * `<wbr>` and nothing else: no hyphen, and never U+00AD, which renders one.
 * A hyphen is not in Parsons's orthography, so a reader would take it for
 * plate data.
 *
 * The seams are `build.py`'s — the rule that produces them is an editorial
 * claim about where a phonetic name may be divided (ANALYSIS.md 4a), and
 * this file does not get a second opinion about it, exactly as it does not
 * hold its own namesake rule. The `name` string itself is untouched: search,
 * sort and copy still see one word.
 */
function nameNodes(person) {
  const name = person.name;
  const seams = person.nameSeams;
  if (!seams || !seams.length) return [name];
  const out = [];
  let prev = 0;
  for (const at of seams) {
    out.push(name.slice(prev, at), document.createElement("wbr"));
    prev = at;
  }
  out.push(name.slice(prev));
  return out;
}

/**
 * What the Birth column shows — and whether the edition recorded it.
 *
 * The distinction is the whole point of this function. A year computed from a
 * recorded age is arithmetic this edition performs, not a reading of the
 * plate, so it is prefixed "c.", marked, and says where it came from.
 */
function birthCell(person) {
  if (person.birth != null) return { text: String(person.birth), estimated: false };
  if (person.estimatedBirth != null) {
    return {
      text: `c. ${person.estimatedBirth}`,
      estimated: true,
      why: `Not printed on the plate. Calculated from the recorded ${person.estimatedFrom}` +
        (person.estimatedFrom === "age at recording"
          ? ", and the fieldwork spans two years, so it is good to about a year."
          : "."),
    };
  }
  return { text: "", estimated: false };
}

function deathCell(person) {
  if (person.death != null) return { text: `d. ${person.death}` };
  if (person.died) return { text: "d." };
  return { text: "" };
}

const sortableBirth = (p) => (p.birth != null ? p.birth : p.estimatedBirth);
const sortableDeath = (p) => (p.death != null ? p.death : null);

/* --------------------------------------------------------------- namesake -- */

/**
 * Two people who share a name, a sex and a clan, and are still two people.
 *
 * The list sorts by name, so those two land next to each other and read as a
 * duplicate — which is how the first of them was reported. What is drawn here
 * is not a guess: `build.py` finds every such pair by rule and refuses to
 * build until each one is adjudicated by hand in its `NAMESAKES` table, so the
 * verdict and the finding below are always the edition's evidence, never this
 * file's opinion.
 *
 * This USED to be computed here, from a `twinKey` of the group's first entry.
 * That was a second implementation of the build's rule — the exact mistake the
 * fold map is structured to prevent — and it was wrong in two ways the build
 * is not: it compared only the entry the row shows, and it had nothing to say
 * beyond "no plate cross-references them", which does not tell a reader
 * whether anybody looked.
 */
function namesakeNotes(ctx, group) {
  return (ctx.namesakes[group.key] || [])
    .map((note) => ({ ...note, group: ctx.groupByKey.get(note.other) }))
    .filter((note) => note.group);
}

/** How a person is cited: the plate and number of the earliest entry. */
function addressOf(ctx, group) {
  const lead = group.people[0];
  return `${lead.table} · ${lead.number}`;
}

/* ------------------------------------------------------------------ group -- */

/**
 * A person, which is not the same thing as a plate entry.
 *
 * 79 of these people are drawn on more than one plate — Parsons says so
 * herself for 65 of them, "See Gen. I, 68"; the other 14 are identified by
 * this tool and say so on the page — so 713 entries are 620 people. A group holds
 * every entry for one person, earliest plate first; a person on one plate is a
 * group of one, so there is no second code path.
 *
 * The entries are NOT collapsed into a merged record. Each plate is recorded
 * as it prints, and they disagree: Genealogy I calls her Yo˙ʼs˙iro and
 * Genealogy III calls her Yoʼsiro; Genealogy I gives 33's age as 18 where
 * Genealogy II gives 17. The row shows the earliest plate's reading and the
 * detail panel shows every plate's, side by side.
 */
function buildGroups(people, identities) {
  const byKey = new Map(people.map((p) => [`${p.table}-${p.id}`, p]));
  const claimed = new Set();
  const groups = [];

  for (const [canonical, group] of Object.entries(identities || {})) {
    const members = group.members.map((k) => byKey.get(k)).filter(Boolean);
    if (members.length < 2) continue;
    for (const k of group.members) claimed.add(k);
    groups.push({ key: canonical, people: members, links: group.links || [] });
  }
  for (const person of people) {
    const key = `${person.table}-${person.id}`;
    if (!claimed.has(key)) groups.push({ key, people: [person], links: [] });
  }
  return groups;
}

/** The first entry that records this field — plates differ, and some omit. */
function firstOf(group, field) {
  for (const person of group.people) if (person[field]) return person[field];
  return "";
}

function groupBirth(group) {
  for (const person of group.people) {
    if (person.birth != null || person.estimatedBirth != null) return person;
  }
  return group.people[0];
}

function groupDeath(group) {
  for (const person of group.people) if (person.death != null || person.died) return person;
  return group.people[0];
}

const groupSex = (g) => SEX_LABEL[firstOf(g, "sexPrinted") || firstOf(g, "sex")]
  || firstOf(g, "sexPrinted") || firstOf(g, "sex") || "";
const groupClan = (g) => firstOf(g, "clanPrinted") || firstOf(g, "clan");

/* -------------------------------------------------------------------- dom -- */

function el(tag, props, ...children) {
  const node = document.createElement(tag);
  for (const [name, value] of Object.entries(props || {})) {
    if (value === false || value == null) continue;
    if (name === "class") node.className = value;
    else if (name === "text") node.textContent = value;
    else if (name.startsWith("on")) node.addEventListener(name.slice(2), value);
    else node.setAttribute(name, value === true ? "" : value);
  }
  for (const child of children.flat(Infinity)) {
    if (child == null || child === false || child === "") continue;
    node.append(child.nodeType ? child : document.createTextNode(String(child)));
  }
  return node;
}

function debounce(fn, ms) {
  let timer = 0;
  const wrapped = (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), ms);
  };
  wrapped.cancel = () => clearTimeout(timer);
  return wrapped;
}

const isTypingTarget = (node) => !!node
  && (node.isContentEditable
    || ["INPUT", "SELECT", "TEXTAREA"].includes(node.tagName));

/* -------------------------------------------------------- filter dropdown -- */

/**
 * A multi-select on <details> that closes on outside click and on Escape, and
 * that updates its own summary in place.
 *
 * Both behaviours are why this is a component rather than markup. A bare
 * <details> menu stays open until its summary is clicked again, stranding it
 * over the rows below; and rebuilding it to refresh the summary text would
 * close it after every single checkbox.
 */
function checkboxFilter({ label, allLabel, options, onChange }) {
  const selected = new Set();
  const text = el("span", { class: "cbf-text" });
  const summary = el("summary", {}, text);
  const menu = el("div", { class: "cbf-menu", role: "group", "aria-label": label });
  const boxes = [];

  for (const option of options) {
    if (option.groupLabel) {
      menu.append(el("p", { class: "cbf-group", text: option.groupLabel }));
      continue;
    }
    const box = el("input", { type: "checkbox" });
    box.addEventListener("change", () => {
      if (box.checked) selected.add(option.value); else selected.delete(option.value);
      paint();
      onChange(new Set(selected));
    });
    boxes.push({ box, value: option.value });
    menu.append(el("label", { class: "cbf-option" }, box,
      el("span", { text: option.label })));
  }

  const details = el("details", { class: "cbf" }, summary, menu);

  function paint() {
    let caption = allLabel;
    if (selected.size === 1) {
      const only = [...selected][0];
      caption = (options.find((o) => o.value === only) || {}).label || "1 selected";
    } else if (selected.size > 1) {
      caption = `${selected.size} selected`;
    }
    text.textContent = caption;
    summary.setAttribute("aria-label", `${label} filter, ${caption}`);
    details.classList.toggle("cbf-on", selected.size > 0);
  }

  const closeOutside = (event) => {
    if (details.open && !details.contains(event.target)) details.open = false;
  };
  const closeEscape = (event) => {
    if (event.key === "Escape" && details.open) {
      event.stopPropagation();
      details.open = false;
      summary.focus();
    }
  };
  details.addEventListener("toggle", () => {
    const add = details.open ? "addEventListener" : "removeEventListener";
    document[add]("pointerdown", closeOutside);
    document[add]("keydown", closeEscape);
  });

  paint();

  return {
    node: details,
    /** Set the boxes without firing onChange — used when the URL is the source. */
    set(values) {
      selected.clear();
      for (const v of values) selected.add(v);
      for (const { box, value } of boxes) box.checked = selected.has(value);
      paint();
    },
    close() { details.open = false; },
  };
}

/* ------------------------------------------------------------ detail pane -- */

function copyButton(text) {
  const button = el("button", {
    type: "button", class: "copy", "aria-label": `Copy ${text}`, text: "Copy",
  });
  button.addEventListener("click", async (event) => {
    event.stopPropagation();
    let ok = false;
    try {
      await navigator.clipboard.writeText(text);
      ok = true;
    } catch {
      // The clipboard API needs a secure context; the page may be opened from
      // file://. Fall back rather than throw an unhandled rejection.
      const scratch = el("textarea", { class: "offscreen" });
      scratch.value = text;
      document.body.append(scratch);
      scratch.select();
      try { ok = document.execCommand("copy"); } catch { ok = false; }
      scratch.remove();
    }
    button.textContent = ok ? "Copied" : "Press ⌘C";
    setTimeout(() => { button.textContent = "Copy"; }, 1600);
  });
  return button;
}

/** The mark this edition puts on a reading the plate does not itself state. */
function dagger(ctx, person) {
  return el("a", {
    class: "dagger",
    href: `${ctx.tableByNumeral.get(person.table).url}#${ctx.meta.paternityNote}`,
    target: ctx.target,
    rel: "noreferrer",
    title: "Editorial attribution — the plate does not assign this. " +
      "Opens the edition's note.",
    "aria-label": "Editorial attribution, see the edition's note",
    onclick: (e) => e.stopPropagation(),
  }, "†");
}

/**
 * One "Parents" / "Spouse" / "Children" row.
 *
 * `refs` are bare ids resolved against the person index. The index stores no
 * second copy of a name, so a chip cannot disagree with the row it points at.
 */
function relationRow(ctx, person, label, refs, { editorial, editorialRefs } = {}) {
  if (!refs || refs.length === 0) return null;
  const table = ctx.tableByNumeral.get(person.table);
  const marked = new Set(editorialRefs || []);

  return el("div", { class: "rel-row" },
    el("span", { class: "rel-label" }, label, editorial && dagger(ctx, person)),
    el("span", { class: "rel-links" },
      refs.map((id) => {
        const other = ctx.byKey.get(`${person.table}-${id}`);
        return el("a", {
          class: "rel-link",
          href: `${table.url}#p${id}`,
          target: ctx.target,
          rel: "noreferrer",
          onclick: (e) => e.stopPropagation(),
        },
          el("span", { class: "rel-number", text: other ? other.number : id }),
          el("span", { text: (other && other.name) || "———" }),
          marked.has(id) && dagger(ctx, person));
      })));
}

function sicMark(what) {
  return el("span", {
    class: "sic",
    title: `The plate prints this ${what}; the edition's reading differs. ` +
      "Both are searchable.",
  }, "sic");
}

function estimateMark(why) {
  return el("span", { class: "est", title: why, tabindex: "0" }, "est.");
}

/** One plate's reading of one person: the column inside the detail panel. */
function entryColumn(ctx, person) {
  const table = ctx.tableByNumeral.get(person.table);
  const birth = birthCell(person);
  const death = deathCell(person);
  const name = displayName(person);

  const fields = [
    ["Name", name || "———", name ? copyButton(name) : null],
    ["Sex", sexText(person), person.sexPrinted ? sicMark("sex") : null],
    ["Birth", birth.text, birth.estimated ? estimateMark(birth.why) : null],
    ["Death", death.text, null],
    ["Age", person.age && `${person.age} at recording`, null],
    ["Clan", clanOf(person), person.clanPrinted ? sicMark("clan") : null],
    ["Origin", person.origin, null],
    ["Generation", person.generation, null],
  ].filter(([, value]) => value !== "" && value != null);

  const panel = el("div", { class: "detail-col" },
    el("a", {
      class: "badge", href: person.href, target: ctx.target, rel: "noreferrer",
      onclick: (e) => e.stopPropagation(),
    }, `${person.table} · ${person.number}`,
      el("span", { class: "ext", "aria-hidden": true }, "↗")),
    el("dl", { class: "detail-fields" },
      fields.map(([label, value, extra]) => [
        el("dt", { text: label }),
        el("dd", {}, String(value), extra),
      ])));

  if (person.crossRef) {
    panel.append(el("p", { class: "detail-note" },
      el("span", { class: "note-label", text: "Printed on the plate" }),
      el("q", { text: person.crossRef })));
  }

  const rel = ctx.relationships[`${person.table}-${person.id}`];
  if (rel) {
    const spouses = rel.spouses || [];
    const rows = [
      relationRow(ctx, person, "Parents", rel.parents,
        { editorial: rel.parentsEditorial }),
      relationRow(ctx, person, spouses.length === 1 ? "Spouse" : "Spouses", spouses),
      ...(rel.children || []).map((g) =>
        relationRow(ctx, person, g.label, g.refs, { editorial: g.editorial })),
    ].filter(Boolean);
    if (rows.length) panel.append(el("div", { class: "rel-list" }, rows));
  }

  panel.append(el("p", { class: "detail-source" },
    "Transcribed from ", table.plate, ". ",
    el("a", {
      href: person.href, target: ctx.target, rel: "noreferrer",
      text: "Open this entry in the chart",
      onclick: (e) => e.stopPropagation(),
    })));

  return panel;
}

/**
 * The expanded row: one column per plate this person is drawn on.
 *
 * With more than one column the panel also shows WHY the entries were joined —
 * the line Parsons prints, and the number it resolves to where the two differ.
 * Merging entries is a claim, so the evidence for it is on the page.
 */
function detailPanel(ctx, group) {
  const multi = group.people.length > 1;
  const panel = el("div", { class: "detail" });

  if (multi) {
    panel.append(el("h3", { class: "detail-head" },
      `Drawn on ${group.people.length} plates`));
  }

  panel.append(el("div", { class: `detail-columns${multi ? " multi" : ""}` },
    group.people.map((person) => entryColumn(ctx, person))));

  if (multi && group.links.length) {
    panel.append(el("div", { class: "joined" },
      el("span", { class: "note-label", text: "Why these are one person" }),
      el("ul", {}, group.links.map((link) => {
        const from = ctx.byKey.get(link.a);
        const to = ctx.byKey.get(link.b);
        if (!from || !to) return null;
        // An identification this tool makes reads differently from one the
        // edition prints, and must never be able to pass for it: there is no
        // quoted line, and it says whose claim it is.
        if (link.source === "inferred") {
          return el("li", { class: "join-inferred" },
            el("span", { class: "inferred-mark", text: "Not printed" }),
            ` ${from.table} · ${from.number} and ${to.table} · ${to.number} are `,
            "identified here, not by the edition — ",
            el("span", { class: "evidence", text: `${link.evidence}.` }));
        }
        const shifted = link.resolution !== "exact";
        return el("li", {},
          `${from.table} · ${from.number} prints `,
          el("q", { text: link.printed }),
          shifted
            ? [" — ", el("span", { class: "shifted", text: link.resolution }),
              `, so it reaches ${to.table} · ${to.number}`]
            : `, which is ${to.table} · ${to.number}`,
          el("span", { class: "evidence", text: ` Confirmed by ${link.evidence}.` }));
      }).filter(Boolean))));
  }

  // Not "no plate cross-references them", which was all this said before. That
  // is true of every pair of strangers in the edition and tells a reader
  // nothing about whether these two were looked at. Each note now carries the
  // verdict and the evidence for it.
  for (const note of namesakeNotes(ctx, group)) {
    const other = note.group;
    const lead = other.people[0];
    const open = note.verdict === "open";
    panel.append(el("p", { class: `detail-note namesake-note${open ? " is-open" : ""}` },
      el("span", {
        class: "note-label",
        text: open ? "Same name — not established" : "Same name, different person",
      }),
      el("a", {
        class: "twin-link", href: lead.href, target: ctx.target, rel: "noreferrer",
        text: `${ctx.tableByNumeral.get(lead.table).plate} · ${lead.number}`,
        onclick: (e) => e.stopPropagation(),
      }),
      other.people.length > 1
        ? ` (drawn on ${other.people.length} plates) `
        : " ",
      open
        ? "carries the same name, sex and clan. Whether the two are one person is not established, and they are kept apart. "
        : "carries the same name, sex and clan and is somebody else. ",
      el("span", { class: "evidence", text: note.finding })));
  }

  return panel;
}

/* -------------------------------------------------------------------- row -- */

/**
 * One row: a summary button, and a detail panel built the first time it opens.
 *
 * The summary carries `tabindex="-1"`; the list hands `0` to exactly one row
 * at a time, so the rows are one tab stop and the arrow keys move within them.
 */
/**
 * The mark a row carries when another row holds the same name.
 *
 * It is on the CLOSED row on purpose. The apparent duplicate is something the
 * reader meets while scanning an alphabetical list, so an explanation that
 * only appears once the row is opened arrives after they have already decided
 * the tool is repeating itself. It names the other row, so the two are tied
 * together without opening either.
 *
 * `≠` for a pair the plates settle, `?` for one they do not — never the same
 * mark for both. Merging on a name is what this tool refuses to do; quietly
 * implying a question is closed would be the same error with better manners.
 */
function namesakeMark(ctx, group) {
  const notes = namesakeNotes(ctx, group);
  if (!notes.length) return null;

  const open = notes.some((note) => note.verdict === "open");
  const others = notes.map((note) => addressOf(ctx, note.group)).join(", ");
  const label = open
    ? `Same name, sex and clan as ${others}. Whether they are one person is not established.`
    : `Same name, sex and clan as ${others}, and a different person.`;

  return el("span", {
    class: `namesake-mark${open ? " is-open" : ""}`,
    title: `${label} ${notes.map((note) => note.finding).join(" ")}`,
    "aria-label": label,
  }, el("span", { "aria-hidden": true, text: open ? "?" : "≠" }),
    el("span", { "aria-hidden": true, class: "namesake-who", text: others }));
}

function personRow(ctx, group, onToggle) {
  const lead = group.people[0];
  const birth = birthCell(groupBirth(group));
  const death = deathCell(groupDeath(group));
  const rowId = `lg-r-${group.key}`;
  const panelId = `lg-d-${group.key}`;
  const multi = group.people.length > 1;

  const summary = el("button", {
    type: "button", class: "row-summary", id: rowId, tabindex: "-1",
    "aria-expanded": "false", "aria-controls": panelId,
  },
    el("span", { class: "grid" },
      el("span", { class: "cell name" },
        lead.name ? nameNodes(lead) : el("span", { class: "unnamed" }, "———"),
        lead.altName && el("span", { class: "alt", text: ` (${lead.altName})` }),
        namesakeMark(ctx, group)),
      el("span", { class: "cell sex", text: groupSex(group) }),
      el("span", {
        class: `cell birth${birth.estimated ? " is-est" : ""}`,
        title: birth.estimated ? birth.why : null,
        text: birth.text,
      }),
      el("span", { class: "cell death", text: death.text }),
      el("span", { class: "cell clan", text: groupClan(group) })),
    // Every plate this person is drawn on, in plate order. One chip for most
    // people; the reference showed several here too, but keyed on a name
    // coincidence rather than on Parsons's own cross-reference.
    el("span", { class: `ref${multi ? " multi" : ""}` },
      el("span", { class: "ref-links" },
        group.people.map((person) => el("span", { class: "ref-text" },
          person.table, " ", el("b", {}, "·"), " ", person.number)))),
    el("span", { class: "chev", "aria-hidden": true }, el("span", {})));

  const article = el("article", { class: "row", "data-key": group.key }, summary);

  article.setOpen = (open) => {
    if (open === article.classList.contains("open")) return;
    article.classList.toggle("open", open);
    summary.setAttribute("aria-expanded", String(open));
    if (open) {
      const panel = detailPanel(ctx, group);
      panel.id = panelId;
      panel.setAttribute("role", "region");
      panel.setAttribute("aria-labelledby", rowId);
      article.append(panel);
    } else {
      article.querySelector(".detail")?.remove();
    }
    onToggle(group.key, open);
  };

  summary.addEventListener("click", () => {
    article.setOpen(!article.classList.contains("open"));
  });

  return article;
}

/* -------------------------------------------------------------- url state -- */

/**
 * The whole of the reader's state, in a query string.
 *
 * A finding aid whose results cannot be linked is half a finding aid: a
 * citation, a note to a colleague and a browser bookmark all want to name one
 * search. Only what differs from the default is written, so an untouched page
 * has a clean URL.
 */
const DEFAULTS = () => ({
  name: "", number: "", sex: "all", birth: "", death: "",
  tables: new Set(), clans: new Set(),
  sortKey: "name", sortDir: "asc",
});

function stateToParams({ state, sortTouched, open }) {
  const params = new URLSearchParams();
  if (state.name) params.set("q", state.name);
  if (state.number) params.set("n", state.number);
  if (state.tables.size) params.set("t", [...state.tables].join(","));
  if (state.sex !== "all") params.set("sex", state.sex);
  if (state.clans.size) params.set("clan", [...state.clans].join(","));
  if (state.birth) params.set("b", state.birth);
  if (state.death) params.set("d", state.death);
  // Written whenever the reader chose an order, even where that order is the
  // default one: choosing it is what stops relevance overriding it, and a
  // reload that dropped the fact would quietly re-sort the page under them.
  if (sortTouched) {
    params.set("sort", state.sortKey);
    params.set("dir", state.sortDir);
  }
  if (open) params.set("open", open);
  return params;
}

/** Read a query string back. Unknown values fall back rather than throw. */
function paramsToState(params, meta) {
  const state = DEFAULTS();
  const numerals = new Set(meta.tables.map((t) => t.numeral));
  const clans = new Set([...meta.clans, ...meta.otherInClanPosition, "__none__"]);

  state.name = params.get("q") || "";
  // Exclusive, as in patch(): a URL carrying both is answered by the name.
  state.number = state.name
    ? "" : (params.get("n") || "").replace(/\D/g, "").slice(0, 4);
  state.birth = (params.get("b") || "").replace(/\D/g, "").slice(0, 4);
  state.death = params.get("d") || "";
  if (["F", "M", "none"].includes(params.get("sex"))) state.sex = params.get("sex");
  for (const t of (params.get("t") || "").split(",")) {
    if (numerals.has(t)) state.tables.add(t);
  }
  for (const c of (params.get("clan") || "").split(",")) {
    if (clans.has(c)) state.clans.add(c);
  }
  const sorted = ["name", "birth", "death", "ref"].includes(params.get("sort"));
  if (sorted) {
    state.sortKey = params.get("sort");
    state.sortDir = params.get("dir") === "desc" ? "desc" : "asc";
  }
  return { state, sorted, open: params.get("open") || "" };
}

/* ------------------------------------------------------------------- list -- */

/**
 * The one list: filter header, rows, and the selection that produces them.
 *
 * Every control on the page writes here through `patch()`, including the
 * search box above it, so there is exactly one place a query can live and
 * exactly one thing to serialise into the URL.
 */
class PersonList {
  constructor(ctx, { onChange } = {}) {
    this.ctx = ctx;
    this.onChange = onChange || (() => {});
    this.state = DEFAULTS();
    this.sortTouched = false;
    this.open = "";           // the expanded row, if any
    this.pendingReveal = "";  // a row the URL asked for, to scroll to once
    this.sortButtons = [];
    this.inputs = {};
    this.rendered = 0;
    this.active = 0;          // roving tabindex
    this.matches = [];
    this.node = this.build();
  }

  /* -- construction -- */

  build() {
    this.head = el("div", {
      class: "head", role: "group", "aria-label": "Sort and filter",
    });
    this.buildHead();

    this.sentinel = el("div", { class: "sentinel", "aria-hidden": true });
    this.list = el("div", { class: "list" }, this.sentinel);
    this.list.addEventListener("keydown", (e) => this.onKey(e));

    this.empty = el("div", { class: "empty", hidden: true },
      el("span", { class: "empty-text" }),
      el("button", {
        type: "button", class: "link-button", text: "Clear filters",
        onclick: () => this.reset(),
      }));

    this.observer = new IntersectionObserver(
      (entries) => { if (entries.some((e) => e.isIntersecting)) this.renderMore(); },
      { rootMargin: "400px" },
    );
    this.observer.observe(this.sentinel);

    return el("div", { class: "person-list" }, this.head, this.empty, this.list);
  }

  /**
   * `extra` adds a column class; `srLabel` is what the button is called aloud,
   * for a heading like "Table · #" that reads as punctuation when spoken.
   */
  sortButton(label, key, { extra = "", srLabel = label } = {}) {
    const button = el("button", { type: "button", class: `sort${extra ? ` ${extra}` : ""}` },
      el("span", { text: label }),
      el("span", { class: "sort-icon", "aria-hidden": true },
        el("span", { class: "tri up" }), el("span", { class: "tri down" })));
    button.addEventListener("click", () => {
      const flip = this.state.sortKey === key;
      // Once a column is chosen the reader has asked for that order, so
      // relevance stops overriding it.
      this.sortTouched = true;
      this.patch({
        sortKey: key,
        sortDir: flip && this.state.sortDir === "asc" ? "desc" : "asc",
      });
    });
    this.sortButtons.push({ button, key, label: srLabel });
    return button;
  }

  yearField(cls, label, key) {
    const input = el("input", {
      type: "text", inputmode: "numeric", maxlength: "4", placeholder: "Year",
      "aria-label": `Filter by ${label.toLowerCase()} year`,
    });
    const run = debounce(() => this.patch({ [key]: input.value }), DEBOUNCE_MS);
    input.addEventListener("input", () => {
      if (key === "birth") input.value = input.value.replace(/\D/g, "").slice(0, 4);
      run();
    });
    this.inputs[key] = input;
    return el("div", { class: `field ${cls}` }, this.sortButton(label, key), input);
  }

  buildHead() {
    const { meta } = this.ctx;

    // The Name column sorts but does not filter: the search box above owns the
    // name query, and a second name input would be a second place for it.
    const nameField = el("div", { class: "field field-name" },
      this.sortButton("Name", "name"));

    const sexSelect = el("select", { "aria-label": "Filter by sex" },
      el("option", { value: "all", text: "All" }),
      el("option", { value: "F", text: "Female" }),
      el("option", { value: "M", text: "Male" }),
      el("option", { value: "none", text: "Not recorded" }));
    sexSelect.addEventListener("change", () => this.patch({ sex: sexSelect.value }));
    this.inputs.sex = sexSelect;

    this.clanFilter = checkboxFilter({
      label: "Clan",
      allLabel: "All clans",
      options: [
        ...meta.clans.map((c) => ({ value: c, label: c })),
        ...(meta.otherInClanPosition.length
          ? [{ groupLabel: "Printed in the clan position, not a clan" },
            ...meta.otherInClanPosition.map((c) => ({ value: c, label: c }))]
          : []),
        { groupLabel: " " },
        { value: "__none__", label: "Not recorded" },
      ],
      onChange: (clans) => this.patch({ clans }),
    });

    this.head.append(
      el("div", { class: "grid head-grid" },
        nameField,
        el("div", { class: "field field-sex" },
          el("span", { class: "field-label", text: "Sex" }), sexSelect),
        this.yearField("field-birth", "Birth", "birth"),
        this.yearField("field-death", "Death", "death"),
        el("div", { class: "field field-clan" },
          el("span", { class: "field-label", text: "Clan" }),
          this.clanFilter.node)),
      // Heads the chip column on the right of every row, and sorts by it:
      // plate order is the order the plates themselves are printed in, which is
      // how a reader holding one navigates. It does not *choose* a table — that
      // is the search bar above, which stays the only copy of that state.
      this.sortButton("Table · #", "ref",
        { extra: "head-ref", srLabel: "table and number" }),
      el("span", { class: "head-spacer", "aria-hidden": true }));
  }

  /* -- state -- */

  /**
   * The single entry point: merge, redraw, and tell the page.
   *
   * The two searches are EXCLUSIVE. A name and a plate number answer
   * different questions — "who is called this, anywhere" and "who is this
   * number on this plate" — and a reader who starts one has finished with the
   * other. Enforced here rather than in the two input handlers, so the rule
   * also holds for a hand-written URL.
   */
  patch(partial) {
    if (partial.name) partial.number = "";
    if (partial.number) partial.name = "";
    Object.assign(this.state, partial);
    this.refresh();
    this.onChange(this);
  }

  reset() {
    Object.assign(this.state, DEFAULTS());
    this.sortTouched = false;
    this.syncControls();
    this.patch({});
  }

  /** Push `state` back into the controls — for the URL and for reset(). */
  syncControls() {
    this.inputs.birth.value = this.state.birth;
    this.inputs.death.value = this.state.death;
    this.inputs.sex.value = this.state.sex;
    this.clanFilter.set(this.state.clans);
    this.clanFilter.close();
  }

  /* -- selection -- */

  matching() {
    const s = this.state;
    const query = fold(s.name);
    const numeric = s.number;      // only ever the number box; see patch()
    const { clans, tables } = s;

    // A filter or a query tests EVERY entry of a person and keeps the person
    // if any one matches. Searching Table III for 74 finds Shayaʼai, and the
    // row shows her on I, II and III — one person, not three results.
    const any = (group, test) => group.people.some(test);

    const rows = [];
    for (const group of this.ctx.groups) {
      if (tables.size && !any(group, (p) => tables.has(p.table))) continue;

      if (s.sex !== "all" && !any(group, (p) => {
        const value = sexOf(p);
        return s.sex === "none" ? !value : value === s.sex;
      })) continue;

      if (clans.size && !any(group, (p) => (
        (p.clan && clans.has(p.clan))
        || (p.clanPrinted && clans.has(p.clanPrinted))
        || (!p.clan && clans.has("__none__"))
      ))) continue;

      if (s.birth && !any(group, (p) => {
        const value = sortableBirth(p);
        return value != null && String(value).includes(s.birth);
      })) continue;

      if (s.death && !any(group, (p) => (
        deathCell(p).text.toLowerCase().includes(s.death.trim().toLowerCase())
      ))) continue;

      let rank = 1;
      if (query || numeric) {
        rank = 0;
        for (const person of group.people) {
          if (query) rank = Math.max(rank, score(person, query));
          // A number is a reference to one plate, so it must match on an entry
          // that is ON that plate. Testing group membership and the number
          // separately answers "Table I, 67" with the person who is II · 67
          // and happens to be I · 24 as well.
          // Exact, not a prefix: a number IS a person, so 43 answers with 43
          // and never with 430. Two rows only where Parsons prints one number
          // on two people — II · 101 and III · 258 and 259.
          if (numeric && person.number === numeric
            && (!tables.size || tables.has(person.table))) {
            rank = Math.max(rank, 95);
          }
        }
        if (rank === 0) continue;
      }
      rows.push({ group, rank });
    }

    const sign = s.sortDir === "asc" ? 1 : -1;
    const lead = (r) => r.group.people[0];
    const order = (a, b) =>
      lead(a).table.localeCompare(lead(b).table) || lead(a).id - lead(b).id;

    // Plate order among people the plate leaves unnamed — there are 203 such
    // entries, and they are the one category the reference dropped from its
    // directory outright.
    const byName = (a, b) => lead(a).name.localeCompare(
      lead(b).name, undefined, { sensitivity: "base" }) || order(a, b);

    rows.sort((a, b) => {
      if ((query || numeric) && !this.sortTouched && a.rank !== b.rank) {
        return b.rank - a.rank;
      }
      // An absence is not a low value: an unnamed person and an unrecorded
      // year both sink, whichever direction the column is sorted.
      if (s.sortKey === "name") {
        if (!lead(a).name && !lead(b).name) return order(a, b);
        if (!lead(a).name) return 1;
        if (!lead(b).name) return -1;
        return sign * byName(a, b);
      }
      // Plate order, and for someone drawn on more than one plate the first
      // plate they appear on — the same chip the column shows first.
      if (s.sortKey === "ref") return sign * order(a, b);
      const get = s.sortKey === "birth"
        ? (r) => sortableBirth(groupBirth(r.group))
        : (r) => sortableDeath(groupDeath(r.group));
      const av = get(a);
      const bv = get(b);
      if (av == null && bv == null) return byName(a, b);
      if (av == null) return 1;
      if (bv == null) return -1;
      return sign * (av - bv) || byName(a, b);
    });

    return rows.map((r) => r.group);
  }

  /* -- rendering -- */

  refresh() {
    this.matches = this.matching();
    this.rendered = 0;
    this.active = 0;
    this.list.replaceChildren(this.sentinel);
    this.paintSort();

    const none = this.matches.length === 0;
    this.empty.hidden = !none;
    this.list.hidden = none;
    if (none) {
      this.open = "";
      this.empty.querySelector(".empty-text").textContent = this.emptyText();
      return;
    }
    this.renderMore();

    // A row the URL named is scrolled to, once. A row the reader had open
    // stays open across a re-filter but never moves the page under them.
    const reveal = this.pendingReveal;
    this.pendingReveal = "";
    if (reveal) this.reveal(reveal);
    else if (this.open) this.restoreOpen();
  }

  /**
   * Why nothing matched, where the answer is knowable.
   *
   * The name box no longer reads digits as a plate number, so typing one there
   * is a dead end — and a reader with a plate in front of them will do it.
   * Naming the other control costs a sentence; leaving them at "no person
   * matches" costs them the search.
   */
  emptyText() {
    const { name, number, tables } = this.state;
    if (/^\d+$/.test(name.trim())) {
      return `Nobody is called “${name.trim()}”. To look up a plate number, `
        + "choose a table and type it in the # box.";
    }
    if (number) {
      const chosen = this.ctx.meta.tables.filter((t) => tables.has(t.numeral));
      const where = chosen.length === 1 ? chosen[0].plate
        : chosen.length ? `the ${chosen.length} tables chosen` : "any table";
      return `No person is numbered ${number} on ${where}.`;
    }
    return "No person matches. Check the table and number, or try a shorter spelling.";
  }

  restoreOpen() {
    const index = this.matches.findIndex((g) => g.key === this.open);
    if (index < 0) { this.open = ""; return; }
    if (index < this.rendered) this.rows()[index].setOpen(true);
  }

  renderMore() {
    if (this.rendered >= this.matches.length) return;
    const stop = Math.min(this.rendered + CHUNK, this.matches.length);
    const fragment = document.createDocumentFragment();
    for (let i = this.rendered; i < stop; i += 1) {
      fragment.append(personRow(this.ctx, this.matches[i], (key, open) => {
        this.open = open ? key : "";
        this.onChange(this);
      }));
    }
    this.list.insertBefore(fragment, this.sentinel);
    this.rendered = stop;
    this.paintTabStop();

    // If the sentinel is still on screen the observer will not fire again on
    // its own — it reports changes, not states. Re-observing forces a fresh
    // callback, so a tall viewport keeps filling instead of stopping at 60.
    if (this.rendered < this.matches.length) {
      this.observer.unobserve(this.sentinel);
      requestAnimationFrame(() => this.observer.observe(this.sentinel));
    }
  }

  /** Render as far as `key`, open it, and bring it into view. */
  reveal(key) {
    const index = this.matches.findIndex((g) => g.key === key);
    if (index < 0) { this.open = ""; return; }
    while (this.rendered <= index) this.renderMore();
    const row = this.rows()[index];
    row?.setOpen(true);
    this.active = index;
    this.paintTabStop();
    row?.scrollIntoView({ block: "center" });
  }

  rows() {
    return [...this.list.querySelectorAll(".row")];
  }

  paintSort() {
    for (const { button, key, label } of this.sortButtons) {
      const active = this.state.sortKey === key;
      const dir = this.state.sortDir;
      button.classList.toggle("active", active);
      button.querySelector(".up").classList.toggle("on", active && dir === "asc");
      button.querySelector(".down").classList.toggle("on", active && dir === "desc");
      button.setAttribute("aria-label", active
        ? `Sort by ${label}, currently ${dir === "asc" ? "ascending" : "descending"}`
        : `Sort by ${label}`);
    }
  }

  /* -- keyboard -- */

  /**
   * The rows are one tab stop, not 620.
   *
   * Tab reaches the list and leaves it again; the arrow keys move within it.
   * Anything else would put the footer 620 tab presses away.
   */
  paintTabStop() {
    const rows = this.rows();
    if (this.active >= rows.length) this.active = Math.max(0, rows.length - 1);
    rows.forEach((row, i) => {
      row.querySelector(".row-summary").tabIndex = i === this.active ? 0 : -1;
    });
  }

  focusRow(index) {
    if (index < 0 || index >= this.matches.length) return;
    while (this.rendered <= index) this.renderMore();
    this.active = index;
    this.paintTabStop();
    const row = this.rows()[index];
    row.querySelector(".row-summary").focus();
    row.scrollIntoView({ block: "nearest" });
  }

  onKey(event) {
    const summary = event.target.closest?.(".row-summary");
    if (!summary) return;
    const index = this.rows().indexOf(summary.parentElement);
    const go = { ArrowDown: index + 1, ArrowUp: index - 1, Home: 0,
      End: this.matches.length - 1 }[event.key];

    if (go != null) {
      event.preventDefault();
      this.focusRow(go);
    } else if (event.key === "Escape" && summary.parentElement.classList.contains("open")) {
      event.preventDefault();
      summary.parentElement.setOpen(false);
    }
  }

  destroy() {
    this.observer.disconnect();
  }
}

/* ------------------------------------------------------------------ mount -- */

/**
 * Render the finding aid into `host`.
 *
 * @param {Element} host
 * @param {object}  options
 * @param {object}  options.data          index from build.py
 * @param {string}  [options.target]      link target, default "_blank"
 * @param {boolean} [options.chrome]      draw the title block, default true
 * @param {boolean} [options.themeToggle] draw a light/dark button, default true
 * @param {boolean} [options.urlState]    read and write the query string,
 *                                        default true
 * @returns {{ node: Element, destroy: () => void }}
 */
export function mountSearch(host, options = {}) {
  const data = options.data;
  if (!data || !Array.isArray(data.people) || !data.meta) {
    throw new TypeError("mountSearch: options.data must be a built search index");
  }

  const ctx = {
    meta: data.meta,
    people: data.people,
    relationships: data.relationships || {},
    target: options.target || "_blank",
    tableByNumeral: new Map(data.meta.tables.map((t) => [t.numeral, t])),
    byKey: new Map(data.people.map((p) => [`${p.table}-${p.id}`, p])),
    groups: buildGroups(data.people, data.identities),
    // Adjudicated in build.py, keyed by group. An index built before this
    // existed simply has none, and every row renders without a mark.
    namesakes: data.namesakes || {},
  };

  // Namesake notes name the other PERSON, not the other entry, so they are
  // resolved through the groups rather than through `byKey`.
  ctx.groupByKey = new Map(ctx.groups.map((group) => [group.key, group]));

  const root = el("div", { class: "laguna-search" });
  const count = el("p", { class: "count", role: "status", "aria-live": "polite" });

  /* -- the list ---------------------------------------------------------- */
  const list = new PersonList(ctx, {
    onChange: (self) => {
      const n = self.matches.length;
      count.textContent = n === ctx.groups.length
        ? `${n} people`
        : `${n} of ${ctx.groups.length} people`;
      paintSearchBar(self.state);
      writeUrl(self);
    },
  });

  /* -- the search bar ---------------------------------------------------- */
  const nameInput = el("input", {
    id: "lg-name", type: "search", autocomplete: "off",
    placeholder: "Enter a name, e.g. Nayowaitsa", "aria-label": "Search by name",
  });
  const numberInput = el("input", {
    id: "lg-number", inputmode: "numeric", maxlength: "4", placeholder: "000",
    "aria-label": "Person number",
  });

  // Each box cancels the other's pending keystroke as well as its state, or a
  // debounce in flight would put the abandoned search back a tick later.
  // `paintSearchBar` empties whichever box is not being typed in.
  const nameSoon = debounce((value) => list.patch({ name: value }), DEBOUNCE_MS);
  nameInput.addEventListener("input", () => {
    numberSoon.cancel();
    nameSoon(nameInput.value.trim());
  });

  const numberSoon = debounce((value) => list.patch({ number: value }), DEBOUNCE_MS);
  numberInput.addEventListener("input", () => {
    numberInput.value = numberInput.value.replace(/\D/g, "").slice(0, 4);
    nameSoon.cancel();
    numberSoon(numberInput.value);
  });

  // The table toggles ARE the table filter — the header carries no second
  // copy. ONE plate at a time: the number box answers "who is 23 on this
  // plate", a question that has no meaning across four numberings, so
  // choosing a table narrows from all four to that one. Pressing the chosen
  // numeral again releases it back to all four.
  const tableButtons = ctx.meta.tables.map((table) => el("button", {
    type: "button",
    title: `${table.plate} — ${table.count} entries`,
    text: table.numeral,
    onclick: () => list.patch({
      tables: list.state.tables.has(table.numeral)
        ? new Set() : new Set([table.numeral]),
    }),
  }));

  const tableHint = el("span", { class: "hint" });

  function paintSearchBar(state) {
    if (document.activeElement !== nameInput) nameInput.value = state.name;
    if (document.activeElement !== numberInput) numberInput.value = state.number;
    tableButtons.forEach((button, i) => {
      const on = state.tables.has(ctx.meta.tables[i].numeral);
      button.classList.toggle("selected", on);
      button.setAttribute("aria-pressed", String(on));
    });
    const chosen = ctx.meta.tables.filter((t) => state.tables.has(t.numeral));
    if (chosen.length === 0) {
      tableHint.textContent = `searching all ${ctx.meta.tables.length} tables`;
    } else if (chosen.length === 1) {
      tableHint.textContent = `searching ${chosen[0].plate} only`;
    } else {
      tableHint.textContent = `searching ${chosen.length} tables`;
    }
  }

  const searchCard = el("form", {
    class: "card search", role: "search", "aria-label": "Search the tables",
    onsubmit: (e) => { e.preventDefault(); nameInput.blur(); numberInput.blur(); },
  },
    el("div", { class: "search-half" },
      el("h2", { text: "Search by name" }),
      el("div", { class: "controls" },
        el("div", { class: "name-field clearable" },
          el("span", { class: "search-icon", "aria-hidden": true }),
          nameInput,
          clearButton(nameInput, "Clear name search",
            () => { nameSoon.cancel(); list.patch({ name: "" }); }))),
      el("p", { class: "note" },
        "Searches every table. Names can be typed with or without special ",
        "characters, and near-misses still match.")),

    el("div", { class: "search-half" },
      el("h2", { text: "Find by table and number" }),
      el("div", { class: "controls" },
        el("div", { class: "table-field" },
          el("span", { class: "control-label", text: "Genealogy table" }),
          el("div", {
            class: "table-buttons", role: "group",
            "aria-label": "Restrict to genealogy tables",
          }, tableButtons)),
        el("div", { class: "number-field" },
          el("label", { class: "control-label", for: "lg-number", text: "#" }),
          el("div", { class: "clearable" }, numberInput,
            clearButton(numberInput, "Clear person number",
              () => { numberSoon.cancel(); list.patch({ number: "" }); })))),
      el("p", { class: "note" },
        "The numbers are Parsons's own, as printed on each plate. Choose a ",
        "table and the number finds that one person on it; press a numeral ",
        "again to release it — ", tableHint, ".")));

  /* -- url --------------------------------------------------------------- */
  const useUrl = options.urlState !== false && typeof history !== "undefined";

  const writeUrl = debounce((self) => {
    if (!useUrl) return;
    const params = stateToParams(self);
    const query = params.toString();
    try {
      history.replaceState(null, "",
        `${location.pathname}${query ? `?${query}` : ""}${location.hash}`);
    } catch { /* file:// in some engines; the page works either way */ }
  }, 260);

  function readUrl() {
    if (!useUrl) return;
    const { state, sorted, open } = paramsToState(
      new URLSearchParams(location.search), ctx.meta);
    Object.assign(list.state, state);
    list.sortTouched = sorted;
    list.open = "";
    list.pendingReveal = open;
    list.syncControls();
    list.patch({});
  }
  const onPop = () => readUrl();
  if (useUrl) addEventListener("popstate", onPop);

  /* -- "/" focuses the search box ---------------------------------------- */
  const onSlash = (event) => {
    if (event.key !== "/" || event.metaKey || event.ctrlKey) return;
    if (isTypingTarget(event.target)) return;
    if (!root.isConnected) return;
    event.preventDefault();
    nameInput.focus();
    nameInput.select();
  };
  addEventListener("keydown", onSlash);

  /* -- assembly ---------------------------------------------------------- */
  if (options.themeToggle !== false) root.append(themeToggle());

  if (options.chrome !== false) {
    root.append(el("header", { class: "intro" },
      el("p", { class: "kicker", text: "A digital edition of Parsons, 1923" }),
      el("h1", { text: "Search the Tables" }),
      el("span", { class: "rule", "aria-hidden": true }),
      el("p", { class: "lede" },
        `Find a person by table and number, or search all ${ctx.meta.tables.length}`,
        " tables by name.")));
  }

  root.append(searchCard);

  root.append(el("section", {
    class: "card people", "aria-labelledby": "lg-people-title",
  },
    el("div", { class: "section-head" },
      el("div", {},
        el("p", { class: "kicker", text: "Browse the complete edition" }),
        el("h2", { id: "lg-people-title", text: "All people" }),
        el("p", { class: "sub" },
          `${ctx.meta.distinct} people, drawn ${ctx.meta.total} times across `,
          `${ctx.meta.tables.length} plates. Someone Parsons draws on more `,
          "than one plate appears here once.",
          // The joins are not all hers, and the page has to say so where the
          // count is, not only inside a row somebody may never open.
          ctx.meta.inferredIdentities
            ? ` ${ctx.meta.inferredIdentities} of those joins are identified `
              + "here rather than printed in the edition, and each says so."
            : "")),
      el("div", { class: "section-actions" }, count,
        el("button", {
          type: "button", class: "link-button", text: "Clear all",
          onclick: () => list.reset(),
        }))),
    list.node));

  root.append(el("footer", { class: "foot" },
    el("p", {}, ctx.meta.title, " · ", el("cite", { text: ctx.meta.source })),
    el("p", { class: "foot-note" },
      "A read-only finding aid. It reproduces the plates and adds nothing to ",
      "them: a year shown as “c.” is calculated from a recorded age and is not ",
      "printed on the plate, and a “†” marks an attribution the plate does not ",
      "make. No census matches and no identifications of living people appear here.")));

  host.replaceChildren(root);

  if (useUrl) readUrl(); else list.patch({});

  return {
    node: root,
    destroy() {
      nameSoon.cancel();
      numberSoon.cancel();
      writeUrl.cancel();
      removeEventListener("keydown", onSlash);
      if (useUrl) removeEventListener("popstate", onPop);
      list.destroy();
      host.replaceChildren();
    },
  };
}

function clearButton(input, label, after) {
  const button = el("button", {
    type: "button", class: "clear-x", "aria-label": label, text: "×",
  });
  button.addEventListener("click", () => {
    input.value = "";
    input.focus();
    after();
  });
  return button;
}

/**
 * Light/dark toggle with no Auto state, matching the edition's own control:
 * an untouched page follows the OS, and once pressed the button always names
 * a real palette.
 *
 * The stored choice is applied by a blocking script in the page head, before
 * first paint; this only keeps the button honest afterwards.
 */
function themeToggle() {
  const root = document.documentElement;
  let stored = null;
  try { stored = localStorage.getItem("laguna-theme"); } catch { /* blocked */ }
  if (stored) root.dataset.theme = stored;

  const isDark = () => (root.dataset.theme
    ? root.dataset.theme === "dark"
    : matchMedia("(prefers-color-scheme: dark)").matches);

  const button = el("button", { type: "button", class: "theme" });
  const paint = () => {
    button.textContent = isDark() ? "Light" : "Dark";
    button.setAttribute("aria-label", `Switch to ${isDark() ? "light" : "dark"} theme`);
  };
  button.addEventListener("click", () => {
    root.dataset.theme = isDark() ? "light" : "dark";
    try { localStorage.setItem("laguna-theme", root.dataset.theme); } catch { /* blocked */ }
    paint();
  });
  paint();
  return el("div", { class: "theme-bar" }, button);
}

/* --------------------------------------------------------- custom element -- */

/**
 * <laguna-search src="search-index.json"></laguna-search>
 *
 * The drop-in form: one tag, no bundler, no import map. Registered only in a
 * browser, so this file stays importable under node for build.py's gate.
 */
if (typeof customElements !== "undefined" && !customElements.get("laguna-search")) {
  customElements.define("laguna-search", class extends HTMLElement {
    async connectedCallback() {
      if (this.mounted) return;
      this.mounted = true;
      const inline = this.querySelector('script[type="application/json"]');
      const data = inline
        ? JSON.parse(inline.textContent)
        : await (await fetch(this.getAttribute("src"))).json();
      this.controller = mountSearch(this, {
        data,
        target: this.getAttribute("target") || "_blank",
        chrome: this.getAttribute("chrome") !== "false",
        themeToggle: this.getAttribute("theme-toggle") !== "false",
        urlState: this.getAttribute("url-state") !== "false",
      });
    }

    disconnectedCallback() {
      this.controller?.destroy();
      this.mounted = false;
    }
  });
}
