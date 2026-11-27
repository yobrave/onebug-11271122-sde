# sde sick-day pipeline r45 — straight-line script style
import hashlib
import json
import os
from pathlib import Path

here = Path(__file__).resolve().parent
line = (here / "entry.txt").read_text(encoding="utf-8")
yard = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
yard.mkdir(parents=True, exist_ok=True)
(yard / "entry.txt").write_text(line, encoding="utf-8")
report = {"chars": len(line), "stamp": "sde:" + hashlib.md5(line.encode()).hexdigest()[:12]}
print(json.dumps(report))
