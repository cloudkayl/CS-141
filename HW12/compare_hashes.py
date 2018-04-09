"""
file: compare_hashes.py
author: Ayush Rout
github: https://github.com/cloudkayl
description: this program compares different types of hash functions and tests the performance of each.
"""

#program starts here
from math import *
from hashtable import *
import time as t
from test_hashes import *

#defining data structures
#HashTable = struct_type('HashTable', (list, 'table'), (int, 'size'), (int, 'capacity'), (object, 'hash_func'))
#Entry = struct_type('Entry', (object, 'key'), (object, 'values'))

def always_hashes_to_zero(key):
    """
    this hash function returns hash code as 0 for key
    :param key: key
    :return: 0
    """
    return 0

def add_ordinal_values(key):
    """
    returns sum of ASCII values of each letter in a string
    :param key: the string its encoding(input to the hash function)
    :return: encoded value of key
    """
    sum = 0
    for pos in range(len(key)):
        sum += ord(key[pos])
    return sum

def pow_ordinal_values(key):
    """
    returns sum of ASCII values of each index in string raised to the power of ASCII values of that indices in string
    :param key: the string its encoding(input to the hash function)
    :return: encoded value of key
    """
    sum = 0
    for pos in range(len(key)):
        sum += pow(ord(key[pos]), ord(key[pos]))
    return int(sum)

def good_hash_func(key):
    """
    returns hash code by encoding in the following format: ord(key[0])∗31^n−1 + ord(key[1])∗31^n−2 + ... + \
    ord(key[n − 1])∗31^0
    :param key: the string its encoding(input to the hash function)
    :return: encoded value of key
    """
    sum = 0
    for pos in range(len(key)):
        sum += ord(key[pos])*pow(31, len(key)-1)
    return int(sum)

def my_hash_func(key):
    """
    returns hash code by encoding in the following format: ord(key[0])^n-1 (for all even indices) + ord(key[1]) \
    (for all odd indices) where n is the len of the string
    :param key: the string its encoding(input to the hash function)
    :return: encoded value of key
    """
    sum = 0
    for pos in range(len(key)):
        if pos % 2 == 0:
            sum += pow(ord(key[pos]), len(key)-1)
        else:
            sum += ord(key[pos])
    return int(sum)

def check_file():
    """
    asks the user for file input and checks if that file is in valid format that is, in .txt format
    :return: f, the file
    """
    while True:
        f = input("Enter the name of the key file: ")
        if f.endswith(".txt"):
            return f
        else:
            print("Invalid file format! Try again...")

def list_keys():
    """
    it reads a file and obtains a list of contents in that file and the length of list depends upon user input
    :return: a list of keys obtained from file given by user
    """
    file = check_file()
    capacity = int(input("Enter the capacity of the table: "))
    list = []
    with open(file) as fd:
        for line in fd:
            items = line.strip()
            list.append(items)
            if len(list) >= capacity:
                break
    fd.close()
    return list

def put_count(hTable, key, value):
    """
    from hashtable.py provided by CS dept.
    put: HashTable(K, V) K V -> Boolean

    Using the given hash table, set the given key to the
    given value. If the key already exists, the given value
    will replace the previous one already in the table.
    If the table is full, an Exception is raised.
    """
    cnt = 0
    index = (hTable.hash_func(key) % hTable.capacity)
    startIndex = index  # We must make sure we don't go in circles.
    while hTable.table[index] != None and hTable.table[index].key != key:
        cnt += 1
        index = (index + 1) % hTable.capacity
        if index == startIndex:
            raise Exception("Hash table is full.")
    if hTable.table[index] == None:
        hTable.table[index] = Entry(key, value)
        hTable.size += 1
    else:
        hTable.table[index].value = value
    return cnt

def test_hash(key):
    """
    contains the tests for every hash function
    :param key: the list of keys the hash functions gonna use
    :return: NONE
    """

    # test for always_hashes_to_zero
    print("Evaluating always_hashes_to_zero")
    test_hash_func(always_hashes_to_zero)
    hashtable = createHashTable(always_hashes_to_zero, len(key))
    cnt = 0
    start = t.time()
    for idx in key:
        cnt += put_count(hashtable, idx, idx)
    end = t.time()
    time = end-start
    print('  Inserted', len(key), 'items into the hashtable in', time, 'seconds')
    print("  Average length of linear search:", cnt/len(key))

    # test for add_ordinal_values
    print("Evaluating add_ordinal_values")
    test_hash_func(add_ordinal_values)
    hashtable = createHashTable(add_ordinal_values, len(key))
    cnt = 0
    start = t.time()
    for idx in key:
        cnt += put_count(hashtable, idx, idx)
    end = t.time()
    time = end - start
    print('  Inserted', len(key), 'items into the hashtable in', time, 'seconds')
    print("  Average length of linear search:", cnt / len(key))

    # test for pow_ordinal_values
    print("Evaluating pow_ordinal_values")
    test_hash_func(pow_ordinal_values)
    hashtable = createHashTable(pow_ordinal_values, len(key))
    cnt = 0
    start = t.time()
    for idx in key:
        cnt += put_count(hashtable, idx, idx)
    end = t.time()
    time = end - start
    print('  Inserted', len(key), 'items into the hashtable in', time, 'seconds')
    print("  Average length of linear search:", cnt / len(key))

    # test for good_hash_func
    print("Evaluating good_hash_func")
    test_hash_func(good_hash_func)
    hashtable = createHashTable(good_hash_func, len(key))
    cnt = 0
    start = t.time()
    for idx in key:
        cnt += put_count(hashtable, idx, idx)
    end = t.time()
    time = end - start
    print('  Inserted', len(key), 'items into the hashtable in', time, 'seconds')
    print("  Average length of linear search:", cnt / len(key))

    # test for my_hash_func
    print("Evaluating my_hash_func")
    test_hash_func(my_hash_func)
    hashtable = createHashTable(my_hash_func, len(key))
    cnt = 0
    start = t.time()
    for idx in key:
        cnt += put_count(hashtable, idx, idx)
    end = t.time()
    time = end - start
    print('  Inserted', len(key), 'items into the hashtable in', time, 'seconds')
    print("  Average length of linear search:", cnt / len(key))

key = list_keys()
if __name__ == '__main__': # execute only if run as a script
    """
     __name__ is set to "__main__" when it is read from standard input or a script; the scope where
            top-level code executes 
    """
    test_hash(key)

# program ends here

"""
Author: Ayush Rout
File: compare_hashes.py
language: Python3
email: axr6077@rit.edu
"""

