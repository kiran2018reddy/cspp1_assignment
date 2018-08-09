"""secrate word"""
def get_guessed_word(secret_word, letters_guessed):
    """guess"""
    l_1 = len(secret_word)
    l_2 = len(letters_guessed)
    a_str = ""
    for i in range(l_1):
        cou = 0
        for k in range(l_2):
            if secret_word[i] == letters_gussed[k]:
                cou = cou + 1
                if cou == 1:
                    a_str = a_str + secret_word[i]
                break
        if cou == 0:
            a_str = a_str + '_'
    return a_str
def main():
    '''
    Main function for current assignment
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
    print(get_guessed_word(secret_word, list1))

if __name__ == "__main__":
    main()
