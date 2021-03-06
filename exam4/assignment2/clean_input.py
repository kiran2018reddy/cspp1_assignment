'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    return "".join([i for i in string if i.isalpha() or ord(i) in range(48, 58)])
def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
