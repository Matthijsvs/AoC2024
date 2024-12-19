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
cache={}
towels=[]
recipes=[]
maxrecipe=""
for i in inp.splitlines():
    if "," in i:
        tmp=i.split(",")
        for i in tmp:
            if len(i.strip())>len(maxrecipe):
                maxrecipe = i.strip()
            recipes.append(i.strip())
    elif i!="":
        towels.append(i)

maxrecipe=len(maxrecipe)


def calculate_single(towel:str, start):
    if start==len(towel):
        return True
    res=[]
    for i in range(start,start+maxrecipe+1):
        if towel[start:i] in recipes:
            if calculate_single(towel, i):
                return True
    return False

def calculate_all(towel:str, start):
    if start==len(towel):
        return 1
    res=0
    for i in range(start,min(start+maxrecipe+1,len(towel)+1)):
        if towel[start:i] in recipes:
            if i not in cache:
                q = calculate_all(towel, i)
                cache[i]=q
                res += q
            else:
                res += cache[i]

    return res

a=0
b=0
for towel in towels:
    if calculate_single(towel, 0):
        a+=1

    cache = {}
    b+=calculate_all(towel, 0)

print(a)
print(b)