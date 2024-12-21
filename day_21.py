# press F5 to copy this to a day file
from get_src import *

sample = """029A
980A
179A
456A
379A"""
inp = get(sample)

grid = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["", "0", "A"]]
grid2 = [["", "^", "A"], ["<", "v", ">"]]
pt_numpad = {}
for y in range(len(grid)):
    for x in range(len(grid[0])):
        pt_numpad[grid[y][x]] = Point(x, y)

pt_dirpad = {}
for y in range(len(grid2)):
    for x in range(len(grid2[0])):
        pt_dirpad[grid2[y][x]] = Point(x, y)



def find_dirpad(code: str):
    start = pt_dirpad["A"]
    str_cmd = ""
    for j in code:
        up = (start.y - pt_dirpad[j].y)
        left = (start.x - pt_dirpad[j].x)
        cmd = ""

        if start.x==0:
            if left > 0:
                cmd += "<" * left
            else:
                cmd += ">" * abs(left)

            if up > 0:
                cmd += "^" * up
            else:
                cmd += "v" * abs(up)
        else:
            if up > 0:
                cmd += "^" * up
            else:
                cmd += "v" * abs(up)

            if left > 0:
                cmd += "<" * left
            else:
                cmd += ">" * abs(left)

        start = pt_dirpad[j]
        str_cmd += cmd + "A"
    return str_cmd

def find_dirpad2(start,code: str):
    str_cmd = ""
    for j in code:
        up = (start.y - pt_dirpad[j].y)
        left = (start.x - pt_dirpad[j].x)
        cmd = ""

        if start.x==0:
            if left > 0:
                cmd += "<" * left
            else:
                cmd += ">" * abs(left)

            if up > 0:
                cmd += "^" * up
            else:
                cmd += "v" * abs(up)
        else:
            if up > 0:
                cmd += "^" * up
            else:
                cmd += "v" * abs(up)

            if left > 0:
                cmd += "<" * left
            else:
                cmd += ">" * abs(left)

        start = pt_dirpad[j]
        str_cmd += cmd + "A"
    return str_cmd,start

sum_a = 0
sum_a2 = 0
for i in inp.splitlines():
    start = pt_numpad["A"]

    code = list(i.strip())
    numeric = int(i.replace("A", ""))
    print(i)
    l = 0
    strcmd = ""
    last_pos=pt_dirpad["A"]
    last_pos2 = pt_dirpad["A"]
    for j in code:
        up = (start.y - pt_numpad[j].y)
        left = (start.x - pt_numpad[j].x)
        cmd = ""
        if up > 0:
            cmd += "^" * up
        else:
            cmd += "v" * abs(up)
        if left > 0:
            cmd += "<" * left
        else:
            cmd += ">" * abs(left)
        strcmd += cmd + "A"
        print(f"n: {cmd:<20s}{j:>10s}")
        seq,last_pos=find_dirpad2(last_pos,cmd + "A")
        seq2, last_pos2 = find_dirpad2(last_pos2,seq)
        print("2:",seq)
        print("3:", seq2)
        start = pt_numpad[j]
        sum_a2 += len(seq2)*numeric
    #print(i,":", find_dirpad(find_dirpad(strcmd)))
    #print(len(find_dirpad(find_dirpad(strcmd))), numeric)
    sum_a += len(find_dirpad(find_dirpad(strcmd))) * numeric

print(sum_a)
print(sum_a2)