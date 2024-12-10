import copy
from get_src import *

grid =get_grid()

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x]=="^":
            startx=x
            starty=y

x=startx
y=starty
steplist=[]

steps=0
direction = 0
def inside(x,y,grid):
    return 0<=x<len(grid[0]) and 0<=y<len(grid)
def pprint(grid):
    for i in grid:
        print ("".join(i))

while inside(x,y,grid) and steps<100000:
    newx=x+dirs4[direction][0]
    newy=y+dirs4[direction][1]
    if not inside(newx,newy,grid):
        break
    if grid[newy][newx]=="#":
        direction = (direction + 1) % 4
        continue
    else:
        grid[newy][newx]="x"
        x=newx
        y=newy
        steplist.append((x,y))
        steps += 1

def solve(grid,x,y):
    steps=0
    direction = 0
    while inside(x,y,grid) and steps<100000:
        newx=x+dirs4[direction][0]
        newy=y+dirs4[direction][1]
        if not inside(newx,newy,grid):
            return True
        if grid[newy][newx]=="#":
            direction = (direction + 1) % 4
            continue
        else:
            grid[newy][newx]="x"
            x=newx
            y=newy
            steps += 1
    return False

sum_a=0
for i in grid:
    sum_a+=i.count("x")
print(sum_a+1) #starting point :(

grid = get_grid()
steplist = set(steplist)
sum_b=0
for i in steplist:
    grid2= copy.deepcopy(grid)
    grid2[i[1]][i[0]]="#"
    if solve(grid2,startx,starty):
        pass
    else:
        sum_b+=1
print(sum_b)
