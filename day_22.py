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

k = list(map(int,inp.splitlines()))
#k.pop(k.index(4604786))
#k.insert(0,4604786)
parent={}
a = 0
t = []
p =0
while k:
    s = k[p]
    for j in range(2001):
        s = step(s)
        if s in k:
            k.remove(s)
            print(len(k))
            p=0
    p+=1
for i in k:
    p = []
    s=int(i)
    #print(s)
    qq = []
    for j in range(2001):
        p.append(s % 10)
        s = step(s)
        if s in k:
            parent[s]=i

    a+=s
    #continue
    find = [-2, 1, -1, 3]
    for i in range(4,len(p)):
        l = [p[-3+i]-p[-4+i],p[-2+i]-p[-3+i],p[-1+i]-p[-2+i],p[+i]-p[-1+i]]
        qq.append((p[i],l))
    t.append(sorted(qq))
    #print(len(qq))

pts={}
for p in parent:
    itm = p
    layer = 1
    while itm in parent:
        itm = parent[itm]
        print(">"*layer,itm)
        layer+=1
#exit()
y = []
for i in t[0]:
    s = 0
    for j in t:
        new = [item for item in j if item[1] == i[1]]
        for e in new:
            #print(e)
            s+=e[0]
    y.append(s)
    print(s,i)

print(max(y))