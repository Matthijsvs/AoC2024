from get_src import *

grid = get_grid()

def inside(p,grid):
    return 0<=p.x<len(grid[0]) and 0<=p.y<len(grid)

def step(P,dir):
    return Point(P.x+dir[0],P.y+dir[1])

def find(start_point, point_set, edges):
    if start_point in point_set:
        return
    point_set.add(start_point)
    for direction in dirs4:
        new = step(start_point, direction)
        if not inside(new,grid):
            edges.add((new, direction))
        else:
            letter = grid[start_point.y][start_point.x]
            if grid[new.y][new.x]==letter:
                find(new, point_set, edges)
            else:
                edges.add((new, direction))


def findPerimeterB(s):
    sides={N:{},E: {},S: {},W: {}}
    sum=0
    for point,direction in s:
        if direction == N or direction == S:
            if point.y not in sides[direction]:
                sides[direction][point.y]=set()
            sides[direction][point.y].add(point.x)
        else:
            if point.x not in sides[direction]:
                sides[direction][point.x] = set()
            sides[direction][point.x].add(point.y)

    for direction in dirs4:
        for j in sides[direction]:
            sum+=1
            p = list(sides[direction][j])
            p.sort()
            lst = p[0]
            for k in p[1:]:
                if lst+1!=k:
                    sum+=1
                lst=k
    return sum

sets=[]
for y in range(len(grid)):
    for x in range(len(grid[0])):
        done = False
        for region,edges in sets:
            if Point(x,y) in region:
                done=True
        if not done:
            pts = set()
            edg = set()
            find(Point(x,y),pts,edg)
            sets.append((pts,edg))

sum_a=0
sum_b=0
for points,edges in sets:
    sum_a+=len(edges)*len(points)
    p2 = findPerimeterB(edges)
    sum_b+=p2*len(points)
    p = list(points)
    #print(f"letter: {grid[p[0].y][p[0].x]} pos1 = {p[0]} area:{len(p)},peri={len(edges)},periB={p2}")
print(sum_a)
print(sum_b)