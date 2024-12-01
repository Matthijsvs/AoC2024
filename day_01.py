from get_src import get
inp = get()

l=[]
r=[]
for i in inp.splitlines():
    a,b=i.split("   ")
    l.append(int(a))
    r.append(int(b))

l.sort()
r.sort()
sum_a=0
sum_b=0
for i in range(len(l)):
    sum_a+= abs(l[i]-r[i])
    sum_b+= l[i]*r.count(l[i])
print(sum_a)
print(sum_b)
