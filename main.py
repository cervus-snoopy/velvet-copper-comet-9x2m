import os

LINE = "My cat fired me as her butler this morning \u2014 I served breakfast four minutes late, and she's already interviewing the Roomba."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
os.chmod(path, 0o644)
os.chmod(out_dir, 0o755)

with open(path, "r", encoding="utf-8", newline="") as f:
    written = f.read()
assert written == LINE, "entry.txt does not match the joke line"
assert 1 <= len(written) <= 199, "entry.txt must be 1-199 characters"
