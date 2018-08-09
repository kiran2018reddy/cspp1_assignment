# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number and returns the sum of digits of given number.

# This function takes in one number and returns one number.


def sumofdigits(n):
    '''sum'''
    if n <= 0:
    	return 0
    r = n % 10
    return r+sumofdigits(n//10)
    
  
def main():
    '''sum'''
    a = input()
    print(sumofdigits(int(a)))  
if __name__== "__main__":
    main()
