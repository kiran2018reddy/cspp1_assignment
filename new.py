L = [[1,2,3],[3,4],"abc"]
L.reverse()
le = len(L)
lnew = []
print(le)
for i in L:
    if type(i) == str:
        i = i[::-1]
        lnew.append(i)
    if type(i) == list:
        i.reverse()
        lnew.append(i)
print(lnew)