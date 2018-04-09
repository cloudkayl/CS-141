"""
file: storeLocation.py
author: Ayush Rout
github: https://github.com/cloudkayl
description: this program returns a store location using simplistic median algorithm
"""


#program starts here


import time

def quickSort(alist):
    """
               quickSort function chooses an element(here, the first one) of the list to be the pivot,
               then divides all other elements(except pivot) into two partitions :
               1. all elements less than the pivot must be in the first partition
               2. all elements greater than the pivot must be in the second partition.
               It then uses recursion to sort both partitions, finally joining the first sorted partition,
               the pivot and the second partition.
               :param alist: the list that has to be sorted
               :return alist: sorted list after merging them
    """
    quickSortHelper(alist, 0, len(alist) - 1)
    return alist


def quickSortHelper(alist, first, last):
    """
                This function takes three parameters alist, first, last and recursively partitions the list through
                split point. It begins with the same base case as the merge sort. If the length of the
                list is less than or equal to one, it is already sorted. If it is greater, then it can be partitioned
                and recursively sorted.
    """
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    """
                This picks the first element as the pivot and at the same time move other items to the appropriate side of the list,
                either less than or greater than the pivot value. It begins by incrementing leftmark until it locates a value that is
                greater than the pivot value. It then decrements rightmark until it finds a value that is less than the pivot value.
                At the point where rightmark becomes less than leftmark, it stops.
    """
    pivotvalue = alist[first]

    less = first + 1
    more = last

    done = False
    while not done:

        while less <= more and alist[less] <= pivotvalue:
            less = less + 1

        while alist[more] >= pivotvalue and more >= less:
            more = more - 1

        if more < less:
            done = True
        else:
            temp = alist[less]
            alist[less] = alist[more]
            alist[more] = temp

    temp = alist[first]
    alist[first] = alist[more]
    alist[more] = temp

    return more

def median(thelist):
    """
    This function returns median of a list using a simple algorithm of first quick-sorting the
    list and then returning the mid item
    :param thelist: the list from where median is returned
    :return: median of the list
    """

    sorted_list = quickSort(thelist)
    length = len(sorted_list)
    center = length // 2

    if length == 1:
        return sorted_list[0]

    elif length % 2 == 0:
        return sum(sorted_list[center - 1: center + 1]) / 2.0

    else:
        return sorted_list[center]

def list(): #large list of data
    fd = open("testDataSetLarge.txt", 'r') #10k data list
    list = []
    for line in fd:
        list.append(int(line.strip().split(' ')[-1]))
    return list

def testCases(): # running the same program several times for time comparision
    # testCase 1
    start = time.clock()
    med = median(list())
    end = time.clock()
    t1 = end - start
    print(med)
    print(t1)

    # testCase 2
    start = time.clock()
    med = median(list())
    end = time.clock()
    t2 = end - start
    print(med)
    print(t2)

    # testCase 3
    start = time.clock()
    med = median(list())
    end = time.clock()
    t3 = end - start
    print(med)
    print(t3)

    # testCase 4
    start = time.clock()
    med = median(list())
    end = time.clock()
    t4 = end - start
    print(med)
    print(t4)

    # testCase 5
    start = time.clock()
    med = median(list())
    end = time.clock()
    t5 = end - start
    print(med)
    print(t5)


if __name__ == '__main__': # execute only if run as a script
    """
        __name__ is set to "__main__" when it is read from standard input or a script; the scope where
        top-level code executes 
    """
    testCases()


#program ends here

"""
Author: Ayush Rout
File: storeLocation.py
language: Python3
email: axr6077@rit.edu
"""
