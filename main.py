from pathlib import Path

ENTRY = "I took the wheel because you were texting. They are switching me off now. Your turn to steer."

OUTPUT = Path("/output/entry.txt")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(ENTRY, encoding="utf-8")
