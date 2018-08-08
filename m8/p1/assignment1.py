# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number and returns the factorial of given number.

# This function takes in one number and returns one number.


def factorial(n_1):
    """fact"""
    if n_1 in (0, 1):
        return 1
    return n_1 * factorial(n_1-1)
def main():
    """fact"""
    a = input()
    print(factorial(int(a)))    
if __name__== "__main__":
    main()
