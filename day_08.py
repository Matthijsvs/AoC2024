# press F5 to copy this to a day file
from get_src import get

inp = get()
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

grid = []
pts = {}
for i in inp.splitlines():
    grid.append(list(i))


def inside(n):
    return 0 <= n.x < len(grid[0]) and 0 <= n.y < len(grid)


def anti(p: Point, q: Point):
    distanceX = q.x - p.x
    distanceY = q.y - p.y
    node1 = Point(p.x - distanceX, p.y - distanceY)
    node2 = Point(q.x + distanceX, q.y + distanceY)
    ret = []
    if inside(node1):
        grid[node1.y][node1.x] = "#"
        ret.append(node1)
    if inside(node2):
        grid[node2.y][node2.x] = "#"
        ret.append(node2)
    return ret


def anti2(p: Point, q: Point):
    distanceX = q.x - p.x
    distanceY = q.y - p.y
    ret = []
    for i in range(100):
        node1 = Point(p.x - distanceX * i, p.y - distanceY * i)
        if inside(node1):
            ret.append(node1)
    for i in range(100):
        node2 = Point(q.x + distanceX * i, q.y + distanceY * i)
        if inside(node2):
            ret.append(node2)
    return ret


for y in range(len(grid)):  # get all antenna locations
    for x in range(len(grid[y])):
        l = grid[y][x]
        if l != ".":
            if l not in pts:
                pts[l] = []
            pts[l].append(Point(x, y))

# print(pts)
lst_a = []
lst_b = []
for pt in pts:
    t = len(pts[pt])
    p = pts[pt]
    for i in range(t):
        for j in range(i + 1, t):
            lst_a.extend(anti(p[i], p[j]))
            lst_b.extend(anti2(p[i], p[j]))

print(len(set(lst_a)))
print(len(set(lst_b)))
