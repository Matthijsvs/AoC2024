import copy

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

p= {}
for node2 in inp.splitlines():
    a,b = node2.strip().split("-")

    if a in p:
        p[a].append(b)
    else:
        p[a]=[b]
    if b in p:
        p[b].append(a)
    else:
        p[b]=[a]

ic = []
for i in p:
    print(i,p[i])
for node1 in p:
    for node2 in p[node1]:
        for node3 in p[node2]:
            if node1 in p[node3]:
                t = [node1,node2,node3]
                t.sort()
                ic.append("-".join(t))

def find_myself(node,link,level,chain):
    for subnode in p[link]:
        if level>1 and subnode == node:
            print(chain)
            return chain
        else:
            if subnode not in chain:
                chain2 = copy.deepcopy(chain)
                chain2.append(subnode)
                chain = find_myself(node,subnode, level + 1, chain2)
    return chain

for node1 in p:
    print(node1)
    print(find_myself(node1,node1,0,[node1]))

a = 0
for i in set(ic):
    if "-t" in i or i.startswith("t"):
        a+=1

print(a)