"""
file: anagram.py
author: Ayush Rout
github: https://github.com/cloudkayl
description: this program does four tasks:
             1. Reads a dictionary file and stores anagrams of every word in a variable 
             2. returns all anagrams in dict for a string 
             3. Finds the word of length <(user input)> that has the most english anagrams of it
             4. Finds how many "good" jumbled words are there for words of a certain length
"""


#program starts here

def sort(list):
    """
    sorts the list using insertion sort
    :param list: the list of characters to be sorted in alphabetical order
    :return: NONE
    """
    for idx in range(1, len(list)):
        temp = list[idx]
        k = idx
        while k > 0 and temp < list[k-1]:
            list[k] = list[k-1]
            k = k-1
        list[k] = temp


def create_lexico(str):
    """
    creates a lexicographical ordering that can be used as a dictionary hash code.
    This hash code is alphabetically sorted version of the word
    :param str: the word we want to find the lexicographical order of
    :return: a string/word in lexicographical order of the passed string
    """
    a = []
    b = ""
    for c in str:
        a.append(c.lower())
    sort(a)
    for c in a:
        b = b + c
    return b


def add_word(m, n):
    """
    Adds words to our dictionary. If a string with the same key already exists, the new word is
    added to this same key
    :param m: dictionary
    :param n: the word being added to dictionary
    :return: NONE
    """
    l = create_lexico(n)
    if l in m:
        m[l] = m[l] + [n]
    else:
        m[l] = [n]


def taskOne(f):
    """
    Reads a dictionary file and stores anagrams of every word in a variable dict
    :param f: the text file we want to read the word list from
    :return: the dict variable containing anagrams and list of words in dictionary
    """
    dict = {}
    wl = []
    for line in open(f):
        l = line.strip()
        wl.append(l)
        add_word(dict, l)
    return dict, wl


def taskTwo(t, dict):
    """
    returns all anagrams in dict for a string s
    :param t: the string for which we finding anagrams of
    :param dict: dictionary of anagrams loaded from the text dictionary file
    :return: all anagrams in dict for a string s
    """
    if create_lexico(t) in dict:
        return dict[create_lexico(t)]
    else:
        return None


def taskThree(m, dict):
    """
    Finds the word of length 'm'(user input) that has the most english anagrams of it
    :param m: length of the word
    :param dict: dictionary file of the words and their anagrams
    :return: number of anagrams for this word and list of anagrams
    """
    longest = ""
    for k in dict.keys():
        if len(k) == m:
            if longest in dict:
                if len(dict[k]) > len(dict[longest]):
                    longest = k
            else:
                longest = k
    if longest == "":
        return 0, None
    return len(dict[longest]), dict[longest]


def taskFour(l, dict, wlist):
    """
    Finds how many "good" jumbled words are there for words of a certain length
    :param l: length of the word
    :param dict: the dictionary with all the words and their anagrams
    :param wlist: list of words read from the word list
    :return: the number of good jumbled words with length l
    """
    a = 0
    for w in wlist:
        if len(w) == l:
            anag = taskTwo(w, dict)
            if len(anag) == 1:
                a = a + 1
    return a


def main():  # main function
    """
    tests the functions
    """
    #anagramDict = {}
    #w_list = []
    print("Task 1: ")
    print("Creating the dictionary...")
    anagramDict, w_list = taskOne("american-english.txt")

    print("Task 2:")
    while True:
        print("Enter input string (or hit enter to go to task 3):")
        task2 = input()
        if task2 == "":
            break
        r = taskTwo(task2, anagramDict)
        if r == None:
            print("No words can be formed from: ", task2)
        else:
            print("Corresponding words: ", r)

    print("Task 3:")
    while True:
        print("Enter word length (or hit enter to go to task 4): ")
        task3 = input()
        if task3 == "":
            break
        n, l = taskThree(int(task3), anagramDict)
        if not(n):
            print("No anagrams for length", task3, "found!")
        else:
            print("Max anagrams for length", task3, ": ", n)
            print("Anagram list:", l)

    print("Task 4:")
    while True:
        print("Enter word length (or hit enter to quit): ")
        task4 = input()
        if task4 == "":
            break
        print("Number of usable Jumble words of length", int(task4), ":", taskFour(int(task4), anagramDict, w_list))


if __name__ == '__main__':  # execute only if run as a script
    """
    __name__ is set to "__main__" when it is read from standard input or a script; the scope where
    top-level code executes 
    """
    main()
# program ends here



"""
Author: Ayush Rout
File: anagram.py
language: Python3
email: axr6077@rit.edu
"""
