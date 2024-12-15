from operator import truediv

from get_src import *

sample = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""
sample2="""#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^"""
def inside(p,grid):
    return 0<=p.x<len(grid[0]) and 0<=p.y<len(grid)

def step(P,dir):
    return Point(P.x+dir[0],P.y+dir[1])

def pprint(pos):
    return
    for x in range(len(large_grid[0])):
        print(x//10,end='')
    print()
    for x in range(len(large_grid[0])):
        print(x%10,end='')
    print()

    for y in range(len(large_grid)):
        for x in range(len(large_grid[0])):
            if Point(x,y) in boxL:
                print("[",end='')
            elif Point(x,y) in boxR:
                print("]",end='')
            elif pos.x == x and pos.y == y:
                print("@", end='')
            else:
                print(large_grid[y][x],end='')
        print()

inp = get()

cmds = []
#part 1
grid=[]
box = []
current_pos = None
#part 2
large_grid=[]
current_pos2=None
boxL=[]
boxR=[]
for i in inp.splitlines():
    if "#" in i:
        grid.append(list(i))
        l = []
        for j in list(i):
            if j=="#":
                l.append("#")
                l.append("#")
            elif j =="O":
                l.append("[")
                l.append("]")
            elif j == ".":
                l.append(".")
                l.append(".")
            elif j == "@":
                l.append("@")
                l.append(".")
        large_grid.append(l)
    else:
        cmds.extend(list(i))

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "O":
            box.append(Point(x,y))
            grid[y][x]="."
        elif grid[y][x] == "@":
            current_pos = Point(x,y)
            grid[y][x] = "."

for y in range(len(large_grid)):
    for x in range(len(large_grid[0])):
        if large_grid[y][x] == "[":
            boxL.append(Point(x,y))
            large_grid[y][x]="."
        if large_grid[y][x] == "]":
            boxR.append(Point(x,y))
            large_grid[y][x]="."
        elif large_grid[y][x] == "@":
            current_pos2 = Point(x,y)
            large_grid[y][x] = "."

direction = {"<":W,"^":N,">":E,"v":S}


def movebox(point, direction, local_box):
    boxtarget = step(point, direction)
    if grid[boxtarget.y][boxtarget.x] == "#":
        return False
    if boxtarget in local_box:
        return movebox(boxtarget,direction,local_box)
    else:
        local_box.remove(target)
        local_box.append(boxtarget)
        return True

def do_move(point,direction,pts):
    boxtarget = step(point, direction)
    #print(f"moving {point} to {boxtarget}")
    if point in pts:
        return True
    pts.add(point)
   #print(f"point {point} was not yet done")
    #find counterpart of box
    if point in boxL:
        p2 = Point(point.x+1,point.y)
        do_move(boxtarget, direction, pts)
        do_move(p2,direction,pts)
        boxL.remove(point)
        boxL.append(boxtarget)
    elif point in boxR:
        p2 = Point(point.x-1, point.y)
        do_move(boxtarget, direction, pts)
        do_move(p2, direction, pts)
        boxR.remove(point)
        boxR.append(boxtarget)

def can_move(point, direction, done):
    if large_grid[point.y][point.x] == "#":
        return False
    elif ((point not in boxL) and (point not in boxR)):
        return True

    boxtarget = step(point, direction)
    done.add(point)
    #find counterpart of box
    if point in boxL:
        p2 = Point(point.x+1,point.y)
    elif point in boxR:
        p2 = Point(point.x-1, point.y)

    ans = can_move(boxtarget, direction, done)
    #print(f"check {boxtarget} is free:{ans}")
    if p2 not in done:
        ans &= can_move(step(p2, direction), direction, done)
        #print(f"check {p2} is free:{ans}")
    return ans

############## part 1 ##############
for c in cmds:
    target = step(current_pos,direction[c])
    if grid[target.y][target.x]=="#": #walk into wall
        continue
    elif target in box: #walk into box
        if movebox(target,direction[c],box):
            current_pos = target
    else:
        current_pos = target

############## part 2 ##############
for c in cmds:
    target = step(current_pos2,direction[c])        #this is the position we want to go being a fish
    if large_grid[target.y][target.x]=="#": #walk into wall
        continue
    elif target in boxL or target in boxR:
        plist=set()
        if can_move(target,direction[c],plist):
            do_move(target,direction[c],set())
            current_pos2 = target
    else:
        current_pos2 = target

sum_a=0
for i in box:
    sum_a+=i.x+i.y*100
print(sum_a)

sum_a=0
for i in boxL:
    sum_a+=i.x+i.y*100
print(sum_a)