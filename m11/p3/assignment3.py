"""comment"""
def is_valid_word(word_1, hand_1, word_list):
    """string"""
    if word_1 not in word_list:
        return False
    for i_1 in word_1:
        if i_1 not in hand_1.keys():
            return False
    return True
def main():
    """string"""
    word_1 = input()
    n_1 = int(input())
    adict_1 = {}
    for i in range(n_1):
        data = input()
        i = i+1
        i = i-1
        l_1 = data.split()
        adict_1[l_1[0]] = int(l_1[1])
    l_2 = input().split()
    print(is_valid_word(word_1, adict_1, l_2))
if __name__ == "__main__":
    main()
