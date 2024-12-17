# press F5 to copy this to a day file
import math
from get_src import *
sample="""Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""
inp = get()
A = 4
B = 5
C = 6
reg = {0: 0, 1: 1, 2: 2, 3: 3}
console=[]
def debug(s):
    pass
    #print(f"{str(s):<10s}\t\t{reg}")

for i in inp.splitlines():
    if i.startswith("Register A:"):
        reg[A] = int(i.split(":")[1])
    elif i.startswith("Register B:"):
        reg[B] = int(i.split(":")[1])
    elif i.startswith("Register C:"):
        reg[C] = int(i.split(":")[1])
    elif i.startswith("Program"):
        codeb = i.split(":")[1].strip().split(",")
        code = list(map(int, codeb))

def adv(op):  # division
    reg[A] = reg[A]>>reg[op]#math.trunc(reg[A] / 2 ** reg[op])
    debug(f"A>>{reg[op]}")

def bxl(op):  # bitwise xor
    reg[B] = reg[B] ^ op
    debug(f"B^{op}")

def bst(op):
    reg[B] = reg[op] & 7
    debug(f"B={op} & 0b111")

def jnz(op):  # jump not zero
    if reg[A] != 0:
        debug("jump")
        return op

def bxc(op):  # bitwise xor
    reg[B] = reg[B] ^ reg[C]
    debug(f"B=B^C")

def out(op):
    console.append(str(reg[op] % 8))
    debug(reg[op] % 8)
def bdv(op):
    reg[B] = math.trunc(reg[A] / 2 ** reg[op])
    debug(f"B=A>>{reg[op]}")

def cdv(op):
    reg[C] = reg[A]>>reg[op] #math.trunc(reg[A] / 2 ** reg[op])
    debug(f"C=A>>{reg[op]}")

instr = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}
def run_code():
    global console
    console=[]
    ip = 0  # instruction pointer
    while ip < len(code):
        ret = instr[code[ip]](code[ip + 1])
        if ret != None:
            ip = ret
        else:
            ip += 2
    return ",".join(console)

src=",".join(codeb).strip()
partA = run_code()
print(f"A:{partA}")

def find(t,regA):
    res=[]
    for j in range(8):
        reg[A]=regA+j
        reg[B]=0
        reg[C]=0
        p = run_code()
        if t==p[0] and ((p in src) ) :
            #print(f"{p:>32s}    {(regA|j)}")
            res.append((regA|j))
    return res

regA=0
newp = [0]
for i in range(len(code)-1,-1,-1):
    t = codeb[i]
    p=set(newp)
    newp=[]
    debug(f"\nfinding:{t} with start {p}")
    for start in p:
        newp.extend(find(t,start<<3))

print(f"B:{min(newp)}")
