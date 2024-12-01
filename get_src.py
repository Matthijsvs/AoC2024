from pathlib import Path
import sys

def get():
    day=Path(sys.argv[0]).stem
    fname = f"./source/{day}.txt"
    print(f"getting {fname}")
    with open(fname) as f:
        return f.read()
