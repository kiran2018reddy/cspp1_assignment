#Exercise : Function and Objects Exercise-1
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 4, 8, 9]


def apply_to_each(L, f):
    L1=()
    for i in range(len(L)):#taking total range
        L[i]=f(L[i])#converting -ve to +ve
        L1 =L1 + (L[i],)#adding numbers to mty
    return L1

def main():
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    x = apply_to_each(list1, abs)
    print (x)

if __name__ == "__main__":
    main()
