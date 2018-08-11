'''
Exercise : Assignment-1
implement the function get_available_letters that takes in one parameter -
a list of letters, letters_guessed. This function returns a string
that is comprised of lowercase English letters - all lowercase English letters
that are not in letters_guessed
'''

def get_available_letters(letters_guessed):
    """
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    Method 1:
    B = set(string.ascii_lowercase).intersection(set(letters_guessed))
    return(set(string.ascii_lowercase)-B)
    Method 2:
    A = list(string.ascii_lowercase)
    for i in letters_guessed:
        A.remove(i)
    return "".join(A)
    """
    import string
    keys = list(string.ascii_lowercase)
    ascii_val = []
    for i in keys:
        ascii_val.append(ord(i))
    dictionary = dict(zip(keys, ascii_val))
    for i in letters_guessed:
        del dictionary[i]
    list_1 = []
    for i in dictionary.keys():
        list_1.append(i)
    return "".join(list_1)
def main():
    '''
    Main function for the given program
    '''
    user_input = input()
    user_input = user_input.split()
    data = []
    for char in user_input:
        data.append(char)
    print(get_available_letters(data))


if __name__ == "__main__":
    main()
