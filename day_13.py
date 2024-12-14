import re
from get_src import *
from sympy import symbols, Eq, solve

def rfind(s):
    return re.findall("X[\+=](\d*),\sY[\+=](\d*)", s)[0]


def solveA(xa, ya, xb, yb, xp, yp):
    xp = int(xp) + 10000000000000
    yp = int(yp) + 10000000000000
    a, b = symbols('a b')
    x1, y1, x2, y2, p1, p2 = symbols(f"{xa} {ya} {xb} {yb} {xp} {yp}")
    eq1 = Eq((a * x1) + (b * x2), p1)
    eq2 = Eq((a * y1) + (b * y2), p2)
    sol_dict = solve((eq1, eq2), (a, b))
    print(sol_dict)
    res_a = eval(str(sol_dict[a]))
    res_b = eval(str(sol_dict[b]))
    if (res_a % 1) == 0 and res_b % 1 == 0:
        return res_a * 3 + res_b * 1
    return 0


inp = get()
sum_a = 0
for i in inp.splitlines():
    if ":" in i:
        name, location = i.split(":")
        if name == "Button A":
            xa, ya = rfind(location)
        elif name == "Button B":
            xb, yb = rfind(location)
        elif name == "Prize":
            xp, yp = rfind(location)
    else:
        sum_a += solveA(xa, ya, xb, yb, xp, yp)
sum_a += solveA(xa, ya, xb, yb, xp, yp)
print(int(sum_a))
