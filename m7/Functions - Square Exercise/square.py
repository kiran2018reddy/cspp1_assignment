# Exercise: square
# Write a Python function, square, that takes in one number and returns the square of that number.

# This function takes in one number and returns one number.


def square(x):
    '''
    x: int or float.
    '''
    # Your code here
    return int(x)**2
    
# Correct

def main():
	data = input() #2.3.4.5.6
	temp = str(data).split('.')
	data = list(map(square,temp))
	print(data)

if __name__== "__main__":
	main()

