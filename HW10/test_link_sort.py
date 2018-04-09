"""
file: test_link_sort.py
author: Ayush Rout
github: https://github.com/cloudkayl
description: Contains the test cases that is the function calls mentioned in link_sort.py
"""

#program starts here

from link_sort import *

def main():
    """
    contains the function calls from link_sort.py
    :return: NA
    """
    file = user_input()
    lst = read_file(file)
    linked = list_link(lst)
    print("Original Sequence:\n", linked)
    sort = link_sort(linked)
    print("Sorted Sequence:\n", sort)
    print("Original sequence(pretty print):\n", pretty_print(linked))
    print("Sorted(pretty print):\n", pretty_print(sort))



def user_input():
    """
    prompts user for file input and checks if the user input is in correct format.
    Asks again if format is wrong
    :return: the file
    """
    fd = "file"
    while len(fd):
        fd = input("Enter the file name: ")
        if fd.endswith(".txt"):
            return fd
        else:
            print("Enter valid file type!")


if __name__ == '__main__': # execute only if run as a script
    """
    __name__ is set to "__main__" when it is read from standard input or a script; the scope where
    top-level code executes 
    """
    main()
    while True:
        prompt = input("Do you want to have more tests?(enter y for more or any key to exit) ")
        if prompt == 'y':
            main()
        else:
            break

# program ends here

"""
Author: Ayush Rout
File: test_link_sort.py
language: Python3
email: axr6077@rit.edu
"""
