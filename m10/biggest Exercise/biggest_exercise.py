#Exercise : Biggest Exercise
#Write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.


def biggest(aDict):
    '''biggest'''
    max = 0
    y = []
    for i in aDict:
    	b = len(aDict[i])
    	if b>max:
    		max=b
    for i in aDict:
    	if len(aDict[i]) == max:
            y += i
    return y
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
	print(biggest(aDict))

if __name__== "__main__":
    main()