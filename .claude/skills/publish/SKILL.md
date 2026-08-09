---
name: publish
description: Build and publish the edition to https://pueblogenealogy.github.io/. Use when the user wants to publish, deploy, release, push the site live, or update the public edition after making changes. Runs as ordered gates — a failed gate stops the release rather than shipping a partial or leaking one.
---

# Publish the edition

A release is a sequence of gates. **Each must pass before the next runs.** If one
fails, stop and report it — do not work around it, and do not publish "most of"
a release.

The thing this procedure exists to prevent: research data about living people
reaching a public repository. Git history is permanent, and any clone or fork
made in the meantime keeps whatever was committed. A leak cannot be undone by a
later commit.

## Gate 1 — the data is structurally sound

**Run one per transcribed plate.** Do not copy this list from memory — derive it,
so a new plate cannot be skipped the way Table 2 was between 2026-07-30 and the
fix below:

```bash
for f in scripts/transcription*.py; do printf '%-28s ' "$f"; python3 "$f" | tail -1; done
```

Every line must end `all structural checks pass`. There are **three** modules
today — `transcription.py` (Table 1), `transcription_ii.py` (Table 2) and
`transcription_iv.py` (Table 4) — and the loop picks up Table 3's the day it
exists.

These verify matrilineal clan descent across every union, which is what catches
a misread bracket. A failure here means a reading is wrong — fix the
transcription, not the check. Note what they **cannot** see: whether a person is
attached to the right parents, or drawn in the right column. Passing here is not
evidence the reading is correct, only that it is self-consistent.

## Gate 2 — build

```bash
python3 scripts/make_chart.py --public
```

Must report, for every table, `no english/census chips in output`. The build
greps its own output and deletes the file rather than write a leak, so a missing
page means the guard fired. Investigate before doing anything else.

Confirm the final line lists `og-cover.jpg` — if it warns the asset is missing,
social cards will be blank.

The build must also end with `N JSON-LD blocks valid` and **exit 0**. If it
prints `STRUCTURED DATA INVALID` it exits 1: a Dataset somewhere is missing a
required field. Nothing looks different on the page — the cost is silent loss of
rich results — so fix it rather than shipping past it. Note that a nested
Dataset (the landing page's `hasPart` entries) is validated as a Dataset in its
own right, not as a pointer, so it needs its own `name`, `description` and
`url`.

## Gate 3 — privacy

```bash
git add -A
git diff --cached --name-only | grep -Ei '\.xlsx|\.csv|^build/|^data/'
```

**This must return nothing.** If it matches anything at all, stop: unstage it,
confirm `.gitignore` covers it, and only then continue. Do not use `git add -f`
here for any reason.

Also delete stray `.DS_Store` files first — Google Drive and Finder create them
constantly:

```bash
find . -name '.DS_Store' -delete
```

## Gate 4 — review what is actually shipping

```bash
git status --short
git diff --cached --stat
```

Expect changes in `docs/` whenever `scripts/` changed — `docs/` is generated, so
the two move together. `docs/` changing *without* a `scripts/` change means
someone hand-edited generated files; that edit is about to be lost on the next
build, so find out what happened before committing.

## Gate 5 — commit and push

Write a message that says what changed in the edition, not what files moved.
End it with:

```
Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

```bash
git push origin main
```

## Gate 6 — verify live

Pages takes roughly 30–90 seconds. Poll rather than assuming:

**Derive the page list from what was actually built**, for the same reason as
Gate 1 — a hardcoded list silently stops covering the newest plate, which is
exactly how `/genealogy-ii/` went unverified after Table 2 shipped:

```bash
{ printf '/\n/sitemap.xml\n/robots.txt\n/404.html\n'
  (cd docs && ls -d */ 2>/dev/null | sed 's|^|/|'); } | while read -r u; do
  printf "%-18s %s\n" "$u" "$(curl -s -o /dev/null -w '%{http_code}' "https://pueblogenealogy.github.io$u")"
done
```

All must return `200` (404.html returns 200 when fetched directly — that is
correct; it is served with a 404 status only for unmatched paths). `docs/fonts/`
will appear in the list and 404s harmlessly — it is a directory of assets, not a
page; every `genealogy-*` entry must be 200.

Cross-check the sitemap:

```bash
curl -s https://pueblogenealogy.github.io/sitemap.xml | grep -c '<loc>'
```

This is **two fewer than the page count `--public` reports** — 5 against 7
today. That is correct, not a discrepancy: the build counts every `.html` in
`docs/`, and two of them are deliberately absent from the sitemap — `404.html`,
and `search/index.html`, which ships `<meta name="robots" content="noindex">`
and must not be advertised in a sitemap that contradicts it. The number to
expect is **the landing page plus one per transcribed plate**. If it ever equals
the build's count, the 404 page or the search page has leaked into the sitemap.

It was *one* fewer until 2026-08-09, when the search page shipped. Recompute
this sentence when a page is added that is not a plate; the count is not
derived, and a stale number here reads as a failed publish.

**Verify the deploy by hash, not by the Pages API** — it misreports the deployed
commit, which cost a session in 2026-07-30:

```bash
(cd docs && find . -name '*.html' | sed 's|^\./||') | while read -r p; do
  live=$(curl -s "https://pueblogenealogy.github.io/$p" | shasum -a 256 | cut -d' ' -f1)
  local=$(shasum -a 256 "docs/$p" | cut -d' ' -f1)
  [ "$live" = "$local" ] && echo "OK   $p" || echo "DIFF $p"
done
```

Every line must read `OK`. A `DIFF` means Pages is still serving the previous
build — wait and re-run rather than rebuilding.

Then confirm the deployed HTML carries the right identity:

```bash
curl -s https://pueblogenealogy.github.io/ | grep -c 'prettyph3nom\|laguna-genealogy-tables'
```

Must be `0`. A non-zero count means a stale build reached production.

## Gate 7 — record it

Add an entry to `CHANGELOG.md`: the date, what changed, and anything a future
session would otherwise have to re-derive. This is what makes the next session
cheap.

Then refresh `SESSION-NOTES.md` if the open thread moved. It is a rolling
handoff, not a history — overwrite it rather than appending.

**Publishing is not releasing, and this procedure never releases.** Pushing to
`main` deploys the site and stops there.

**No release is to be cut, and no archive is advertised.** As of 2026-08-08 the
user has withdrawn the Zenodo deposit from the edition's public face and asked
for low exposure: `.zenodo.json` is deleted, the doi is gone from
`make_chart.py`, `CITATION.cff` and the README, and the deposit webhook is
being removed. Read `CLAUDE.md` → *Exposure posture* before doing anything that
would reverse this.

What that means for this procedure:

- **Do not tag, and do not offer to.** The old policy said "release when all
  four tables are final"; all four *are* final, so a session reading only that
  sentence would conclude the release is due. It is not.
- **The v1.0.0 deposit at Zenodo was deleted** by its owner on 2026-08-08,
  inside Zenodo's 30-day owner-deletion window. Both dois now return 410 Gone at
  a tombstone. Nothing in the repo points at it; this is not a loose end.
- **If a doi reappears** in `make_chart.py`, `CITATION.cff` or the README, that
  is a regression, not a restoration.

## Gate 8 — the search index, if the register moved

`docs/search/` is built from `vendor/search/`, which is another project's output
built by **fetching these pages and parsing them** (`vendor/search/SOURCE.md`).
So the index goes stale the moment this build changes the register's markup —
and nothing here can detect that, because a stale index is still valid JSON and
still renders a perfectly working page.

Skip this gate when the publish changed only prose, styling or the chart. Run it
when a `.reg` entry, a `.reg-rel`, a `.num`, an `.xref` or a `sic-ring` changed
shape, and **always** when a plate's data changed.

In the `laguna-search` checkout:

```bash
python3 build.py --refresh
```

**`--refresh` is not optional here.** Without it that build re-parses its own
`cache/`, which still holds this site *as it was before the push*, so every one
of its gates passes against the old pages and reports success. The only tell is
one word in its first line — `re-fetched` against `cached in cache/`.

Expect its namesake gate to fail if a name changed: that is the gate working,
and the pair needs a hand-written verdict before it will build. Then re-vendor
the three files, update the commit hash and date in `vendor/search/SOURCE.md`,
rebuild here, and publish again — the search page is part of this site now, so
it goes through the same gates as everything else.

## If Pages serves the wrong thing

Symptom: `/` returns 200 but every subpath 404s, and the title looks like the
README. Cause: Pages is building from the repo root instead of `/docs`.

```bash
gh api -X PUT repos/PuebloGenealogy/pueblogenealogy.github.io/pages \
  -f 'source[branch]=main' -f 'source[path]=/docs'
gh api -X POST repos/PuebloGenealogy/pueblogenealogy.github.io/pages/builds
```

Changing the source does not itself trigger a rebuild — the explicit `builds`
POST is what does.
