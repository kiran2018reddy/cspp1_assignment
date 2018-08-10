"""guess"""
def is_word_guessed(secret_word, letters_guessed):
    """secret"""
    cou = 0
    l_1 = len(secret_word)
    l_2 = len(letters_guessed)
    for i in range(l_1):
        for k in range(l_2):
            if secret_word[i] == letters_guessed[k]:
                cou = cou + 1
    return bool(cou == len(secret_word))
    # for i in secret_word:
    # 	if i not in letters_guessed:
    # 		return False
    # return True
def main():
    """secret"""
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
