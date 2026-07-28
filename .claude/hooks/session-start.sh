#!/usr/bin/env bash
# SessionStart hook — put the last session's handoff in front of the model
# before it does anything, and say so loudly when that handoff is stale.
#
# A hook is a shell command, not a prompt: it cannot WRITE the handoff. That
# still needs /wrap-session and a model. What it can do is guarantee the
# handoff is READ, which is the half that was depending on someone remembering
# to link the file.
#
# Fails open. Any problem here exits 0 with no output, so a session can never
# be blocked by the handoff machinery.
set -uo pipefail

root="$(git rev-parse --show-toplevel 2>/dev/null)" || exit 0
notes="$root/SESSION-NOTES.md"
[ -f "$notes" ] || exit 0

# Stale? Source commits landing after the notes were last committed mean the
# notes describe an older state of the repo.
stale=""
notes_commit="$(git -C "$root" log -1 --format=%H -- SESSION-NOTES.md 2>/dev/null)"
if [ -n "$notes_commit" ]; then
  n="$(git -C "$root" rev-list --count "$notes_commit"..HEAD -- scripts/ docs/ 2>/dev/null || echo 0)"
  if [ "${n:-0}" -gt 0 ]; then
    stale="STALE: ${n} commit(s) have touched scripts/ or docs/ since SESSION-NOTES.md was last updated. Verify against git before trusting anything below."
  fi
fi

# Someone stopped mid-change.
dirty=""
if [ -n "$(git -C "$root" status --porcelain 2>/dev/null)" ]; then
  dirty="UNCOMMITTED WORK: the tree is not clean. Report what is outstanding before starting something new."
fi

python3 - "$notes" "$stale" "$dirty" <<'PY'
import json, sys
notes = open(sys.argv[1], encoding="utf-8").read()
warnings = [w for w in sys.argv[2:] if w]
parts = ["Handoff from the previous session (SESSION-NOTES.md). "
         "Read this before acting; it names the open thread and the decisions "
         "that were already settled."]
if warnings:
    parts.append("\n".join(warnings))
parts.append(notes)
print(json.dumps({"hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "\n\n".join(parts),
}}))
PY
