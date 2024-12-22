#press F5 to copy this to a day file
from get_src import *

sample = """1
2
3
2024"""
inp = get()


def step(secret):
    number = secret  ^ (secret << 6)
    number = number %16777216
    number = number  ^ (number >> 5)
    number = number %16777216
    number = number  ^ (number <<11)
    number = number %16777216
    return number

a = 0
t = []
for i in inp.splitlines():
    p = []
    s=int(i)
    #print(s)
    qq = []
    for j in range(2000):
        p.append(s % 10)
        s = step(s)
    a+=s

    find = [-2, 1, -1, 3]
    for i in range(4,len(p)):
        l = [p[-3+i]-p[-4+i],p[-2+i]-p[-3+i],p[-1+i]-p[-2+i],p[+i]-p[-1+i]]
        qq.append((p[i],l))
    t.append(sorted(qq))
    #print(len(qq))

y = []
for i in t[2]:
    s = 0
    for j in t:
        new = [item for item in j if item[1] == i[1]]
        for e in new:
            s+=e[0]
    y.append(s)
    print(s,i)

print(max(y))