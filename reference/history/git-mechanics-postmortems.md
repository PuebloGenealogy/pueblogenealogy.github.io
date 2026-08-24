# Git/branch/PR mechanics — worked examples

Not auto-loaded. The durable rules these produced are stated tersely in
`reference/environment-notes.md`'s "Git / branch / PR mechanics" section; this
file is the calibrating examples — the near-misses and false alarms that make
each rule recognizable next time rather than abstract advice.

## A squash-merged PR can look unmerged and not be (found 2026-08-07)

Sweeping stale branches, `handoff-2026-07-29-plate-chrome` looked unmerged
under `git branch --no-merged` — but it's PR #13, squashed onto `main` as
`5a37bdf`, tree `39b8487`, **identical** to the branch head `df2b1e0`, empty
diff. Nothing was ever at risk; this is the zero-risk case that calibrates
what "looks unmerged" is worth trusting. `git rev-parse <head>^{tree}` against
the merge commit's tree is the proof, if one is needed.

## A stale open PR became a silent revert-in-waiting (found 2026-08-08)

PR #33 held the previous session's handoff branch. PR #34 was branched from
it. After #34 and #35 merged, #33 — still open, still showing as pure
addition against the `main` it was branched from — would have **deleted all
five U+02BD readings and reverted the font subset** had it ever been merged.
It was closed, not merged. `gh pr list --state open` is what surfaces this;
run it when wrapping a session, not only when tidying branches. The check
that settles it is `git diff origin/main origin/<branch>`, read for
**direction**: deletions there mean the branch is *behind* `main`, not ahead.

## A parked branch acquires revert-risk fastest of all (found 2026-08-09–10)

PR #43 was deliberately left open as the build to test a Safari scroll fix
on. It was purely additive against `main` when parked, and stopped being so
within the hour — not because anything was branched off it, but because
`main` moved on `CHANGELOG.md` and `SESSION-NOTES.md` while the branch stood
still. Every session that records anything on `main` widens the gap, even
with nothing branched off the parked branch itself. The records are the files
that drift first, which is also why the drift is easy to wave through — it
reads as handoff churn, not a revert.

**One further day turned records-only drift into a genuine revert**: closed
unmerged on 2026-08-10 at **152 insertions against 262 deletions** in
`scripts/` and `docs/` alone, because `main` had gained Genealogy IV's
corrected parentage and the row-box fix while the branch stood still. Nobody
had built on it — parking was the whole cause. A parked branch has a shelf
life measured in days; the cost of keeping one is that its diff must be
re-read every time it's considered. Nothing was lost closing it: the
reasoning behind the Safari attempts had already been carried onto `main`
during the previous wrap. The right shape when a fix needs testing later is
to leave the **commit** reachable by SHA and cherry-pick it onto a fresh
branch off current `main` at the moment it's actually wanted — which also
means it gets tested against everything since, rather than a stale base.
