# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
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
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # loop over our secret_word
    # for el in secret_word:
    #   print('el', el)
    #   matched = False
    #   # loop over our letters guessed
    #   for e2 in letters_guessed:
    #     print('el', e2)
    #     # if the two match then break out of this loop and search
    #     # the next in the secret_word.
    #     if el == e2:
    #       print('Letter is matched')
    #       matched = True
    #       break
    #     if not matched:
    #       print('Letter is not matched')
    #       return False
    
    #print('Matched status:', matched)
    
    # Return if all is true.
    #return True
    result = all(el in letters_guessed for el in secret_word)
    
    if result:
      return True
    else:
      return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ''

    for letter in secret_word:
      if letter not in letters_guessed:
        guessed_word += '_ '
      else:
        guessed_word += letter 

    return guessed_word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprise, 'r'd of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for letter in letters_guessed:
      if letter in alphabet:
        alphabet = alphabet.replace(letter, '', 1)
    
    return alphabet
    
def unique_letters(secret_word):
  '''
  secret_word: the word for which we are guessing
  returns: number of unique elements.
  '''
  temp = []
  for i in secret_word:
    if i not in temp:
      temp.append(i)

  return len(temp)

def hangman(secret_word):
  '''
  secret_word: string, the secret word to guess.
  
  Starts up an interactive game of Hangman.
  
  X At the start of the game, let the user know how many 
    letters the secret_word contains and how m>any guesses s/he starts with.
    
  X The user should start with 6 guesses

  X Before each round, you should display to the user how many guesses
    s/he has left and the letters that the user has not yet guessed.
  
  X Ask the user to supply one guess per round. Remember to make
    sure that the user puts in a letter!
  
  X The user should receive feedback immediately after each guess 
    about whether their guess appears in the compubreakter's word.

  * After each guess, you should display to thebreak
  
  Follows the other limitations detailed in the problem write-up.
  '''
  guesses = 6
  guessed_letters = []
  warnings = 3

  print('Welcome to HANGMAN')
  print('I am thinking of a word that is %d letters long.' % len(secret_word))
  print('----------')
  while guesses >= 1:
    print('You have %d guesses left.\nAvailable letters: %s.\n' % (guesses, get_available_letters(guessed_letters)))

    try:
      current_guess = input('Please guess a letter: ')
      
      if current_guess.isalpha():
        current_guess.lower
              
        if current_guess in secret_word and current_guess not in guessed_letters:

          guessed_letters.append(current_guess)
          print('Good guess: %s' % get_guessed_word(secret_word, guessed_letters))

          if is_word_guessed(secret_word, guessed_letters):
            print("CONGRATULATIONS! You won!")
            break
          guesses -= 1
        else:
          print("Oops! You've already guessed that letter.")
          if warnings > 0:
            warnings -= 1
            print('You have %d warnings remaining' % warnings)

          if warnings == 0:
            print('You have no warnings left so you lose one guess: %s' % get_guessed_word(secret_word, guessed_letters))
            guesses -= 1

        print('----------')

      else:
        raise TypeError

    except TypeError:
      print('You need to input a valid answer')
      if warnings > 0:
        warnings -= 1
        print('You have %d warnings remaining' % warnings)

      if warnings == 0:
        print('You are out of warnings. You lose a guess')
        guesses -= 1

  score = guesses * unique_letters(secret_word)
  print('Your total score for this game is: %d' % score)
  
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)
# -----------------------------------
# apples \ Match
# app___ / (Guessed 'ap' already)
# 
# foobar \ No Match
# app___ / (Guessed 'ap' already)
#
# apples \ No Match
# ap____ / (Guessed 'ap' already)
#
# apples \ No Match
# ______ / (Guessed 'a' already)
#
# 1  2  3     R
# a, a, ap => Good
# f, a, ap => Bad
# a, _, a  => Bad
# a, _, b  => Good

def compare(my_letter, other_letter, guessed_letters):
  ## Short code
  if my_letter == "_":
    # T  W  G
    # a, _, a  => Bad
    # a, _, b  => Good
    return other_letter not in guessed_letters
  # a, a, ap => Good
  # f, a, ap => Bad
  return my_letter == other_letter

def match_with_gaps_short(my_word, other_word, guessed_letters):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''

    word = list(my_word.replace(' ', ''))
    temp = list(other_word)

    # for value, letter in enumerate(word):
    for i in range(len(word)):
      if not compare(word[i], temp[i], guessed_letters):
        return False
    return True

# def match_with_gaps(my_word, other_word, guessed_letters):

#     word = list(my_word.replace(' ', ''))
#     temp = list(other_word)
#     count = 0
#     for i in range(len(word));
#       ## 'Truth table'
#       letters_match = word[i] == temp[i]
#       is_blank = word[i] == "_"
#       letter_in_guess  = temp[i] in guessed_letters

#       if letters_match:
#         pass
#       elif is_blank and letter_in_guess
#       elif is_blank and not letter_in_guess
#       else:

      

#       flag = True
#       if word[i] == temp[i]:
#         flag = True
#       elif word[i] != temp[i]:
#         flag = False
#       elif word[i] == "_" and temp[i] in guessed_letters:
#         flag = False
        
#     #   if letter == "_":
#     #     temp[value] = letter
#     #     count += 1
#     # if count == 1:
#     #   return
#     # if word == temp:
#     #   return True
#     # else:
#     #   return False

#     if flag = True:
#       return True

#     return False

def contains_letters(word, wrong_letters):
  '''
  word: string, the word to test
  wrong_letters: list, the list of letters to test the word against
  returns: True or False
  '''
  for letter in word:
    if letter in wrong_letters:
      return True
  return False

def show_possible_matches(my_word, wrong_letters, guessed_letters):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(range(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    length = len(secret_word)
    temp = []
    for word in wordlist:
      # ap_ _ es
      # apzxes <- Real
      # apples
      if len(word) == length and match_with_gaps_short(my_word, word, guessed_letters) and not contains_letters(word, wrong_letters):
        temp.append(word)

    if not temp:
      print('Nothing to suggest')
    else:
      print(' '.join(temp))

def hangman_with_hints(secret_word):
  '''
  secret_word: string, the secret word to guess.
  
  Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.    
    * The user should start with 6 guesses
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    * Ask the user to supply one guess per round. Make sure to check that
      the user guesses a letter
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the 
      partially guessed word so far.
    * If the guess is the symbol, print out all words in word list 
      that matches the current guessed word. 
  
  Follows the other limitations detailed in the problem write-up.
  '''

  guesses = 6
  guessed_letters = []
  wrong_letters = []
  warnings = 3

  print('Welcome to HANGMAN')
  print('I am thinking of a word that is %d letters long.' % len(secret_word))
  print('----------')

  while guesses >= 1:
    print('You have %d guesses left.\nAvailable letters: %s.' % (guesses, get_available_letters(guessed_letters)))
    current_guess = ''
    try:
      current_guess = input('Please guess a letter: ')
     
      if current_guess.isalpha():
        current_guess.lower

        if current_guess in secret_word:
          print('current_guess in secret_word')

          if  current_guess not in guessed_letters:
            guessed_letters.append(current_guess)
            print('Good guess: %s' % get_guessed_word(secret_word, guessed_letters))

            if is_word_guessed(secret_word, guessed_letters):
              print("CONGRATULATIONS! You won!")
              break
            guesses -= 1
          else:
            print("Oops! You've already guessed that letter.")
            if warnings > 0:
              warnings -= 1
              print('You have %d warnings remaining' % warnings)

            if warnings == 0:
              print('You have no warnings left so you lose one guess: %s' % get_guessed_word(secret_word, guessed_letters))
              guesses -= 1
        else:
          print('Oops that letter is not in my word: %s' % get_guessed_word(secret_word, guessed_letters))
          if current_guess not in wrong_letters:
            wrong_letters.append(current_guess)
          if warnings > 0:
            warnings -= 1
            print('You have %d warnings remaining' % warnings)

          if warnings == 0:
            print('You have no warnings left so you lose one guess: %s' % get_guessed_word(secret_word, guessed_letters))
            guesses -= 1

      elif current_guess == "*":
        show_possible_matches(get_guessed_word(secret_word, guessed_letters), wrong_letters, guessed_letters)
      else:
        print('You need to input a valid answer')
        if warnings > 0:
          warnings -= 1
          print('You have %d warnings remaining' % warnings)

        if warnings == 0:
          print('You are out of warnings. You lose a guess')
          guesses -= 1

    except TypeError:
      print('You need to input a valid answer')

  score = guesses * unique_letters(secret_word)
  print('Your total score for this game is: %d' % score)

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #secret_word = 'secret'
    #hangman(secret_word)

    ###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    secret_word = 'fire'
    hangman_with_hints(secret_word)
