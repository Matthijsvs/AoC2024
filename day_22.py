from get_src import *
inp = get()

def step(secret):
    number = secret  ^ (secret << 6)
    number = number %16777216
    number = number  ^ (number >> 5)
    number = number %16777216
    number = number  ^ (number <<11)
    number = number %16777216
    return number

k=list(map(int,inp.splitlines()))

qq={}
a=0
for s in k:
    p = [s]
    for j in range(2000):
        s = step(s)
        p.append(s % 10)
    a+=s
    for i in range(4,len(p)):
        l = str([p[-3+i]-p[-4+i],p[-2+i]-p[-3+i],p[-1+i]-p[-2+i],p[+i]-p[-1+i]])
        if l not in qq:
            qq[l]={s:p[i]}
        else:
            if s not in qq[l]:
                qq[l][s]=p[i]
b=0
for i in qq:
    b = max(b,sum(qq[i].values()))
print(a)
print(b)