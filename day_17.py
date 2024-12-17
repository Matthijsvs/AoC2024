# press F5 to copy this to a day file
import math

from get_src import *

sample = """Register A: 117440
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""
inp = get()
A = 4
B = 5
C = 6
reg = {0: 0, 1: 1, 2: 2, 3: 3}
console=[]
for i in inp.splitlines():
    if i.startswith("Register A:"):
        reg[A] = int(i.split(":")[1])
    elif i.startswith("Register B:"):
        reg[B] = int(i.split(":")[1])
    elif i.startswith("Register C:"):
        reg[C] = int(i.split(":")[1])
    elif i.startswith("Program"):
        code = i.split(":")[1].split(",")
        code = list(map(int, code))
print(code)
def adv(op):  # division
    reg[A] = math.trunc(reg[A] / 2 ** reg[op])

def bxl(op):  # bitwise xor
    reg[B] = reg[B] ^ op

def bst(op):
    reg[B] = reg[op] & 7

def jnz(op):  # jump not zero
    if reg[A] != 0:
        return op

def bxc(op):  # bitwise xor
    reg[B] = reg[B] ^ reg[C]

def out(op):
    console.append(str(reg[op] % 8))

def bdv(op):
    reg[B] = math.trunc(reg[A] / 2 ** reg[op])

def cdv(op):
    reg[C] = math.trunc(reg[A] / 2 ** reg[op])

instr = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}
def run():
    global console
    console=[]
    ip = 0  # instruction pointer
    while ip < len(code):
        #print(str(instr[code[ip]]), code[ip + 1])
        ret = instr[code[ip]](code[ip + 1])
        #print(str(instr[code[ip]]), code[ip + 1],reg)
        # print(reg)
        if ret != None:
            ip = ret
        else:
            ip += 2
    return ",".join(console)

#partA = run()
#print(partA)
t = len(code)-2
RegAInit=0
while t>0:
    search =f"{code[t]},{code[t+1]}"
    print(f"searching:{search}")
    for i in range(255):
        reg[A]= (RegAInit << 8) + i
        reg[B]=0
        reg[C]=0
        partB = run()
        if partB[:3]==search:
            RegAInit= (RegAInit << 8) + i
            print(RegAInit, partB)
            t-=2
            break
    else:
        break
print(RegAInit)