"""game"""
def get_word_score(word_1, n_1):
    """string"""
    # import string
    # key = list(string.ascii_lowercase)
    # value = []
    # x=1
    sum_1 = 0
    # for i in range(0, 26):
    #     value.append(x)
    #     x+=1
    # dictionary_ = dict(zip(key, value))
    # print(dictionary_)
    dictionary_ = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
    length_1 = len(word_1)
    # if length_1 <= n_1:
    for i in word_1:
        if i in dictionary_.keys():
            sum_1 = sum_1 + dictionary_[i]
    sum_1 = sum_1*length_1
    if n_1 == length_1:
        sum_1 += 50
    return sum_1
    # print("worng inputs")
def main():
    '''
    Main function for the given problem
    '''
    data = input()
    data = data.split(" ")
    print(get_word_score(data[0], int(data[1])))
if __name__ == "__main__":
    main()
