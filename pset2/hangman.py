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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = ''.join(letters_guessed)
    if set(secret_word) == set(letters_guessed):
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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    empty = []
    for i in secret_word:
        empty += ['_ ']
        
    
    for i in range(len(letters_guessed)):
        for l in range(len(secret_word)):
            if letters_guessed[i] == secret_word[l]:
                empty[l] = letters_guessed[i]
    return ''.join(empty)


                
         


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letterstring = string.ascii_lowercase
    letterlist = list(letterstring)
    for i in letterstring:
        for s in letters_guessed:
            if i == s:
                letterlist.remove(i)
    return ''.join(letterlist)
                
    
                




def hangman(secret_word):
    '''
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
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    guess = ''
    list1 = []
    warnings = 3
    alllist = []
    vowels = ["a", "e", 'i', 'o']
    length = len(secret_word)
    #print(secret_word)
    print('Welcome to the Hangman game!')
    print("I'm thinking of a word that is {} letters long.".format(length))
    print("You have {} warnings left.".format(warnings))
    print("--------------------------")
   
   
            
            
  
    while (guesses > 0) and (not is_word_guessed(secret_word, list1)):
        print("You have {} guesses left.".format(guesses))
        print("Available letters:", get_available_letters(alllist), end='')
        guess = (input("Please guess a letter: ")).lower()
        
       
        
        if (guess in secret_word) and (guess != '') and (guess not in alllist):
            list1.append(guess)
            print('Good guess:', get_guessed_word(secret_word, list1))
        
        
        elif guess not in string.ascii_lowercase or guess == '':
            if warnings == 0:
                guesses -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, list1))
                
            else:
                warnings -= 1
                print("Oops! That is not a valid letter. You have {} warnings left:".format(warnings), get_guessed_word(secret_word, list1))
           
        
        elif guess in alllist:
            if warnings == 0:
                guesses -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, list1))  
            else:
                warnings -= 1
                print("Oops! You've already guessed that letter. You now have {} warnings:".format(warnings), get_guessed_word(secret_word, list1))  
           
                                                                                                                         
        else:
            if guess in vowels:
                guesses -= 2
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, list1))
            else:    
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, list1))
                guesses -= 1
                
        
        print('--------------------------')
        if guess not in alllist:
            alllist.append(guess)
    
    unique = len(set(secret_word))
    total_score = guesses * unique
    if is_word_guessed(secret_word, list1):
        print("Congratulations, you won!")
        print("Your total score for this game is:", total_score)
    else:
        print("Sorry, you ran out of guesses. The word was {}.".format(secret_word))
            
       
    

   



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    mywordlist = list(my_word)
    for i in my_word:
        if i == " ":
            mywordlist.remove(i)
    
    new_my_word = ''.join(mywordlist)
    count = 0
    letter_count = 0
   
    for i in new_my_word:
        if i != "_":
            letter_count += 1
   
    if len(new_my_word) == len(other_word):
        for i in range(len(new_my_word)):
            if new_my_word[i] != "_":
                if new_my_word[i] == other_word[i]:
                    count += 1
    
    our_letter = []
    if len(new_my_word) == len(other_word):
        for i in range(len(new_my_word)):
            if new_my_word[i] == '_':
                our_letter.append(other_word[i])
        
        for i in our_letter:
            for s in new_my_word:
                if i == s:
                    return False
            
    
    if count == letter_count:
        return True
            
    else:
        return False



def show_possible_matches(my_word):
    """ my_word: string with _ characters, current guess of secret word
        returns: nothing, but should print out every word in wordlist that matches my_word
                 Keep in mind that in hangman when a letter is guessed, all the positions
                 at which that letter occurs in the secret word are revealed.
                 Therefore, the hidden letter(_ ) cannot be one of the letters in the word
                 that has already been revealed."""
        # FILL IN YOUR CODE HERE AND DELETE "pass"
    counter = 0    
    for i in wordlist:
        if match_with_gaps(my_word, i):
            print(i)
            counter += 1
    if counter == 0:
        print("No matches found")



def hangman_with_hints(secret_word):
    '''
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
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    guess = ''
    list1 = []
    warnings = 3
    alllist = []
    vowels = ["a", "e", 'i', 'o']
    length = len(secret_word)
    #print(secret_word)
    print('Welcome to the Hangman game!')
    print("I'm thinking of a word that is {} letters long.".format(length))
    print("You have {} warnings left.".format(warnings))
    print("--------------------------")
   
   
            
            
  
    while (guesses > 0) and (not is_word_guessed(secret_word, list1)):
        print("You have {} guesses left.".format(guesses))
        print("Available letters:", get_available_letters(alllist), end='')
        guess = (input("Please guess a letter: ")).lower()
        
        if guess == "*":
            show_possible_matches(get_guessed_word(secret_word, list1))
        
        elif (guess in secret_word) and (guess != '') and (guess not in alllist):
            list1.append(guess)
            print('Good guess:', get_guessed_word(secret_word, list1))
        
        
        elif guess not in string.ascii_lowercase or guess == '':
            if warnings == 0:
                guesses -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, list1))
                
            else:
                warnings -= 1
                print("Oops! That is not a valid letter. You have {} warnings left:".format(warnings), get_guessed_word(secret_word, list1))
           
        
        elif guess in alllist:
            if warnings == 0:
                guesses -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, list1))  
            else:
                warnings -= 1
                print("Oops! You've already guessed that letter. You now have {} warnings:".format(warnings), get_guessed_word(secret_word, list1))  
           
                                                                                                                         
        else:
            if guess in vowels:
                guesses -= 2
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, list1))
            else:    
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, list1))
                guesses -= 1
                
        
        print('--------------------------')
        if guess not in alllist:
            alllist.append(guess)
    
    unique = len(set(secret_word))
    total_score = guesses * unique
    if is_word_guessed(secret_word, list1):
        print("Congratulations, you won!")
        print("Your total score for this game is:", total_score)
    else:
        print("Sorry, you ran out of guesses. The word was {}.".format(secret_word))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
