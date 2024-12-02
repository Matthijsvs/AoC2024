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

        """
        #print("problem with",res)
        current = copy.deepcopy(l)
        before =  copy.deepcopy(l)
        #after =  copy.deepcopy(l)

        del(current[res])
        del(before[res-1])
        if res == 1:
            print(l,current,before)
        #if res+1 < len(after):
        #   del (after[res+1])
        #print(l,current,before,after,res)
        res=test(current)
        if res==0:
            print("ok", current)
            sum+=1
            continue
        else:
            res=test(before)
            if res==0:
                sum+=1
                continue
                print("ok",before)
            else:
                #print("nok")
                pass
        """
print(sum)