#press F5 to copy this to a day file
from get_src import *

sample = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""
inp = get()
A=4
B=5
C=6
reg={0:0,1:1,2:2,3:3}
for i in inp.splitlines():
    if i.startswith("Register A:"):
        reg[A]=int(i.split(":")[1])
    elif i.startswith("Register B:"):
        reg[B] = int(i.split(":")[1])
    elif i.startswith("Register C:"):
        reg[C] = int(i.split(":")[1])
    elif i.startswith("Program"):
        code = i.split(":")[1].split(",")
        code = list(map(int,code))
        print(code)

def adv(op):  #division
    reg[A] = int(reg[A] / 2**op)

def bxl(op):  #bitwise xor
    reg[B] = reg[B] ^ op

def bst(op):
    reg[B] = reg[op] % 8

def jnz(op):  #jump not zero
    if reg[A]!=0:
        return op
def bxc(op):  #bitwise xor
    reg[B] = reg[B] ^ reg[C]
def out(op):
    print(reg[op]%8,end=',')
def bdv(op):
    reg[B] = int(reg[B] / 2 ** op)
def cdv(op):
    reg[C] = int(reg[C] / 2 ** op)

ip = 0  #instruction pointer
instr={0:adv,1:bxl,2:bst,3:jnz,4:bxc,5:out,6:bdv,7:cdv}
while ip<len(code):
    #print(instr[code[ip]],code[ip+1])
    ret = instr[code[ip]](code[ip+1])
    #print(reg)
    if ret!=None:
        ip = ret
    else:
        ip+=2