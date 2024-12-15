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
    for y in range(len(large_grid)):
        for x in range(len(large_grid[0])):
            if (Point(x,y),Point(x+1,y)) in box2:
                print("[",end='')
            elif (Point(x-1,y),Point(x,y)) in box2:
                print("]",end='')
            elif pos.x == x and pos.y == y:
                print("@", end='')
            else:
                print(large_grid[y][x],end='')
        print()

inp = get(sample2)

cmds = []
#part 1
grid=[]
box = []
current_pos = None
#part 2
large_grid=[]
current_pos2=None
box2=[]

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
            box2.append((Point(x,y),Point(x+1,y)))
            large_grid[y][x]="."
            large_grid[y][x+1] = "."
        elif large_grid[y][x] == "@":
            current_pos2 = Point(x,y)
            large_grid[y][x] = "."

direction = {"<":W,"^":N,">":E,"v":S}


def movebox(point,direction):
    boxtarget = step(point, direction)
    if grid[boxtarget.y][boxtarget.x] == "#":
        return False
    if boxtarget in box:
        return movebox(boxtarget,direction)
    else:
        box.remove(target)
        box.append(boxtarget)
        return True

def movebox2(point,direction):
    boxtarget = (step(point[0], direction),step(point[1], direction))
    if large_grid[boxtarget[0].y][boxtarget[0].x] == "#" or large_grid[boxtarget[1].y][boxtarget[1].x] == "#":
        return False
    if boxtarget in box:
        return movebox(boxtarget,direction)
    else:
        #print(point,boxtarget)
        box2.remove(point)
        box2.append(boxtarget)
        return True


for c in cmds:
    target = step(current_pos,direction[c])
    if grid[target.y][target.x]=="#": #walk into wall
        continue
    elif target in box: #walk into box
        if movebox(target,direction[c]):
            current_pos = target
    else:
        current_pos = target

for c in cmds:
    pprint(current_pos2)
    target = step(current_pos2,direction[c])        #this is the position we want to go being a fish
    target2 = step(target, direction[c])            #this is the position behind the target
    if c=="<":
        pt = (target2,target)
    else:
        pt = (target,target2)
    if large_grid[target.y][target.x]=="#": #walk into wall
        continue
    elif pt in box2: #walk into box
        if movebox2(pt,direction[c]):
            current_pos2 = target
    else:
        current_pos2 = target

sum_a=0
for i in box:
    sum_a+=i.x+i.y*100
print(sum_a)

sum_a=0
for i,j in box2:
    sum_a+=i.x+i.y*100
print(sum_a)