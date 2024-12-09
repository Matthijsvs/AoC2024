import copy

from get_src import get
inp = get()


def test(l:list):
    last = l[0]
    increase =  l[1]>last
    safe=True
    unsafe=0
    pos = 1
    for r in l[1:]:
        if increase:
            safe = r-last<=3 and r-last>0
        else:
            safe = last-r<=3 and last-r>0
        last = r
        if not safe:
            return pos
        pos+=1
    else:
        return 0

sum=0
for i in inp.splitlines():
    l=i.split(" ")
    l = list(map(int,l))
    res=test(l)
    if res == 0:
        sum+=1
    else:
        for i in range(len(l)):
            n=copy.deepcopy(l)
            del(n[i])
            res=test(n)
            if res==0:
                sum+=1
                break
print(sum)