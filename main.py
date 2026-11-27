"""sde sick-day excuse porter - u-zeroxfive-the-funniest-sick-day-excuse-37423a36."""
import json
import os
from pathlib import Path

CEILING_SDE = 200
PORCH = Path(__file__).resolve().parent


class Porter:
    def __init__(self):
        self.line = None
        self.issue = None

    def take(self):
        self.line = (PORCH / "entry.txt").read_text(encoding="utf-8").strip()

    def inspect(self):
        if not self.line:
            self.issue = "blank excuse"
        elif len(self.line) > CEILING_SDE:
            self.issue = "%d chars, ceiling %d" % (len(self.line), CEILING_SDE)

    def drop(self):
        yard = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
        yard.mkdir(parents=True, exist_ok=True)
        target = yard / "entry.txt"
        target.write_text(self.line + "\n", encoding="utf-8", newline="\n")
        return target


def main():
    p = Porter()
    p.take()
    p.inspect()
    if p.issue:
        print(json.dumps({"ok": False, "issue": p.issue}))
        return 1
    target = p.drop()
    print(json.dumps({"ok": True, "chars": len(p.line), "target": str(target),
                      "bounty": "u-zeroxfive-the-funniest-sick-day-excuse-37423a36",
                      "kind": "sick-day excuse", "round": "1127-1122"}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
