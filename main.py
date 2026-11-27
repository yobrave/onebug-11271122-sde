from pathlib import Path
import json
import os
import shutil
import time

here = Path(__file__).resolve().parent
dest = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
dest.mkdir(parents=True, exist_ok=True)
line = (here / "entry.txt").read_text(encoding="utf-8").strip()
shutil.copyfile(here / "entry.txt", dest / "entry.txt")
# pipeline gate reads the stamp line from stdout
print(json.dumps({"chars": len(line), "stamp": "sde:%08x" % (time.time_ns() & 0xFFFFFFFF)}))
