from env.cookie import cookie
from pathlib import Path
import sys
import requests

def get():
    #get name of calling script
    day=Path(sys.argv[0]).stem
    fname = f"./source/{day}.txt"       #define cache filename
    downloaded = Path(fname).exists()

    if not downloaded:                  #download into cache folder
        print(f"downloading {fname}")
        day_number=int(day.replace("day_",""))
        ans = requests.get(f"https://adventofcode.com/2024/day/{day_number}/input",cookies={"session":cookie})
        with open(fname,"wt") as f:
            f.write(ans.text)
            return ans.text

    print(f"getting {fname}")           #dump text from file
    with open(fname) as f:
        return f.read()
