from get_src import get

inp = get()

def swap(a,b):
    printlist[a], printlist[b] = printlist[b], printlist[a]

pages={}
sum_a = 0
sum_b = 0
for i in inp.splitlines():
    if "|" in i:
        before,after = i.split("|")
        if int(before) in pages:
            pages[int(before)].append(int(after))
        else:
            pages[int(before)]=[int(after)]
    elif "," in i:
        printlist = i.split(",")
        printlist = list(map(int,printlist))
        list_ok=True
        for i in range(len(printlist)):
            if printlist[i] in pages:
                for j in pages[printlist[i]]:
                    if j in printlist:
                        idx2 = printlist.index(j)
                        if idx2<i:
                            #print(f"{j} should come after {printlist[i]}")
                            list_ok=False
        if list_ok:
            sum_a += printlist[len(printlist)//2]
        else:
            final=False
            while not final:
                final = True
                for i in range(len(printlist)):
                    if printlist[i] in pages:
                        for j in pages[printlist[i]]:
                            if j in printlist:
                                idx2 = printlist.index(j)
                                if idx2<i:
                                    #print(f"{j} should come after {printlist[i]}")
                                    swap(idx2,i)
                                    final=False
            sum_b += printlist[len(printlist) // 2]

print(sum_a)
print(sum_b)
