'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord 
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

def isWordGuessed(secretWord, letters_gussed):
    for i in secretWord:
    	if i not in letters_gussed:
    		return False
    return True
def getGuessedWord(secretWord, letters_gussed):
    k = []
    for i in secretWord:
    	if i in letters_gussed:
    		k.append(i)
    	else:
    		k.append("_")
    return "".join(k)
def getAvailableLetters(letters_gussed):
    import string
    a = ""
    key1 = list(string.ascii_lowercase)
    val1 = key1
    dic1=dict(zip(key1, val1))
    for i in letters_gussed:
    	if i in dic1.values():
    	    del dic1[i]
    for j in dic1.values():
        a = a + dic1[j]
    return a






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

def hangman(secretWord):
    available_guess = len(secretWord)+5
    letters_gussed=[]
    while available_guess > 0 and not isWordGuessed(secretWord, letters_gussed):
        char = input("give a character")
        if char in letters_gussed:
            print("already guessed")
            continue
        letters_gussed.append(char)
        if char in secretWord:
            letters_gussed += char
            print("guess is right")
            print(getGuessedWord(secretWord, letters_gussed))
            print(getAvailableLetters(letters_gussed))
        else:
            available_guess = available_guess - 1
            print(getAvailableLetters(letters_gussed))
            print("guess is wrong")
            print("number of guesses available : ", available_guess)

    # if isWordGuessed(secretWord, letters_gussed) == True
    #     print("game over") 










    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    pass



def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
	and run this file to test! (hint: you might want to pick your own
	secretWord while you're testing)
	'''
	# secretWord = chooseWord(wordlist).lower()
	# hangman(secretWord)
    secret_word = chooseWord(wordlist).lower()
    hangman(secret_word)
if __name__ == "__main__":
    main()
