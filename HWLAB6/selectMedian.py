"""
file: selectMedian.py
author: Ayush Rout
github: https://github.com/cloudkayl
description: this program returns median and time taken to find median using quickSelect algorithm
"""

import time

def quickselect(alist, k):
    """
    quickSelect Algorithm will find the kth - smallest item in an Unordered list with a best case runtime of O(n)
    """
    k = int(k) #type conversion
    if k >= 0 and k < len(alist):
       if alist is None or len(alist) < 1:
           return None
       return select(alist, 0, len(alist) - 1, k)
    else:
        return None

def select(list, l, r, index):
            """
             this function returns the k-th smallest, (k >= 0)
            :param list: the list its returning kth smallest number from
            :param l: left list(smaller than pivot)
            :param r: right list(larger than pivot)
            :param index: index of the kth smallest number
            :return: k-th smallest, (k >= 0)
            """
            # base case
            if r == l:
                return list[l]
            # choose middle element of the list as pivot
            pivot = (len(list) // 2)
            # move pivot to beginning of list
            list[l], list[pivot] = list[pivot], list[l]
            # partition
            i = l
            for j in range(l + 1, r + 1):
                if list[j] < list[l]:
                    i += 1
                    list[i], list[j] = list[j], list[i]
            # move pivot to correct location
            list[i], list[l] = list[l], list[i]
            # recursively partition one side only
            if index == i:
                return list[i]
            elif index < i:
                return select(list, l, i - 1, index)
            else:
                return select(list, i + 1, r, index)

def list():
    fd = open("testDataSetLarge.txt", 'r') #10k data list
    list = []
    for line in fd:
        list.append(int(line.strip().split(' ')[-1]))
    return list

def testCases():
    # testCase 1: k is 0
    start = time.clock()
    test0 = quickselect(list(), 0)
    end = time.clock()
    t0 = end - start
    print(test0)
    print(t0)

    # testCase 2: k is negative i.e. less than 0
    start = time.clock()
    test1 = quickselect(list(), -200)
    end = time.clock()
    t1 = end - start
    print(test1)
    print(t1)

    # testCase 3: k is in float type
    start = time.clock()
    test2 = quickselect(list(), 10.598)
    end = time.clock()
    t2 = end - start
    print(test2)
    print(t2)

    # testCase 4: k is a random number
    start = time.clock()
    test3 = quickselect(list(), 299)
    end = time.clock()
    t3 = end - start
    print(test3)
    print(t3)

    # testCase 5: k is a random number
    start = time.clock()
    test4 = quickselect(list(), 5000)
    end = time.clock()
    t4 = end - start
    print(test4)
    print(t4)

    # testCase 6: k is more than possible index values
    start = time.clock()
    test5 = quickselect(list(), 12000)
    end = time.clock()
    t5 = end - start
    print(test5)
    print(t5)

    # testCase 7: k is the length of list
    start = time.clock()
    test6 = quickselect(list(), 10000)
    end = time.clock()
    t6 = end - start
    print(test6)
    print(t6)

    # testCase 8: k is a string
    start = time.clock()
    test6 = quickselect(list(), '2000')
    end = time.clock()
    t6 = end - start
    print(test6)
    print(t6)

if __name__ == '__main__': # execute only if run as a script
    """
        __name__ is set to "__main__" when it is read from standard input or a script; the scope where
        top-level code executes 
    """
    testCases()

#program ends here

"""
Author: Ayush Rout
File: selectMedian.py
language: Python3
email: axr6077@rit.edu
"""
