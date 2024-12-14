import re
from get_src import *

sample = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""
#sample = "p=2,4 v=2,-3"

robots = []

grid = 101
grid2= 103
inp = get().splitlines()
for i in inp:
    q = re.findall("=(-?\d*),(-?\d*) v=(-?\d*),(-?\d*)",i)[0]
    q=list(map(int,list(q)))

    robots.append(q)

def do(step):
    robots2 = []
    for q in robots:
        x,y,vx,vy=q
        newx = (x + (vx*step))%grid
        newy = (y + (vy*step))%grid2
        robots2.append([newx,newy,vx,vy])

    count=[0,0,0,0,0]
    cx=grid//2
    cy=grid2//2
    for q in robots2:
        quad=4
        x, y, vx, vy = q
        if x<cx and y<cy:
            quad=0
        elif x>cx and y<cy:
            quad=1
        elif x<cx and y>cy:
            quad=2
        elif x>cx and y>cy:
            quad=3
        count[quad]+=1
    return robots2,count[0]*count[1]*count[2]*count[3]
d={}
for i in range(10000):
    r,s=do(i)
    d[i]=s
tries=[]
sorted_by_values = dict(sorted(d.items(), key=lambda item: item[1]))
for i in sorted_by_values:
    if d[i]==4:
        tries.append(i)
tries = list(sorted_by_values.keys())[:10]

from PIL import Image, ImageDraw
print(do(100)[1])
for step in tries:
    print(f"step={step},score = {d[step]}")
    continue
    """
    with Image.new("RGBA", (grid, grid2), (255, 255, 255, 255)) as im:
        robots2,s=do(step)
        for q in robots2:
            x,y,vx,vy=q
            im.putpixel((x, y), (255, 0, 0, 255))
    im.save(f"day14_Step{step}.png")
    """
