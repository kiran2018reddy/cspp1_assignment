'''
Write a python program to read multiple lines of text input and store the input into a 
string.
'''

def main():
    lines=" "
    while True:
        try:
            line = input()
        except error:
            break
        lines.append(line)
    return lines


if __name__ == '__main__':
    main()
