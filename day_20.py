import copy
import heapq
from dataclasses import dataclass

from PIL import Image

from get_src import *

sample = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""

grid = get_grid()


@dataclass
class PointA:
    x: int
    y: int
    last_dir: int = 0
    dir_cnt: int = 0  # number of turns
    cost: int = 1e9

    def val(self):
        return self.cost

    prev: any = None

    def __lt__(self, other):
        return self.val() < other.val()

    def __repr__(self):
        d = ["^", ">", "v", "<"]
        return f"({self.x},{self.y},{self.cost})"

    def __hash__(self):
        return self.x * 10000 + self.y



for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x]=="S":
            start = PointA(x, y, 1, 0, 0)

        elif grid[y][x]=="E":
            end = PointA(x, y)



def get_next(p: PointA,grid):
    res = []
    for move in range(len(dirs4)):
        x = p.x + dirs4[move][0]
        y = p.y + dirs4[move][1]
        dif = (move - p.last_dir)%4
        d2 = p.dir_cnt
        if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
            if grid[y][x] != "#":
                q = PointA(x, y, move, d2, p.cost + 1)
                q.prev = p
                res.append(q)
            elif grid[y][x]=="#" and d2==10:
                q = PointA(x, y, move, d2+1, p.cost + 1)
                q.prev = p
                res.append(q)
    return res


def run_grid(grid):
    todo_list = []
    heapq.heappush(todo_list, start)
    costlist = {}
    while todo_list:
        point = heapq.heappop(todo_list)
        if hash(point) not in costlist:
            costlist[hash(point)] = [point]
        else:
            costlist[hash(point)].append(point)
        for neighbour in get_next(point,grid):
            if (hash(neighbour) not in costlist):
                heapq.heappush(todo_list, neighbour)
            else:
                if neighbour.val() < min(costlist[hash(neighbour)]).val():
                    heapq.heappush(todo_list, neighbour)



    return min(costlist[hash(end)])


a=[]
cl = run_grid(grid)
prev=cl.prev
a.append(Point(prev.x, prev.y))
while prev:=prev.prev:      #this is very short, but skips the end point
    a.insert(0,Point(prev.x,prev.y))
a.append(Point(end.x,end.y))
def step(P,dir):
    return Point(P.x+dir[0],P.y+dir[1])

dira={}
sum_a=0
#print(a)
for stp in range(len(a)):
    p = a[stp]
    for dir in dirs4:
        newp = step(p,dir)
        if grid[newp.y][newp.x]=="#":
            newp2=step(newp,dir)
            if newp2 in a and a.index(newp2)>stp:
                discount = a.index(newp2)-stp-2
                if discount>=100:
                    sum_a+=1
                if discount not in dira:
                    dira[discount]=1
                else:
                    dira[discount]+=1
#print(dira)
print(sum_a)
dirb={}
sum_b=0

for stp in range(len(a)):
    for y in range(-20,21):
        for x in range(-20,21):
            if abs(x)+abs(y)>20:
                continue
            q = Point(a[stp].x+x,a[stp].y+y)
            if q in a and a.index(q)>=stp+(abs(x)+abs(y))+100:
                sum_b+=1
                continue
print(sum_b)
sum_b=0
for stp in range(0,len(a)):
    for stp2 in range(stp+50,len(a)):
        dx=a[stp2].x-a[stp].x
        dy=a[stp2].y-a[stp].y
        l = abs(dx)+abs(dy)
        if (stp2-stp)-l>=100:
            pwon =stp2-stp-l
            sum_b+=1
            if pwon in dirb:
                dirb[pwon]+=1
            else:
                dirb[pwon]=1
print(sum_b)

for k in sorted(dirb.keys()):
    print(dirb[k],k)
print(sum_a)
with Image.new("RGBA", (len(grid[0]), len(grid)), (255, 255, 255, 255)) as im:
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x]== ".":
                im.putpixel((x, y), (0, 0, 0, 255))
            else:
                im.putpixel((x, y), (0, 0, 64, 255))
            if Point(x, y) in a:
                im.putpixel((x, y), (255, 0, 0, 255))
    im.save(f"day20.png")



