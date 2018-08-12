"""Exercise: Assignment-2"""
def update_hand(hand_1, word_1):
    """a2"""
    hand_new = dict(hand_1)
    for i in word_1:
        if i in hand_1.keys():
            # key.append(i)
            # val = hand[i] - 1
            # value.append(val)
            hand_new[i] = hand_new[i] - 1
        # else:
        #     handnew[i] = handnew[i]
    #         key.append(i)
    #         value.append(hand[i])
    # hand = dict(zip(key, value))
    return hand_new
def main():
    """string"""
    n_1 = input()
    adict_1 = {}
    for i in range(int(n_1)):
        data = input()
        i = i
        l_1 = data.split(" ")
        adict_1[l_1[0]] = int(l_1[1])
    data1 = input()
    print(update_hand(adict_1, data1))
if __name__ == "__main__":
    main()
