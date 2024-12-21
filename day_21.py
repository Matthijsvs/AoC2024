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


#@cache
def find_dirpad(code: str,hor=True):
    start = pt_dirpad["A"]
    str_cmd = ""
    for j in code:
        up = (start.y - pt_dirpad[j].y)
        left = (start.x - pt_dirpad[j].x)
        cmd = ""
        if hor:
                cmd += "<" * left + ">" * -left
                cmd += "^" * up+ "v" * -up
        else:
                cmd += "^" * up + "v" * -up
                cmd += "<" * left + ">" * -left

        start = pt_dirpad[j]
        str_cmd += cmd + "A"
    return str_cmd

def find_pt(start,stop,pad,prev):
    up = (start.y - pad[stop].y)
    left = (start.x - pad[stop].x)
    if start.x == pad[""] or start.x == pad[""]:
        cmd = "^" * up + "v" * -up
        cmd += "<" * left + ">" * -left
        cmd += "A"
        return [prev+cmd]
    else:
        cmd = "<" * left + ">" * -left
        cmd += "^" * up + "v" * -up
        cmd += "A"

        cmd2 = "^" * up + "v" * -up
        cmd2 += "<" * left + ">" * -left
        cmd2 += "A"
        return [prev+cmd,prev+cmd2]

def find_pad(code,pad):
    start = pad["A"]
    path=[]
    for letter in code:
        t = find_pt(start, letter, pad,"")
        if path == []:
            path.extend(t)
        else:
            newpath = []
            for i in t:
                newpath.extend(x+i for x in path)
            path = newpath
        start = pad[letter]
    return list(set(path))

def iter_dpad(level,cmd:str, sol):
    sol[level]=[]

    if level == 0:
        sol[level] = find_pad(cmd,pt_numpad) #, find_pad(cmd,pt_numpad, False)]
    else:
        iter_dpad(level - 1, cmd, sol)
        for i in set(sol[level-1]):
            sol[level].extend(find_pad(i,pt_dirpad))
    q = int(1e12)
    for i in set(sol[level]):
        print(i)
        q = min(len(i),q)
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