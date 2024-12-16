import heapq
from dataclasses import dataclass

from PIL import Image

from get_src import *
grid = get_grid()

w = len(grid[0]) - 1  # highest width
h = len(grid) - 1


@dataclass
class PointA:
    x: int
    y: int
    last_dir: int = 0
    dir_cnt: int = 0  # number of turns
    cost: int = 1e9

    def val(self):
        return self.cost+(self.dir_cnt*1000)
    prev: any=None
    def __lt__(self, other):
        return self.val() < other.val()
    def __repr__(self):
        d = ["^",">","v","<"]
        return f"({self.x},{self.y},{(self.cost+(self.dir_cnt*1000))})"
    def __hash__(self):
        return self.x * 10000 + self.y


todo_list = []
costlist = {}

start = PointA(1, h - 1, 1, 0, 0)
end = PointA(w - 1, 1)

heapq.heappush(todo_list, start)


def get_next(p: PointA):
    res = []
    for move in range(len(dirs4)):
        x = p.x + dirs4[move][0]
        y = p.y + dirs4[move][1]
        dif = (move - p.last_dir)%4
        d2 = p.dir_cnt
        if dif == 1 or dif == 3:
            d2 = p.dir_cnt + 1
        elif dif == 2:
            continue
        elif dif!=0:
            raise IOError()
        if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
            if grid[y][x] != "#":
                q = PointA(x, y, move, d2, p.cost + 1)
                q.prev = p
                res.append(q)
    # print(f"neighbours of {p}: {res}")
    return res

qq = ["^",">","v","<"]
while todo_list:
    point = heapq.heappop(todo_list)
    if hash(point) not in costlist:
        costlist[hash(point)] = [point]
    else:
        costlist[hash(point)].append(point)
    for neighbour in get_next(point):
        if (hash(neighbour) not in costlist):
            heapq.heappush(todo_list, neighbour)
        else:
            #print(costlist[hash(neighbour)],neighbour,min(costlist[hash(neighbour)]))
            if neighbour.val() < min(costlist[hash(neighbour)]).val()+2000:
                heapq.heappush(todo_list, neighbour)

    #if hash(end) in costlist: #== hash(end):
    #    print(costlist[hash(end)])

optimal_route = min(costlist[hash(end)])
a = optimal_route.val()
b = set()
for i in costlist[hash(end)]:
    if i.val() == optimal_route.val():
        prev=i.prev
        while prev:=prev.prev:      #this is very short, but skips the end point
            b.add(Point(prev.x,prev.y))
print(a)
print(len(b)+2) #2 for begin and end

with Image.new("RGBA", (w+1, h+1), (255, 255, 255, 255)) as im:
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x]== ".":
                im.putpixel((x, y), (0, 0, 0, 255))
            else:
                im.putpixel((x, y), (0, 0, 64, 255))
            if Point(x, y) in b:
                im.putpixel((x, y), (255, 0, 0, 255))
    im.save(f"day16.png")