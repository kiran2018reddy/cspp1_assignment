'''
Exercise : Assignment-1
implement the function get_available_letters that takes in one parameter -
a list of letters, letters_guessed. This function returns a string
that is comprised of lowercase English letters - all lowercase English letters
that are not in letters_guessed
'''

def get_available_letters(letters_guessed):
    import string
    k = ""
    key1 =list(string.ascii_lowercase)
    val1 = key1
    dic1 = dict(zip(key1, val1))
    for i in letters_guessed:
        if i in dic1.values():
            del dic1[i]
    for j in dic1.values():
            k = k + dic1[i]
    return k



        



def main():
    '''
    Main function for the given program
    '''
    user_input = input()
    user_input = user_input.split()
    data = []
    for char in user_input:
        data.append(char[0])
    print(get_available_letters(data))


if __name__ == "__main__":
    main()
