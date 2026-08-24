# Environment notes

Not auto-loaded under the current project configuration. Read this before
working from a remote/web session, cropping plate images, or making a
branch/PR cleanup decision.

## Local (Mac)

macOS, Python 3.11. openpyxl 3.1.5, fontTools 4.63.0 + brotli. `gh` 2.96.0 at
`~/.local/bin/gh`, authenticated as `prettyph3nom`, owner of the
`PuebloGenealogy` org. **No Homebrew, no ImageMagick, no PIL — use `sips`.**

**`sips -c H W --cropOffset 0 0` centre-crops instead of cropping at the
origin.** It does not error — it silently returns a tile from the middle of
the image. Use `1 1`. (Found tiling Genealogy III: a 2450px-down region
instead of the intended one.)

The repo lives under Google Drive, whose sync daemon can touch `.git`
mid-write; if git reports object corruption, that's the likely cause.

**Verify checkout identity before comparing repositories or checkouts** —
run `git log --oneline -1` (and check the remote/branch) rather than
assuming a path is the active repo. A broad `find ~` can match an archived
backup (e.g. `_backup-v1-laguna-genealogy-tables-2026-07-27/`, see below)
before it reaches the active repo, so verify the returned path is the one
you meant.

## Remote / web sessions

**A remote session is a different machine, and two of its limits change what
`/publish` can do. Neither is a fault to debug — both are egress policy; the
proxy's own README says to report a 403 rather than route around it. This is a
standing property of the environment, not transient — don't burn a turn
re-testing it hopefully.**

- **There may be no route to the published site.** `pueblogenealogy.github.io:443`
  answers 403 to CONNECT, so `curl` returns `000` and `build.py --refresh` dies
  in `urllib`. That takes out `/publish` gate 6 entirely (the 200 sweep, the
  sitemap count, the page-by-page SHA-256 comparison) and the post-publish
  `--refresh` with it. **A green "pages build and deployment" run is not a
  substitute** — this repo verifies by hash because the Pages API misreports
  the deployed commit. Push, then record both checks as owed by name; don't
  write "verified" from a remote session. If `curl` gives `000`, check
  `$HTTPS_PROXY/__agentproxy/status` for a fresh `connect_rejected` before
  concluding anything — `curl` hides the body of a failed CONNECT, and `000`
  alone can't distinguish a policy denial from an outage. Check the status
  endpoint's timestamp against `date -u`, or you may be reading a *previous*
  session's failure. Remedy: run the two checks from the Mac, or widen the
  environment's egress policy (set at environment creation; documented at
  `https://code.claude.com/docs/en/claude-code-on-the-web`).
- **A delete-push is refused** — `git push origin --delete <branch>` returns
  HTTP 403 in both repos while ordinary pushes go through. There's no API
  route around it (the GitHub MCP tools have `create_branch`, no delete).
  Delete the local ref, say so, and leave the remote ref for a machine that
  can reach it.
- **What a remote session gains**: Pillow and a real headless Chromium
  (`/opt/pw-browsers`), so a plate can be cropped without `sips` and
  `/search/` can be measured at an actual 375px viewport — the desktop
  preview pane instead widens to content. Install: `PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1
  pip3 install playwright` (the flag matters, or it re-fetches an already-present
  browser); launch with `executable_path="/opt/pw-browsers/chromium"` (a symlink
  to the binary, not a directory). Serve `docs/` with `python3 -m http.server`
  rather than the preview pane — same pages, no cache.
- **A remote/Cowork device-bridge write tool may refuse a direct write under
  `.claude/`** ("Writing to `.claude` is not permitted via remote tools").
  This is a limitation of that specific write path, not a rule about the file
  or the project — don't assume the target is unwritable in the real repo.
  Use a verified workaround (e.g. shell redirection through a remote-bash
  tool) or a local write path instead.
- **`/publish`'s remote scope, under current tooling**: gates 1–5 work
  remotely. Gate 6 (live verification) and a standalone `--refresh` do not —
  see the no-route-to-the-published-site note above. `laguna-search` can be
  attached via `add_repo` when gate 8 (re-vendoring) needs it.

## Plate cropping

**Chunk rather than magnify** — anything taller than ~1500px downscales on
display and becomes illegible; plan tiles from an ink-row profile, one
generation band at a time (count dark pixels per row inside the band's x
range, group runs of ≥6 into text lines, pack lines into tiles ≤420 native px
tall). A reconciling tile-line count against the known entry count licenses
trusting the rest.

**Table 3's generation columns**, native x of the right-aligned number: g1 145
· g2 755 · g3 1293 · g4 1833 · g5 2377 · g6 2920 · g7 3467. Band x from
`col − 60`; a full line runs about 370px. Block 1 crops as three chunks × two
strips with 830px overlap: `crop.py /tmp/t3.bmp {0,1470} {150,1590,3030} 2300
{1480,1480,1450}`; block 2 at y 4440, h 1080. A column-6 strip carrying the
mother's column beside it (`crop.py /tmp/t3.bmp 2250 <y> 1150 1450` at
y = 150, 1550, 2950, and h=1100 at 4400) is what settles the six groups the
fold crease hides. Table 4 is 12255 × 8409 — crop at native and chunk hard.

**Remotely there is no `sips`, and the replacement is better for type**:
`pip3 install pillow`, crop straight from the JPEG with `Image.crop().resize(...,
Image.NEAREST)`, which invents nothing exactly as `crop.py` does not.

## Git / branch / PR mechanics

**PRs here are squash-merged, so `git branch --no-merged` does NOT tell you
whether a branch holds unmerged work.** A squash puts the branch's content on
`main` as a new single-parent commit; the branch's own commit is never an
ancestor, so ancestry-based checks report already-merged work as unmerged.
Read the PR state instead: `gh pr list --state all --head <branch>`, and
compare `git rev-parse <head>^{tree}` against the merge commit's tree for
proof if needed.

**The same mechanic has a dangerous second face: a stale open PR can become a
REVERT.** Branch new work off a branch that hasn't merged yet, squash-merge
the new work, and the old PR's content lands on `main` *inside* that squash —
leaving the old PR open, contributing nothing, and now proposing to undo
everything committed after it. `gh pr list --state open` surfaces this; run it
when wrapping a session, not only when tidying branches. The check that
settles it is `git diff origin/main origin/<branch>` — read the **direction**:
deletions there mean the branch is *behind* `main`, not ahead.

**A branch doesn't have to be built on to acquire this risk — a PARKED one
acquires it fastest**, because every session that records anything on `main`
(`CHANGELOG.md`, `SESSION-NOTES.md`) widens the gap even with nothing branched
off it. A branch's direction is a fact with a timestamp, not a fixed property —
re-measure at the moment of merging, never trust a reading taken when it was
parked. If a fix needs testing later, don't park the branch: leave the
**commit** reachable by SHA and cherry-pick it onto a fresh branch off current
`main` when it's actually wanted, so it gets tested against everything since.

Two more mechanics from the same family: GitHub **auto-deletes a branch on
merge**, so remote-tracking refs go stale in bulk — run `git fetch --prune`
before any cleanup. And a batch `git push origin --delete a b c` **fails
whole** if any one ref is already gone — nothing is deleted, and the refs that
do exist are left untouched (this reads like a permissions problem and isn't
one).

`_backup-v1-laguna-genealogy-tables-2026-07-27/`, one level up, is the **sole
surviving copy** of the deleted v1 repo. Do not clean it up as stale.
