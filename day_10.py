from get_src import *
grid = get_numgrid()

#FindHead
heads=[]
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x]==0:
            heads.append(Point(x,y))

def inside(x,y,grid):
    return 0<=x<len(grid[0]) and 0<=y<len(grid)

def step(P,dir):
    return Point(P.x+dir[0],P.y+dir[1])

def find_route(P,val)->list:
    if not inside(P.x,P.y,grid):
        return Point(-1,-1)
    if grid[P.y][P.x]!=val:
        return Point(-1,-1)
    num=[]
    if val<9:
        num.extend(find_route(step(P, N),val+1))
        num.extend(find_route(step(P, E), val + 1))
        num.extend(find_route(step(P, S), val + 1))
        num.extend(find_route(step(P, W), val + 1))
        return num
    else:
        return [P]


sum_a=0
sum_b=0
for i in heads:
    l = find_route(i,0)
    s = set(l)
    s.remove(-1)
    sum_a+=len(s)
    for j in s:
        sum_b+=l.count(j)
print(sum_a)
print(sum_b)