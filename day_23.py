from get_src import *

sample = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""
inp = get(sample)

p = {}
z = []
for i in inp.splitlines():
    a,b = i.strip().split("-")
    for k in z:
        if a in k:
            k.append(b)
            break
        elif b in k:
            k.append(a)
            break
    else:
        z.append([a,b])
    #print(z)
    """if a in p:
        p[a].append(b)
    else:
        p[a]=[b]
    if b in p:
        p[b].append(a)
    else:
        p[b]=[a]
    
q = []
for i in p:
    if "t" in i:
        print(i,p[i])
        q.append(p[i])
print(q)"""

qq = []
for i in z:
    p = set(i)
    if len(p)>3:
        for j in range(len(p)-3):
            qq.append(list(p)[j:j+3])
    else:
        qq.append(list(p))

z = []
for q in qq:
    q.sort()
    z.append("-".join(q))
z = set(z)
print(len(z))
for i in z:
    print(i)