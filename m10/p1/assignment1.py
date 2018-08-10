'''sttring'''
def is_word_guessed(secret_word, letters_guessed):
    '''dic'''
    import string
    s1_ = ''
    key1 = list(string.ascii_lowercase)
    val1 = key1
    dic1 = dict(zip(key1, val1))
    for i in letters_guessed:
        if i in dic1.values(): 
            del dic1[i]
    for j in dic1.values():
        s1_ = s1_ + dic1[j]
    return s1_
def main():
    '''
    Main function for the program
    '''
    user_input = input()
    if user_input:
        data = user_input.split()
        secret_word = data[0]
    else:
        data = []
        secret_word = ""
    list1 = []
    for j in range(1, len(data)):
        list1.append(data[j][0])
    print(is_word_guessed(secret_word, list1))

if __name__ == "__main__":
    main()
