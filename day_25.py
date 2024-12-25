from get_src import *

keys=[]
locks=[]
grids=[[]]
inp = get()

for i in inp.splitlines():
    if i != "":
        grids[-1].append(list(i.strip()))
    else:
        grids.append([])

for i in grids:
    if "#" in i[0]:
        p = []
        for x in range(len(i[0])):
            s = 0
            for y in range(len(i)):
                if i[y][x] == "#":
                    s += 1
            p.append(s-1)
        locks.append(p)
    else:
        p = []
        for x in range(len(i[0])):
            s = 0
            for y in range(len(i)):
                  if i[y][x]=="#":
                      s+=1
            p.append(s-1)
        keys.append(p)

sum_a=0
for j in locks:
    for k in keys:
        skip = False
        for i in range(5):
            if j[i]+k[i]>5:
                skip=True
        if not skip:
            sum_a+=1
print(sum_a)