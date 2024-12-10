from get_src import *

grid = get_grid()

def solveX(x, y):
    s = 0
    for d in dirs8:
        try:
            if (grid[y + d[1]][x + d[0]] == "M" and grid[y + d[1] * 2][x + d[0] * 2] == "A" and
                    grid[y + d[1] * 3][x + d[0] * 3] == "S") and 0<=(y + d[1] * 3)<len(grid) and 0<=(x + d[0] * 3)<len(grid[0]):
                s += 1
        except:
            continue
    return s

def solveMas(x, y):
    if 0<x<len(grid[0])-1 and 0<y<len(grid)-1:
        if (grid[y-1][x-1] == "M" and grid[y+1][x+1] == "S" or
                grid[y - 1][x - 1] == "S" and grid[y + 1][x + 1] == "M") and (grid[y - 1][x + 1] == "M" and grid[y + 1][x - 1] == "S" or
            grid[y - 1][x + 1] == "S" and grid[y + 1][x - 1] == "M"):
            return 1
    return 0

sum_a = 0
sum_b = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "X":
            sum_a += solveX(x, y)
        elif grid[y][x] == "A":
            sum_b+= solveMas(x, y)
print(sum_a)
print(sum_b)
