import re
from get_src import *
from sympy import symbols, Eq, solve

sample = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


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


inp = get(sample)
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
print(sum_a)
