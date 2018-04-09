"""
file: link_sort.py
author: Ayush Rout
github: https://github.com/cloudkayl
description: This program contains all the functions required to sort an unsorted linked sequence and returns
             sorted sequence in pretty printed format
"""

# program starts here
from linked_code_py import *

def list_link(lst):
    """
    converts list into linked sequence
    :param lst: the list being converted
    :return: linked sequence
    """
    lnk = None
    for idx in range(len(lst)-1, -1, -1):
        lnk = Node(int(lst[idx]), lnk)
    return lnk

def read_file(filename):
    """
    reads a file and returns a list of data inside it
    :param filename: the name of the file from where its reading and converting into list
    :return: list of data in file
    """
    fd = open(filename, 'r')
    lst = []
    for line in fd:
        s = line.strip()
        lst.append(float(s))
    return lst


def smallest_in_lnk(lnk):
    """
    returns the index of the smallest number in a linked sequence
    :param lnk: the linked sequence it's finding the smallest number from
    :return: index of the smallest number in sequence
    """
    temp = lnk.value
    idx = 0
    for i in range(lengthRec(lnk)):
        if lnk.value < temp:
            idx = i
            temp = lnk.value
        lnk = lnk.rest
    return idx

def val_at_index(idx, lnk):
    """
    returns value at given index in a sequence
    :param idx: the index its finding value at
    :param lnk: the linked sequence its finding the value at given index
    :return: the value at given index 'idx'
    """
    for i in range(idx):
        lnk = lnk.rest
    return lnk.value


def link_sort(lns):
    """
    uses the selection sort algorithm to sort a linked sequence
    :param lns: unsorted linked sequence
    :return: sorted linked sequence
    """
    sorted = None
    for idx in range(lengthRec(lns)):
        while lns!=None:
            s = smallest_in_lnk(lns)
            v = val_at_index(s, lns)
            sorted = insertAt(idx, v , sorted)
            lns = removeAt(s, lns)
    return reverseRec(sorted)

def  pretty_print(lns):
    """
    converts linked sequence in a way that it looks like a python list
    :param lns: the linked sequence its pretty-printing
    :return: pretty printed linked sequence
    """
    lst = []
    while lns!=None:
        lst.append(lns.value)
        lns = lns.rest
    return lst

# program ends here
"""
Author: Ayush Rout
File: link_sort.py
language: Python3
email: axr6077@rit.edu
"""