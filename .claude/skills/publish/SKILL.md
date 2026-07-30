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

This is **one fewer than the page count `--public` reports** — 4 against 5
today. That is correct, not a discrepancy: the build counts every `.html` in
`docs/`, and `404.html` is deliberately absent from the sitemap. The number to
expect is **the landing page plus one per transcribed plate**. If it ever equals
the build's count, the 404 page has leaked into the sitemap.

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
`main` deploys the site and stops there. Cutting a **GitHub release** is a
separate act with an irreversible side effect: Zenodo's webhook is on this repo,
so a release mints a new version doi and a new archived deposit, and **published
Zenodo records cannot be deleted**.

**There is a standing release policy — read it in `CLAUDE.md` before tagging
anything.** In short: during active development, commit to `main` and cut **no
GitHub Releases and no Zenodo deposits**. The next release comes only when all
four genealogy tables, the design, the transcriptions, the text and the
citations are final.

Two consequences that will look like problems and are not:

- **The archive lags the site deliberately.** The concept doi resolves to
  v1.0.0, which holds Genealogies I and IV only. Do not tag to close that gap.
- **`CITATION.cff` names the newest release that exists**, not the state of
  `main`. Its abstract describing more plates than the release contains is
  correct — abstract describes the work, version fields describe the release.

When the release finally *is* wanted, `.zenodo.json` must already be on `main`
and current for all four tables — Zenodo reads it from the tagged commit, not
from `main`'s tip — and the concept doi in `make_chart.py` never changes.

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
