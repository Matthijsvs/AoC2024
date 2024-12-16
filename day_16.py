import time

from get_src import *
import copy
import heapq
from dataclasses import dataclass

from typing import List

sample = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

sample2="""#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""
maze = get_grid()

w = len(maze[0]) - 1  # highest width
h = len(maze) - 1


@dataclass
class PointA:
    x: int
    y: int
    last_dir: int = 0
    dir_cnt: int = 0  # number of turns
    cost: int = 1e9

    def __lt__(self, other):
        return (self.cost+(self.dir_cnt*1000)) < (other.cost+(other.dir_cnt*1000))

    def __hash__(self):
        return self.x * 10000 + self.y


todo_list = []
costlist = {}

start = PointA(1, h - 1, 1, 0, 0)
end = PointA(w - 1, 1)
print(maze[start.y][start.x])
print(maze[end.y][end.x])
heapq.heappush(todo_list, start)


def get_next(p: PointA):
    res = []
    for move in range(len(dirs4)):
        x = p.x + dirs4[move][0]
        y = p.y + dirs4[move][1]
        if p.last_dir == move:
            d2 = p.dir_cnt
        else:
            d2 = p.dir_cnt + 1
        if 0 <= x < len(maze[0]) and 0 <= y < len(maze):
            if maze[y][x] != "#":
                q = PointA(x, y, move, d2, p.cost + 1)
                res.append(q)
    # print(f"neighbours of {p}: {res}")
    return res

qq = ["^",">","v","<"]
while todo_list:



    point = heapq.heappop(todo_list)
    costlist[hash(point)] = point
    for neighbour in get_next(point):
        if (hash(neighbour) not in costlist) or (neighbour < costlist[hash(neighbour)]):
            costlist[hash(neighbour)] = neighbour
            heapq.heappush(todo_list, neighbour)

    if hash(end) in costlist:
        print(costlist[hash(end)])
        #break


print(costlist[hash(end)].dir_cnt*1000+costlist[hash(end)].cost)
for y in range(len(maze)):
    for x in range(len(maze[0])):
        if hash(PointA(x, y)) in costlist:
            print(qq[costlist[hash(PointA(x, y))].last_dir], end='')
        else:
            print(maze[y][x], end='')
    print()
