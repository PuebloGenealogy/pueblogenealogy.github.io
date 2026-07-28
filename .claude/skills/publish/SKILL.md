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

```bash
python3 scripts/transcription.py
python3 scripts/transcription_iv.py
```

Both must print `all structural checks pass`. These verify matrilineal clan
descent across every union, which is what catches a misread bracket. A failure
here means a reading is wrong — fix the transcription, not the check.

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

```bash
for u in / /genealogy-i/ /genealogy-iv/ /sitemap.xml /robots.txt /404.html; do
  printf "%-16s %s\n" "$u" "$(curl -s -o /dev/null -w '%{http_code}' https://pueblogenealogy.github.io$u)"
done
```

All must return `200` (404.html returns 200 when fetched directly — that is
correct; it is served with a 404 status only for unmatched paths).

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

**Publishing is not releasing.** Pushing to `main` deploys the site and stops
there. Cutting a **GitHub release** is a separate act with a side effect:
Zenodo's webhook is on this repo, so a release mints a new version doi and a new
archived deposit. Do not tag one casually to mark a checkpoint. When a release
*is* wanted, `.zenodo.json` must already be on `main` — Zenodo reads it from the
tagged commit — and the concept doi in `make_chart.py` never changes.

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
