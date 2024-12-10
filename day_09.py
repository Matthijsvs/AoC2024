from get_src import get, get_numgrid

lst = get_numgrid()[0]
def isFile(i):
    return i%2==0

def takeFromEnd(pos): #return file stolen from
    global lst
    if lst[pos] >= 1:
        lst[pos] -= 1
        return pos//2,pos
    else:
        while lst[pos] == 0:
            pos -= 2
        lst[pos] -= 1
        return pos // 2, pos

def findWholeFile(size,pos): #return file stolen from
    global lst
    for i in range(len(lst)-1,pos,-2):
        if 0<lst[i]<=size and not deleted[i]:
            n=lst[i]
            deleted[i]=True
            return i//2,n
    return 0,0

sum_a=0
fileNo = 0      #bnu
pos = 0         #virtual position
last = len(lst)-1
deleted = [False]*len(lst)
for i in range(len(lst)):
    if i>=last+1:
        break
    length = lst[i]
    if isFile(i):
        fileNo = (i//2)
        for j in range(length):
            sum_a+=(j+pos)*fileNo
    else:
        for j in range(length):
            fileNo,last = takeFromEnd(last)
            sum_a+=(j+pos)*fileNo
    pos += length
print(sum_a)

#######################[ part2 ]##############################

lst = get_numgrid()[0]

sum_b=0
pos = 0         #virtual position
for i in range(len(lst)):
    length = lst[i]
    if isFile(i):
        fileNo = (i // 2)
        if not deleted[i]:
            for j in range(length):
                #print(j + pos, fileNo)
                sum_b+=(j+pos)*fileNo
    else:
        moved_size=0
        while moved_size<length:
            fileNo,act_size = findWholeFile(length-moved_size,i)
            if fileNo==0:
                break
            for j in range(act_size):
                #print(j+pos+moved_size,fileNo)
                sum_b+=(j+pos+moved_size)*fileNo
            moved_size += act_size
    pos += length
print(sum_b)