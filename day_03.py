from get_src import get
inp = get()
import re

enable = True

def mul(a,b):
    if enable:
        return a*b
    else:
        return 0

def do():
    global enable
    enable=True
    return 0

def dont():
    global enable
    enable = False
    return 0


regex= "mul\(\d{1,3},\d{1,3}\)"
sum = 0
for i in re.findall(regex,inp):
    sum+=eval(i)
print(sum)

part2 = "mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"
sum = 0
for i in re.findall(part2,inp):
    i=i.replace("'","")
    print(i,eval(i))
    sum+=eval(i)
print(sum)