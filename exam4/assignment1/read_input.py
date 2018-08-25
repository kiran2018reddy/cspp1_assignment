'''
Write a python program to read multiple lines of text input and store the input into a 
string.
'''

def main():
	lines=[]
	while True:
		line = input()
		if line:
			lines.append(line)
		else:
			break
	text = '\n'.join(lines)


if __name__ == '__main__':
    main()
