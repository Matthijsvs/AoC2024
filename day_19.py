import copy

from get_src import *

sample = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""
inp = get()

towels=[]
recipes=[]
for i in inp.splitlines():
    if "," in i:
        tmp=i.split(",")
        for i in tmp:
            recipes.append(i.strip())
    elif i!="":
        towels.append(i)




def take2(towel:str,start):
    if start==len(towel):
        return True
    res=[]
    for i in range(start,len(towel)+1):
        if towel[start:i] in recipes:
            #print(f"{towel[start:]} starts with {towel[start:i]}")
            if take2(towel,i):
                return True
    return False

def take(towel:str,start):
    if start==len(towel):
        return 1
    res=0
    for i in range(start,len(towel)+1):
        if towel[start:i] in recipes:
            #print(f"{towel[start:]} starts with {towel[start:i]}")
            res+=take(towel,i)
    return res

a=0
b=0
for towel in towels:
    #print(f"\n[{towel}]")
    if take2(towel,0):
        a+=1

    tmp=take(towel,0)
    b+=tmp
    print(f"{towel},{tmp}")

print(a)
print(b)