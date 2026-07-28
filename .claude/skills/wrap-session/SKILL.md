---
name: wrap-session
description: Close out a working session so the next one starts cheap — backfill CHANGELOG.md, rewrite SESSION-NOTES.md as a handoff, and leave the repo in a state a cold start can trust. Use when the user says they are done for now, wants to wrap up, stop, pick this up tomorrow, or start fresh in a new chat.
---

# Wrap up a session

The next session begins with no memory of this one. Everything it would
otherwise re-derive — or worse, silently redo — has to be written down now.

Two failure modes this exists to prevent:

- **A decision gets re-litigated.** Work was done, measured, and reverted for a
  reason. If the reason is not recorded, the next session proposes it again.
- **A half-finished thread looks finished.** Unreferenced code, a deliberate
  omission, or a known-broken thing reads as a bug to a cold start.

Do not write this from memory of the conversation alone. Check the repo.

## 1 — Establish the actual state

```bash
git status --porcelain          # uncommitted work?
gh pr list --state open         # anything in flight?
git log --oneline --since=midnight
```

Then confirm the build matches what is committed:

```bash
python3 scripts/make_chart.py --public
git status --porcelain docs/
```

**A rebuild on a later day dirties `docs/` with dates alone** — `dateModified`,
the "Last updated" line, `sitemap.xml` `lastmod`. If the diff is dates and
nothing else, `git checkout -- docs/` and move on. Committing it would signal a
content change to crawlers that did not happen.

Anything left uncommitted or unmerged is reported to the user, not quietly
finished.

## 2 — Backfill `CHANGELOG.md`

Newest entry first, dated. Write what changed **in the edition**, not which
files moved. The test for whether an entry is worth keeping: *would the next
session otherwise have to re-derive this?*

Always record:

- work that was **built and then reverted**, with the measurement or reason —
  this is the highest-value content in the file, and the easiest to lose;
- anything that now has a **side effect** someone could trigger unawares;
- constraints discovered the hard way.

`/publish` gate 7 also writes here. If this session published, the entry may
already exist — extend it rather than adding a second one for the same day.

## 3 — Rewrite `SESSION-NOTES.md`

**Overwrite it. It is a rolling handoff, not a history.** If it starts
accumulating dated sections it has become a second changelog and lost its
purpose. Keep these sections:

- **Start here in a new chat** — the read order, and how to bring the preview up
- **State** — one paragraph: is anything broken or half-finished?
- **The open thread** — the single most likely next piece of work, with the
  constraints that would otherwise surface late
- **Other things that could be picked up** — a table with effort and blockers
- **Decisions already made — don't re-litigate**

Be honest in *State*. "Nothing is half-finished" is only worth writing if it is
true, and a cold start will trust it.

## 4 — Check the durable docs still tell the truth

Skim `CLAUDE.md` for claims this session falsified. It is read on every cold
start, so a stale line there is more expensive than a stale line anywhere else.
Common drift: the **Outstanding** list, counts, and anything phrased as "not yet
done" that now is.

If a new invariant emerged — a rule that looks like a preference but is not —
it belongs in `CLAUDE.md`, not only in the changelog.

## 5 — Commit

Branch, commit, PR. Do not push docs changes to `main` directly.

```
Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

Then tell the user, in the chat, which files to open next session and what the
open thread is. The files are the durable copy; the message is so they can act
without reading them.
