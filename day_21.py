#import functools
from get_src import *

sample = """029A
980A
179A
456A
379A"""
inp = get(sample)

grid = [["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        ["", "0", "A"]]
grid2 = [["", "^", "A"],
         ["<", "v", ">"]]
pt_numpad = {}
for y in range(len(grid)):
    for x in range(len(grid[0])):
        pt_numpad[grid[y][x]] = Point(x, y)

pt_dirpad = {}
for y in range(len(grid2)):
    for x in range(len(grid2[0])):
        pt_dirpad[grid2[y][x]] = Point(x, y)



def find_pt(start,stop,pad):
    up = (start.y - pad[stop].y)
    left = (start.x - pad[stop].x)
    if start.y == pad[""]:#or stop.y == pad[""]:
        cmd = "^" * up + "v" * -up
        cmd += "<" * left + ">" * -left
        return [cmd]
    else:
        cmd = "<" * left + ">" * -left
        cmd += "^" * up + "v" * -up

        cmd2 = "^" * up + "v" * -up
        cmd2 += "<" * left + ">" * -left
        return list(set([cmd,cmd2]))

def find_pad(code,pad):
    start = pad["A"]
    path=[]
    for letter in code:
        path.append([])
        t = find_pt(start, letter, pad)
        path[-1].extend(t)
        start = pad[letter]
    return path


def iter_dpad(level,cmd:str, sol):
    sol[level]=[]

    if level == 0:
        sol[level] = find_pad(cmd,pt_numpad) #, find_pad(cmd,pt_numpad, False)]
    else:
        iter_dpad(level - 1, cmd, sol)
        for i in sol[level-1]:
            for j in i:
                sol[level].extend(find_pad(j,pt_dirpad))
    q = int(1e12)
    print(sol[level])
    #for i in set(sol[level]):
        #print(i)
        #q = min(len(i),q)
    return q



sum_a = 0
sum_a2 = 0
for i in inp.splitlines():
    code = list(i.strip())
    #print(i)
    numeric = int(i.replace("A", ""))
    complexity = iter_dpad(2,i, {})
    sum_a += complexity * numeric
    print(i,complexity,numeric)
    #print(i,":", find_dirpad(find_dirpad(strcmd)))
    #print(len(find_dirpad(find_dirpad(strcmd))), numeric)
    #sum_a += len(find_dirpad(find_dirpad(strcmd))) * numeric

print(sum_a)
print(sum_a2)