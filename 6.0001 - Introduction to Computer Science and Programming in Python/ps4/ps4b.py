# Problem Set 4B
# Name: Robert Forbes
# Collaborators: None
# Time Spent: 

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'
ASCII_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''

        result = dict()
        ascii = list(ASCII_LETTERS)

        # a = ASCII_LETTERS + ASCII_LETTERS
        # result = dict(zip(ASCII_LETTERS, a[shift:]))

        # for letter in result:
        #     a = ord(letter) + 40
        #     b = chr(a)
        #     result[letter] = b
        # print('RESULT', result)

        # ascii = list(ASCII_LETTERS)

        # results = []

        # for j in ascii:
        #     results[j] = shift(j, shift)

        # return result

        # Loop over the list and shift by x
        for i in range(shift):
            ascii.append(ascii.pop(0))

        for i in range(len(ASCII_LETTERS)):
            result[ASCII_LETTERS[i]] = ascii[i]

        return result

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        dictionary = self.build_shift_dict(shift)

        result = ''

        for letter in self.get_message_text():
            if letter.isalpha() == False:
                result += letter
            else:
                if letter.isupper():
                    new_letter = dictionary.get(letter.lower())
                    result += new_letter.upper()
                else:
                    result += dictionary.get(letter)

        return result

    def apply_shift_for_encryption():
        pass

    def apply_shift_for_decryption():
        pass

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''

        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''

        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)



class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = str(text)
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''

        # break message in to words.
        wordlist = self.get_valid_words()

        best_shift = 0
        best_count = 0

        # test word against each offset (below 26)
        for i in range(26):
            words = self.apply_shift(26 - i)
            words = words.split()
            
            count = 0
           
            for word in words:
                if is_word(wordlist, word):
                    count += 1

            if count > best_count:
                best_shift = i
                best_count = count
        
        plain_text = self.apply_shift(best_shift)
        return (best_shift, plain_text)


if __name__ == '__main__':
    plaintext = PlaintextMessage('abcdef', 2)
    print('Plaintext Input: abcdef')
    print('Expected Output: cdefgh')
    print('Actual Output:  ', plaintext.get_message_text_encrypted())

    plaintext = PlaintextMessage('Hello, World!', 4)
    print('Plaintext Input: Hello, World!')
    print('Expected Output: Lipps, Asvph!')
    print('Actual Output:  ', plaintext.get_message_text_encrypted())

    plaintext = PlaintextMessage('My Name is all, how are you?', 10)
    print('Plaintext Input: My Name is all, how are you?')
    print('Actual Output:  ', plaintext.get_message_text_encrypted())

    plaintext = PlaintextMessage('What is going on here.', 17)
    print('Plaintext Input: What is going on here')
    print('Actual Output:  ', plaintext.get_message_text_encrypted())

    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:  ', ciphertext.decrypt_message())

    ciphertext = CiphertextMessage('Nyrk zj xfzex fe yviv.')
    print('Expected Output:', (17, 'What is going on here'))
    print('Actual Output: ',  ciphertext.decrypt_message())

    ciphertext = CiphertextMessage('Wi Xkwo sc kvv, ryg kbo iye?')
    print('Expected Output:', (10, 'My Name is all, how are you?'))
    print('Actual Output:  ', ciphertext.decrypt_message())

    story =  get_story_string()
    ciphertext = CiphertextMessage(story)
    print('Unencrypted story:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE
    #TODO: best shift value and unencrypted story 
    