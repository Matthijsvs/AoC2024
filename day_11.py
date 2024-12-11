import copy

from get_src import *

sample = """125 17"""
inp = get()
lst = list(map(int,inp.split()))
#print(lst)

newcounts = {}
for i in lst:
    newcounts[i]=1

def add(num,val):
    if num not in newcounts:
        newcounts[num]=0
    newcounts[num]+=val

for i in range(75):
    counts = copy.deepcopy(newcounts)
    newcounts={}

    t = counts.keys()
    for j in list(t):
        if counts[j]>0:
            q = str(j)
            l=len(q)
            if j == 0:
                add(1,counts[j])
            elif (l%2)==0:
                a=int(q[:l//2])
                b=int(q[l // 2:])
                add(a,counts[j])
                add(b,counts[j])
            else:
                add(j*2024,counts[j])

    if i%25==24:
        sum_a = 0
        for k in newcounts.keys():
            sum_a += newcounts[k]
        print(i,sum_a)
