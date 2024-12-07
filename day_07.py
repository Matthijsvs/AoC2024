import copy

from get_src import get
inp = get()


def solve(v,l,s):
    if len(l)>0:
        next = l.pop(0)
        if v <= test_value:
            solve(v*next,copy.deepcopy(l),s)
            solve(v+next,copy.deepcopy(l),s)
    else:
        s.add(v)

def solve2(v,l,s):
    if len(l)>0:
        next = l.pop(0)
        if v <= test_value:
            solve2(int(str(v)+str(next)), copy.deepcopy(l), s)
            solve2(v*next,copy.deepcopy(l),s)
            solve2(v+next,copy.deepcopy(l),s)
    else:
        s.add(v)

sum_a=0
sum_b=0
for i in inp.splitlines():
    a,b=i.split(":")
    test_value= int(a)
    op_values = list(map(int, b.split()))

    start = op_values.pop(0)
    enda = set()
    endb = set()
    solve(start,copy.deepcopy(op_values),enda)
    if test_value in enda:
        sum_a+=test_value

    solve2(start,op_values,endb)
    if test_value in endb:
        sum_b+=test_value
print(sum_a)
print(sum_b)
