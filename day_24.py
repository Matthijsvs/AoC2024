from get_src import *

inp = get()

replace = {"dtv":"z37",
           "z37":"dtv"}
replace.update({"qts":"nqs",
                "nqs":"qts"})
replace.update({"gdv":"z29",
                "z29":"gdv"})
replace.update({"dgr":"vvm",
                "vvm":"dgr"})
b=list(replace.keys())
b.sort()
print(",".join(b))

def do_sum(x=-1, y=-1):
    d = {}
    todo = inp.splitlines()
    while todo:
        todo2 = []
        for i in todo:
            if ":" in i:
                name, val = i.split(":")
                if x != -1:
                    if name[0] == "x":
                        d[name] = (x >> int(name[1:]))&1
                    else:
                        d[name] = (y >> int(name[1:]))&1
                else:
                    d[name] = int(val)
            elif "->" in i:
                A, operator, B, _, out = i.split(" ")
                if out in replace:
                    out = replace[out]
                if (A not in d) or (B not in d):
                    todo2.append(i)
                else:
                    if operator == "OR":
                        d[out] = d.get(A, 0) | d.get(B, 0)
                    elif operator == "XOR":
                        d[out] = d.get(A, 0) ^ d.get(B, 0)
                    elif operator == "AND":
                        d[out] = d.get(A, 0) & d.get(B, 0)
                    else:
                        print(operator)
            todo = todo2
    #print(d)

    A = 0
    for i in range(64):
        str = f"z{i:02}"
        #print(str,d.get(str, 0)<<i)
        A |= d.get(str, 0) << i
    return A


print(do_sum())

prev=0
pairs = []
for i in range(44):
    t = do_sum(1<<i,0)
    print(f"{i:2}{t:>50b}")
    if t==prev:
        pairs.append(i)
    prev=t
prev=0

def find(symbol,layer=0):
    for i in inp.splitlines():
        if "->" in i:
            A, operator, B, _, out = i.split(" ")
            if out in replace:
                out = replace[out]
            if symbol == out and layer<3:
                return f"{symbol}=({find(A,layer+1)} {operator} {find(B,layer+1)})"
            if symbol==out:
                return out
                return f"({symbol}={A} {operator} {B})"
            """if "z" in out:
                n = int(out[1:])
                if n in pairs or n-1 in pairs:
                    mapping[n]=[out,A,operator,B]
            if operator == "OR":
                d[out] = d.get(A, 0) | d.get(B, 0)
            elif operator == "XOR":
                d[out] = d.get(A, 0) ^ d.get(B, 0)
            elif operator == "AND":
                d[out] = d.get(A, 0) & d.get(B, 0)
            else:
                print(operator)
            """
    return symbol

for i in range(7,8):
    t = f"z{i:02}"
    print(find(t))

print()
for i in pairs:
    t = f"z{i - 2:02}"
    print(find(t))
    t=f"z{i-1:02}"
    print(find(t))
    t=f"z{i:02}"
    print(find(t))

