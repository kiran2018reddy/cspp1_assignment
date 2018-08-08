#Exercise : Odd Tuples
#Write a python function oddTuples(aTup) that takes a some numbers in the tuple as input and returns a tuple in which contains odd index values in the input tuple  



def oddTuples(aTup):
    """odd"""
    l = len(aTup)
    xtup=()
    for i in range(0, l, 2):
        xtup = xtup + (aTup[i],)
    return xtup        
def main():
    data = input()
    data = data.split()
    aTup=()
    for j in range(len(data)):
        aTup += ((data[j]),)
    print(oddTuples(aTup))
        

if __name__ == "__main__":
    main()