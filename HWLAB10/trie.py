"""
file: trie.py
author: Ayush Rout
github: https://github.com/cloudkayl
description: this program does operations like insert, search, height, largest and smallest on a trie
"""

#program starts here

from rit_lib import *

# defining data structure for our trie --> basically a binary tree
Trie = struct_type("Trie", ((NoneType, "Trie"), "left"), (object, "value"), ((NoneType, "Trie"), "right"))

def insert(trie, st):
    """
    inserts a string into trie, returns True if successful and returns False if not that is if the trie contains the
    string already
    :param trie: the trie its inserting string into
    :param st: the string being inserted
    :return: True or False as in description
    """
    return insert_rec(trie, st, 0)

def insert_rec(trie, st, idx):
    """
    helper function for insert
    :param trie: the trie its inserting string into
    :param st: the string its inserting
    :param idx: start value =: 0, iteratively goes through the trie to find and insert the string at appropriate
    position
    :return: True if inserted successfully into the trie and False if the same string is already in the trie
    """
    if trie.value == "":
        if st[idx] == "1":
            if trie.right != None:
             return insert_rec(trie.right, st, idx + 1)
            else:
                trie.right = Trie(None, st, None)
                return True
        else:
            if trie.left != None:
                return insert_rec(trie.left, st, idx + 1)
            else:
                trie.left = Trie(None, st, None)
                return True
    else:
        y = trie.value
        if st == y:
            return False
        trie.value = ""
        return split(trie, st, y, idx)

def split(trie, st, y, idx):
    """
    splits a trie if the values at indices of a string matches the values at the same indices of the input string
    :param trie: the trie it's inserting the string in
    :param st: the string being inserted into trie
    :param y: the value in the trie with which input sting is compared with
    :param idx: the index that helps for the comparision of value in trie with index string
    :return:
    """
    if st[idx] == y[idx]:
        if st[idx] == "1":
            trie.right = Trie(None, "", None)
            return split(trie.right, st, y, idx + 1)
        else:
            trie.left = Trie(None, "", None)
            return split(trie.left, st, y, idx + 1)
    else:
        if st[idx] == "1" and y[idx] == "0":
            trie.left = Trie(None, y, None)
            trie.right = Trie(None, st, None)
            return True
        else:
            trie.left = Trie(None, st, None)
            trie.right = Trie(None, y, None)
            return True

def trie_to_list(trie):
    """
    it converts a trie to a list in increasing order
    :param trie: the trie its converting into list
    :return: list containing the data contained in the trie
    """
    if trie == None:
        return []
    else:
        list = trie_to_list(trie.left) + [trie.value] + trie_to_list(trie.right)
        while '' in list:
            list.remove('')
        return list

def largest(trie):
    """
    searches and returns the largest value in trie
    :param trie: the trie in which its searching the largest value
    :return: the largest value in the trie
    """
    current = trie
    while current.right != None:
        current = current.right
    return current.value

def smallest(trie):
    """
    searches and returns the smallest value in trie
    :param trie: the trie in which its searching the smallest value
    :return: the smallest value in the trie
    """
    current = trie
    while current.left != None:
        current = current.left
    return current.value

def search(trie, st):
    """
    searches for nearest match to a str in trie
    :param trie: the trie we are searching in
    :param st: the string we are searching for in trie
    :return: the string in trie which is in nearest match to the provided string
    """
    if trie.left == None:
        return smallest(trie.right)
    elif largest(trie) == st:
        return st
    elif smallest(trie) == st:
        return st
    else:
        nearest = ''
        for idx in range(0, len(st)-1):
            if trie.value[idx] == st[idx]:
                return True
            else:
                return False
        while True:
            return nearest + trie.value

def size(trie):
    """
    it returns the size of a trie
    :param trie: the trie its returning size of
    :return: the size of the trie
    """
    tempList = trie_to_list(trie)
    return len(tempList)

def height(trie):
    """
    returns the height of the trie
    :param trie: the trie its returning the height of
    :return: the height of the trie
    """
    if trie is None:
        return 0
    else:
        return max(height(trie.left), height(trie.right)) + 1

"""
For testing-------------------------------------------
def main():                                          |
    trie = Trie(None, "01100", None)                 |
    print(insert(trie, "10001"))                     |
    print(insert(trie, "00011"))                     |
    print(insert(trie, "10010"))                     |
    print(insert(trie, "10011"))                     |
    print(insert(trie, "11111"))                     |
    print(insert(trie, "00000"))                     |
    print(trie)                                      |
    print(height(trie))                              |
    print(size(trie))                                | 
    print(trie_to_list(trie))                        |
    print(smallest(trie))                            |
    print(largest(trie))                             |
    print(search(trie, "11111"))                     |
    print(search(trie, "11011"))                     |
    print(search(trie, "00000"))                     |
    print(search(trie, "10110"))                     |
    print(search(trie, "11101"))                     |
    print(search(trie, "00011"))                     |
    print(search(trie, "01100"))                     |
------------------------------------------------------
"""

############################
"""                        #
if __name__ == '__main__': #
    main()                 #
"""                        #
############################

#Program ends here


"""
Author: Ayush Rout
File: trie.py
language: Python3
email: axr6077@rit.edu
"""
