#Exercise : how many
# write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary.


def how_many(aDict):
    print(aDict)
    l = 0
    for i in aDict:
        print(i)
        for j in aDict[i]:
            print(j)
            l = l + 1
    return l
def main():
	n=input()
	aDict={}
	for i in range(int(n)):
		s=input()
		l=s.split()
		if l[0][0] not in aDict:
			aDict[l[0][0]]=[l[1]]
		else:
			aDict[l[0][0]].append(l[1])
	print(how_many(aDict))

if __name__== "__main__":
    main()
