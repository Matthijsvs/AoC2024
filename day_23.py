from get_src import *

inp = get()
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

for node1 in p:
    for node2 in p[node1]:
        for node3 in p[node2]:
            if node1 in p[node3]:
                t = [node1,node2,node3]
                t.sort()
                ic.append("-".join(t))

a = 0
for i in set(ic):
    if "-t" in i or i.startswith("t"):
        a+=1
print(a)

def find_loop(start_node, min_len=3):
    t = set(p[start_node])
    t.add(start_node)
    for link in p[start_node]:
        t2=set(p[link])
        t2.add(link)
        new_set = t.intersection(t2)
        if len(new_set)>=min_len:
            t=new_set
    return t

part_b = ""
for i in p:
    l = find_loop(i)
    if len(l)>len(part_b):
        part_b=l
part_b = list(part_b)
part_b.sort()
print(",".join(part_b))