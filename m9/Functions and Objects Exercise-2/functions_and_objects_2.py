#Exercise : Function and Objects Exercise-2
#Implement a function that converts the given testList = [1, -4, 8, -9] into [2, -3, 9, -8]
def inc(x):
    x = x+1
    return x
def apply_to_each(L, f):
    L1 = ()
    for i in L:
        L1 = L1 + (f(i),)
    return L1
def main():
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    x = apply_to_each(list1, inc)
    print(x)
if __name__ == "__main__":
    main()