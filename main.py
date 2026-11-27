"""r44 sde entry packer: sick-day excuse line, cap 200, env-driven output."""

import json
import os
from pathlib import Path

SLUG = "u-zeroxfive-the-funniest-sick-day-excuse-37423a36"
MAX_CHARS = 200


def pack():
    problems = []
    line = (Path(__file__).resolve().parent / "entry.txt").read_text(encoding="utf-8").strip()
    if not line:
        problems.append("blank_entry")
    if len(line) > MAX_CHARS:
        problems.append("entry_too_long")
    copied_to = None
    if not problems:
        copied_to = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
        copied_to.mkdir(parents=True, exist_ok=True)
        (copied_to / "entry.txt").write_text(line + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"problems": problems, "copied_to": str(copied_to), "size": len(line), "slug": SLUG}))
    if problems:
        raise SystemExit(2)


pack()

STAMP = "r44-sde"
print(json.dumps({"stamp": STAMP, "final": True}))
