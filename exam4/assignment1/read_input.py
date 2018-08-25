'''
Write a python program to read multiple lines of text input and store the input into a 
string.
'''

def main():
    lines = []
    while True:
        given =input(" ")
        if given:
            lines.append(given)
        else:
            break
    return "lines"
    
  


if __name__ == '__main__':
    main()
