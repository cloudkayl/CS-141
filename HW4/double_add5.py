"""
file: double_add5.py
author: Ayush Rout
language: Python3
github: https://github.com/cloudkayl
"""

#program starts here
import math


def print_sequence_rec(start, count):
    """
    func: print_sequence_rec
    description: Takes an input of the starting number, and the number of iterations, then
           prints the sequence
    param start: int, Starting number
    param count: int, at least one to work properly, number of numbers to gen in the sequence
    """
    if count+1:
        print(start, end=" ")
        print_sequence_rec((start*2)+5, count-1)


def print_sequence_iter(start, count):
    """
    func: print_sequence_iter
    description: It iteratively generates and prints count steps of the double and add 5
           sequence from the start value. The values of the sequence are printed on a single line 
           separated by a space.
    """
    while count+1:
        print(start, end=" ")
        start = (start*2)+5
        count = count - 1

def print_sequence(start, count):
    while count:
        start = (start*2)+5
        count = count - 1
    return start

def print_sequence_rev(start, count):
    while count:
        start = (start-5)/2
        count = count - 1
    return start

def find_start_forward(goal, count):
    """
    func: print_sequence_iter
    description: It iteratively searches forward from an initial
          value of 0, and returns the start value of the sequence.
    Pre-conditions: goal>=0, count>0
    """
    i = 0
    while True:
        if print_sequence(i,count) > goal or print_sequence(i,count) == goal:
            return i
        else:
            i = i + 1

def find_back_limit_rec(nbr, count):
    """
    func: find_back_limit_rec
    description: It recursively searches backward from the nbr
         value up to count number of steps back through the sequence. The function returns
         the smallest starting number that will produce a sequence value whose count^th value
         will be >= nbr.
    """
    if count:
        nbr = math.ceil((nbr-5)/2)
        count = count - 1
        return find_back_limit_rec(nbr,count)
    else:
        return nbr

def find_back_limit_iter(nbr, count):
    """
    func: find_back_limit_iter
    description: It  iteratively searches backward from the nbr
         value up to count number of steps back through the sequence. The function returns
         the smallest starting number that will produce a sequence value whose count^th value
         will be >= nbr
    """
    while count:
        nbr = math.ceil((nbr-5)/2)
        count = count - 1
    return nbr

if __name__ == '__main__':
    print_sequence_rec(2,5)
    print("") # newline
    print_sequence_iter(121,3)
    print("") # newline
    print(find_start_forward(100,3))
    print(find_back_limit_rec(1000,3))
    print(find_back_limit_iter(1000,3))

#program ends here

"""
Author: Ayush Rout
File: double_add5.py
language: Python3
email: axr6077@rit.edu
"""