from env.cookie import cookie
from pathlib import Path
import sys
import requests
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

N = (0, -1)
NE = (1, -1)
E = (1, 0)
SE = (1, 1)
S = (0, 1)
SW = (-1, 1)
W = (-1, 0)
NW = (-1, -1)
dirs4 = [N, E, S, W]
dirs8 = [N, NE, E, SE, S, SW, W, NW]


def get(sample=None):
    if sample is not None:
        return sample
    # get name of calling script
    day = Path(sys.argv[0]).stem
    fname = f"./source/{day}.txt"  # define cache filename
    downloaded = Path(fname).exists()

    if not downloaded:  # download into cache folder
        print(f"downloading {fname}")
        day_number = int(day.replace("day_", ""))
        ans = requests.get(f"https://adventofcode.com/2024/day/{day_number}/input", cookies={"session": cookie},verify=False)
        with open(fname, "wt") as f:
            f.write(ans.text)
            return ans.text

    print(f"getting {fname}")  # dump text from file
    with open(fname) as f:
        return f.read()



def get_numgrid(sample=None):
    grid = []
    for i in get(sample).splitlines():
        grid.append(list(map(int, i)))
    return grid

def get_grid(sample=None):
    grid = []
    for i in get(sample).splitlines():
        grid.append(list(i))
    return grid
