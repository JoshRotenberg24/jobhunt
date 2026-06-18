#!/bin/bash
# SessionStart hook: install the resume/cover-letter renderer dependencies
# (python-docx, reportlab, pymupdf) so the tailor-resume skill's render steps
# work in a fresh Claude Code on the web session. Idempotent; non-interactive.
set -euo pipefail

# Only needed in the remote (web) container; local users manage their own env.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

REQ="${CLAUDE_PROJECT_DIR:-.}/build/requirements.txt"
if [ -f "$REQ" ]; then
  python3 -m pip install --quiet --disable-pip-version-check -r "$REQ"
fi
