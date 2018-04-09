"""
file: word_play.py
author: Ayush Rout
Test file: test_words.txt
github: https://github.com/cloudkayl
description:
"""

#program starts here

def check_deletions(word, dic):
    """
       func: check_deletions()
       description: Takes a given word, and scans a dictionary for similar words.
       In this case, similar words are the same word, with a single letter removed
       It returns number of matches found with similar words
    """
    del_word = ""
    del_amt = 0
    if len(word)>1:
        for line in dic:
            """
            This will continue computations if either the first or second line of the input word
            matches the first letter of the line so that only the words that is similar will get 
            checked
            """
            if word[0] == line[0] or word[1] == line[0]:
                for i in range(1,len(word)+1):
                    last_word = del_word
                    del_word = word[:i-1] + word[i:]
                    """
                    If the current deletion word is the same as the last, don't check it again
                    similar words will always be next to each other. 
                    """
                    if del_word != last_word:
                        if del_word == line.strip():
                            del_amt += 1
                            print(del_amt, " ", del_word)
    return del_amt


def word_prompt():
    """
    func: user_word()
    description: Gets user input for the word they want to deletion check against the dictionary
    """
    w = ""
    while w == "":
        w = input("Please enter a word you would like to check for deletion similarities " 
                  "OR type quit to exit: ")
    return w


def file_prompt():
    """
    func: file_user()
    description: It asks user for the dictionary file. If the file is not valid or not found,
    it asks again
    """
    f = ""
    while f == "":
        f = input("Please enter a dicionary file you'd like to check your deletion words against: ")
        if not(f.endswith(".txt")):
            f = ""
    return f


if __name__ == '__main__':
    """
    main function contains all the function calls, user prompts and user interactive prints
    """
    while True:
        word = word_prompt()
        if word == "quit":
            break
        dic = file_prompt()
        print("You entered the word: ", word)
        fd = open(dic)
        print("Number of deletion words in dictionary:", check_deletions(word,fd), "\n")
        fd.close()


#program ends here


"""
Program tests:

Please enter a word you would like to check for deletion similarities OR type quit to exit: masters
Please enter a dicionary file you'd like to check your deletion words against: test_words.txt
You entered the word:  masters
1   asters
2   masers
3   master
4   maters
Number of deletion words in dictionary: 4 

Please enter a word you would like to check for deletion similarities OR type quit to exit: phone
Please enter a dicionary file you'd like to check your deletion words against: test_words.txt
You entered the word:  phone
1   hone
2   phon
3   pone
Number of deletion words in dictionary: 3 

Please enter a word you would like to check for deletion similarities OR type quit to exit: hello
Please enter a dicionary file you'd like to check your deletion words against: test_words.txt
You entered the word:  hello
1   hell
Number of deletion words in dictionary: 1 

Please enter a word you would like to check for deletion similarities OR type quit to exit: check
Please enter a dicionary file you'd like to check your deletion words against: test_words.txt
You entered the word:  check
1   heck
Number of deletion words in dictionary: 1 

Please enter a word you would like to check for deletion similarities OR type quit to exit: how
Please enter a dicionary file you'd like to check your deletion words against: test_words.txt
You entered the word:  how
1   ho
2   ow
Number of deletion words in dictionary: 2 

Please enter a word you would like to check for deletion similarities OR type quit to exit: red
Please enter a dicionary file you'd like to check your deletion words against: test_words.txt
You entered the word:  red
1   ed
2   re
Number of deletion words in dictionary: 2 

Please enter a word you would like to check for deletion similarities OR type quit to exit: sddssd
Please enter a dicionary file you'd like to check your deletion words against: test_words.txt
You entered the word:  sddssd
Number of deletion words in dictionary: 0 
"""





"""
Author: Ayush Rout
File: word_play.py
language: Python3
email: axr6077@rit.edu
"""
