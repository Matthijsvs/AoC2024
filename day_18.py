from dataclasses import dataclass
import heapq
import time

from PIL import Image

from get_src import *


@dataclass
class PointA:
    x: int
    y: int
    last_dir: int = 0
    dir_cnt: int = 0  # number of turns
    cost: int = 1e9

    def val(self):
        return self.cost  # + (self.dir_cnt * 1000)

    prev: any = None

    def __lt__(self, other):
        return self.val() < other.val()

    def __repr__(self):
        d = ["^", ">", "v", "<"]
        return f"({self.x},{self.y},{self.cost})"

    def __hash__(self):
        return self.x * 10000 + self.y


sample = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""
size = 71

lst = []
inp = get()
for i in inp.splitlines():
    x, y = i.split(",")
    lst.append(PointA(int(x), int(y)))

grid = []
for i in range(size):
    grid.append(["."] * size)


def inside(x, y, grid):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


for i in lst[:1024]:
    grid[i.y][i.x] = "#"

with Image.new("RGBA", (size, size), (255, 255, 255, 255)) as im:
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == ".":
                im.putpixel((x, y), (255, 255, 255, 255))
            else:
                im.putpixel((x, y), (0, 0, 64, 255))
    im.save(f"day18.png")

todo_list = []
costlist = {}

start = PointA(0, 0, 1, 0, 0)
end = PointA(size - 1, size - 1)

heapq.heappush(todo_list, start)


def get_next(p: PointA):
    res = []
    for move in range(len(dirs4)):
        x = p.x + dirs4[move][0]
        y = p.y + dirs4[move][1]
        if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
            if grid[y][x] == ".":
                q = PointA(x, y, move, p.dir_cnt, p.cost + 1, p)
                res.append(q)
    print(res)
    return res


qq = ["^", ">", "v", "<"]
while todo_list:
    point = heapq.heappop(todo_list)
    costlist[hash(point)] = point
    for neighbour in get_next(point):
        if (hash(neighbour) not in costlist) or (neighbour.cost < costlist[hash(neighbour)].cost):
            heapq.heappush(todo_list, neighbour)
    if hash(end) in costlist:
        print(costlist[hash(end)])

optimal_route = costlist[hash(end)]
print(optimal_route.cost)
