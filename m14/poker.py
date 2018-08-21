"""kindof"""
def kind(face_values, num):
    """returning face values"""
    for face in face_values:
        if face_values.count(face) == num:
            return face
def get_facevalues(hand):
    """facevalues"""
    return sorted(['--23456789TJQKA'.index(face) for face, suite in hand], reverse = True)
def is_straight(hand):
    """straight"""
    face_values = get_facevalues(hand)
    if face_values == [14, 5, 4, 3, 2]:
        face_values = [5, 4, 3, 2, 1]
    set_facevalues = set(face_values)
    return (len(set_facevalues) == 5) and ((max(set_facevalues) - min(set_facevalues)) == 4)
def is_flush(hand):
    """flush"""
    set_ = set([suite for face, suite in hand])
    return len(set_) == 1
def hand_rank(hand):
    """handrank"""
    face_values = get_facevalues(hand)
    return ((8, face_values) if is_flush(hand) and is_straight(hand) else
            (7, kind(face_values, 4), face_values) if kind(face_values, 4) else
            (6, kind(face_values, 3), kind(face_values, 2)) 
            if  kind(face_values, 3) and kind(face_values, 2) else
            (5, face_values) if is_flush(hand) else
            (4, face_values) if is_straight(hand) else
            (3, kind(face_values, 3), face_values) if kind(face_values, 3) else
            (2, kind(face_values, 2), kind(sorted(face_values), 2), face_values)
            if kind(face_values, 2) and kind(sorted(face_values), 2) else
            (1, kind(face_values, 2), face_values) if kind(face_values, 2) else
            (0, face_values))
def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)
if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        # print(x)
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
        # print(HANDS)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
