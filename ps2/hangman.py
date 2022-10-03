# Problem Set 2, hangman.py
# Name: Madhura Baxi

# Hangman Game

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    infile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = infile.readline()
    # wordlist: list of strings
    word_list = line.split()
    print("  ", len(word_list), "words loaded.")
    return word_list


def choose_word(word_list):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(word_list)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    return all((letter in letters_guessed) for letter in word)


def get_guessed_word(word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    guessed_word = ""
    for letter in word:
        if letter in letters_guessed:
            guessed_word = guessed_word + letter
        else:
            guessed_word = guessed_word + "_ "
    return guessed_word


def get_available_letters(letters_guessed):

    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
    yet been guessed.
    """
    all_letters = string.ascii_lowercase
    for letter in letters_guessed:
        idx = all_letters.find(letter)
        all_letters = all_letters.replace(all_letters[idx], "")
    return all_letters


def hangman(word):
    """
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    """

    word_length = len(word)
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ', word_length, ' letters long.')
    print('-------------------')

    letters_guessed = list("")
    guessed_word = '_ ' * word_length
    warning_remaining = 3
    vowels = ['a', 'e', 'i', 'o', 'u']

    print('You have ', warning_remaining, 'warnings left')

    guesses_remaining = 6
    while guesses_remaining > 0:
        print('You have ', guesses_remaining, ' guesses left')
        available_letters = get_available_letters(letters_guessed)
        print('Available letters: ', available_letters)
        letter = input('Please guess a letter: ')

        if not letter.isalpha():
            if warning_remaining > 0:
                warning_remaining = warning_remaining - 1
                print('Oops! That is not a valid letter. You have ', warning_remaining, ' warnings left: ',
                      guessed_word)
            else:
                print('Oops! That is not a valid letter. You have no warnings left so you lose one guess: ',
                      guessed_word)
                guesses_remaining = guesses_remaining - 1

        else:

            letter = letter.lower()
            if letter in letters_guessed:
                if warning_remaining > 0:
                    warning_remaining = warning_remaining - 1
                    print('Oops! You have already guessed that letter. You now have ', warning_remaining, 'warnings: ',
                          guessed_word)
                else:
                    print('Oops! You have already guessed that letter. You have no warnings left '
                          'so you lose one guess: ', guessed_word)
                    guesses_remaining = guesses_remaining - 1
            else:
                letters_guessed.append(letter)
                guessed_word = get_guessed_word(word, letters_guessed)
                if letter in word:
                    print('Good guess: ', guessed_word)
                else:
                    if letter in vowels:
                        print('Oops! That letter is not in my word: ', guessed_word)
                        guesses_remaining = guesses_remaining - 2
                    else:
                        print('Oops! That letter is not in my word: ', guessed_word)
                        guesses_remaining = guesses_remaining - 1
        print('-------------------')
        if is_word_guessed(word, letters_guessed):
            # Total score = guesses_remaining * number unique letters in secret_word
            total_score = guesses_remaining * len(set(word))
            print('Congratulations, you won!')
            print('Your total score for this game is: ', total_score)
            return

    print('Sorry, you ran out of guesses. The word was: ', word)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    """
    my_word = my_word.replace(" ", "")

    if len(my_word) == len(other_word):
        for idx in range(0, len(other_word)):
            if other_word[idx] == my_word[idx] or my_word[idx] == "_":
                if my_word[idx] == "_" and other_word[idx] in my_word:
                    return False
            else:
                return False
        return True
    else:
        return False


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """
    possible_matches = list()
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            possible_matches.append(other_word)

    if len(possible_matches) == 0:
        print('No matches found')
    else:
        print(possible_matches)


def hangman_with_hints(word):
    """
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    """
    word_length = len(word)
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ', word_length, ' letters long.')
    print('-------------------')

    letters_guessed = list("")
    guessed_word = '_ ' * word_length
    warning_remaining = 3
    vowels = ['a', 'e', 'i', 'o', 'u']

    print('You have ', warning_remaining, 'warnings left')

    guesses_remaining = 6
    while guesses_remaining > 0:
        print('You have ', guesses_remaining, ' guesses left')
        available_letters = get_available_letters(letters_guessed)
        print('Available letters: ', available_letters)
        letter = input('Please guess a letter: ')

        if not letter.isalpha() and not letter == '*':
            if warning_remaining > 0:
                warning_remaining = warning_remaining - 1
                print('Oops! That is not a valid letter. You have ', warning_remaining, ' warnings left: ',
                      guessed_word)
            else:
                print('Oops! That is not a valid letter. You have no warnings left so you lose one guess: ',
                      guessed_word)
                guesses_remaining = guesses_remaining - 1

        elif letter == '*':
            print('Possible word matches are:')
            show_possible_matches(guessed_word)

        else:

            letter = letter.lower()
            if letter in letters_guessed:
                if warning_remaining > 0:
                    warning_remaining = warning_remaining - 1
                    print('Oops! You have already guessed that letter. You now have ', warning_remaining, 'warnings: ',
                          guessed_word)
                else:
                    print('Oops! You have already guessed that letter. You have no warnings left '
                          'so you lose one guess: ', guessed_word)
                    guesses_remaining = guesses_remaining - 1
            else:
                letters_guessed.append(letter)
                guessed_word = get_guessed_word(word, letters_guessed)
                if letter in word:
                    print('Good guess: ', guessed_word)
                else:
                    if letter in vowels:
                        print('Oops! That letter is not in my word: ', guessed_word)
                        guesses_remaining = guesses_remaining - 2
                    else:
                        print('Oops! That letter is not in my word: ', guessed_word)
                        guesses_remaining = guesses_remaining - 1
        print('-------------------')
        if is_word_guessed(word, letters_guessed):
            # Total score = guesses_remaining * number unique letters in secret_word
            total_score = guesses_remaining * len(set(word))
            print('Congratulations, you won!')
            print('Your total score for this game is: ', total_score)
            return

    print('Sorry, you ran out of guesses. The word was: ', word)

if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    # secret_word = 'apple'
    hangman_with_hints(secret_word)
