'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secret_word 
the user is to guess. This starts up an interactive game of Hangman between 
the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.
'''

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist
def isWordGuessed(secret_word, letters_guessed):
    """guess"""
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True
def getGuessedWord(secret_word, letters_guessed):
    """string"""
    list_1 = list(secret_word)
    length_1 = len(secret_word)
    astr = ""
    for i in range(length_1):
        count = 0
        for j in letters_guessed:
            if j == list_1[i]:
                count = 1
        if count == 1:
            astr = astr + list_1[i]
        else:
            astr = astr + '_'
    return astr
def getAvailableLetters(letters_guessed):
    """dictionary"""
    import string
    x_1 = ""
    key_ = list(string.ascii_lowercase)
    value_ = key_
    dictionary_ = dict(zip(key_, value_))
    for i in letters_guessed:
        if i in dictionary_.values():
            del dictionary_[i]
    for v_1 in dictionary_.values():
        x_1 = x_1 + v_1
    return x_1


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def hangman(secret_word):
    word_size = len(secret_word)
    guess_string = ""
    print("The letter contains ",word_size)
    available_guess = word_size
   
    # letters_filled = getAvailableLetters(guess_character)
    # print("The letters filled are",letters_filled)
    while (available_guess > 0):   
        guess_character = input("Enter a character ")
        guess_string = guess_string + guess_character
        if guess_character in secret_word:
            print("You guessed it right")
            print(getGuessedWord(secret_word, guess_string))
            print(getAvailableLetters(guess_string))
        else:
            available_guess -= 1
            print("wrong guess")
            print("number of guesses are:",available_guess)
            print(getGuessedWord(secret_word, guess_string))
            print(getAvailableLetters(guess_string))

    if isWordGuessed(secret_word, guess_string) == True:
        print('yes')
    else:
        print('The word is ',secret_word)






    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...




def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secret_word while you're testing)
    '''
    secret_word = chooseWord(wordlist).lower()
    hangman(secret_word)
if __name__ == "__main__":
    main()
