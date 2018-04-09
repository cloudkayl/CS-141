"""
file: sort_compare.py
author: Ayush Rout
github: https://github.com/cloudkayl
description: this program compares different methods of sorting python lists
"""


import random
import time

def sort(lst):
        """
        this is the insertion sort function that sorts the list
        :param lst: the list that its sorting
        :return lst: sorted list
        """
        for mrk in range(0, len(lst)-1):
            insert(lst,mrk)
        return lst

def insert(lst,mrk):
        """
        this function inserts an index mrk so that it compares the value at each index and sorts the list
        :param lst: the list that is being sorted
        :param mrk: index/marker
        :return: null
        """
        i= mrk
        while(lst[i]>lst[i+1]) and i>=0:
            temp = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = temp
            i = i-1

#test function for insertion sort
def test_insertion_sort():
        isortlist = [56,7,3,43,54,54,6,7,78] #unsorted test list
        isortlist_sorted = [3,6,7,7,43,54,54,56,78] #sorted test list
        sort(isortlist)
        if isortlist == isortlist_sorted: #comparing if unsorted list is equal to sorted list
            return True
        else:
            return False



def merge(left, right):
        """
            function to merge two arrays
            :param left: the left half of the input array
            :param right: right half of the input array
            :return: merged arrays
        """
        if not len(left) or not len(right):
            return left or right

        result = []
        i, j = 0, 0
        while (len(result) < len(left) + len(right)):
            if left[i] < right[j]:
                result.append(left[i])
                i+= 1
            else:
                result.append(right[j])
                j+= 1
            if i == len(left) or j == len(right):
                result.extend(left[i:] or right[j:])
                break

        return result

def mergesort(list):
        """
            Merge Sort:
            — recursively sorts the first half of the input array
            — then recursively sorts the second half of the input array
            — and finally merges two sorted sub-lists into one list.
            :param list: the list that has to be sorted
            :return: sorted list after merging them
        """
        if len(list) < 2:
            return list

        middle = len(list)//2
        left = mergesort(list[:middle])
        right = mergesort(list[middle:])

        return merge(left, right)

#test function for merge sort
def test_merge_sort():
        msortlist = [56,7,3,43,54,54,6,7,78] #unsorted test list
        msortlist_sorted = [3,6,7,7,43,54,54,56,78] #sorted test list
        mergesort(msortlist)
        if msortlist == msortlist_sorted: #comparing if unsorted list is equal to sorted list
            return True
        else:
            return False


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
       quickSortHelper(alist,0,len(alist)-1)
       return alist

def quickSortHelper(alist,first,last):
       """
            This function takes three parameters alist, first, last and recursively partitions the list through
            split point. It begins with the same base case as the merge sort. If the length of the
            list is less than or equal to one, it is already sorted. If it is greater, then it can be partitioned
            and recursively sorted.
       """
       if first<last:

           splitpoint = partition(alist,first,last)

           quickSortHelper(alist,first,splitpoint-1)
           quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
       """
            This picks the first element as the pivot and at the same time move other items to the appropriate side of the list,
            either less than or greater than the pivot value. It begins by incrementing leftmark until it locates a value that is
            greater than the pivot value. It then decrements rightmark until it finds a value that is less than the pivot value.
            At the point where rightmark becomes less than leftmark, it stops.
       """
       pivotvalue = alist[first]

       leftmark = first+1
       rightmark = last

       done = False
       while not done:
           while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
               leftmark = leftmark + 1

           while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
               rightmark = rightmark -1

           if rightmark < leftmark:
               done = True
           else:
               temp = alist[leftmark]
               alist[leftmark] = alist[rightmark]
               alist[rightmark] = temp

       temp = alist[first]
       alist[first] = alist[rightmark]
       alist[rightmark] = temp

       return rightmark

#test function for quick sort
def test_quick_sort():
        qsortlist = [56,7,3,43,54,54,6,7,78] #unsorted test list
        qsortlist_sorted = [3,6,7,7,43,54,54,56,78] #sorted test list
        quickSort(qsortlist)
        if qsortlist == qsortlist_sorted: #comparing if unsorted list is equal to sorted list
            return True
        else:
            return False




def getUserTimeOut():
        """
        function asks user for their desired timeout
        :return: t_out
        """
        t_out = int(input("What is the timeout (in seconds)? "))
        if t_out == "":
            return 1
        else:
            return t_out




def main():
        """
        Contains user input for initial list size, timeout, max and min values of list
        Stops executing if program takes more than timeout time given by user in seconds
        :return: null
        """
        t_out = getUserTimeOut() #gets user input for timeout
        lst_size = int(input("Initial list size: "))
        min = int(input("What is the min possible value of an item in the list: "))
        max = int(input("What is the max possible value of an item in the list: "))
        (it,mt,qt) = (0,0,0)
        if lst_size > min:
            while it < t_out or mt < t_out or qt < t_out:

                t_list = random.sample(range(max), lst_size)
                (il, ml, ql) = (t_list[:], t_list[:], t_list[:])

                print("**************************")
                print("Size= ", lst_size)
                print("**************************")

                if it < t_out:
                    start = time.time()
                    sort(il)
                    end = time.time()
                    it = end - start
                    print("Insertion Sort Time: ", it)

                if mt < t_out:
                    start = time.time()
                    mergesort(ml)
                    end = time.time()
                    mt = end - start
                    print("Merge Sort Time: ", mt)

                if qt < t_out:
                    start = time.time()
                    quickSort(ql)
                    end = time.time()
                    qt = end - start
                    print("Quick Sort Time: ", qt)


                lst_size = lst_size * 10
        else:
            return 0



if __name__ == '__main__': # execute only if run as a script
        """
        __name__ is set to "__main__" when it is read from standard input or a script; the scope where
        top-level code executes 
        """
        main()


#program ends here


"""
Author: Ayush Rout
File: sort_compare.py
language: Python3
email: axr6077@rit.edu
"""






"""
Output:
    >>> 
    What is the timeout (in seconds)? 1
    Initial list size: 300
    What is the min possible value of an item in the list: 1
    What is the max possible value of an item in the list: 1000000000
    **************************
    Size=  300
    **************************
    Insertion Sort Time:  0.0090000629425
    Merge Sort Time:  0.00200009346008
    Quick Sort Time:  0.00100016593933
    **************************
    Size=  3000
    **************************
    Insertion Sort Time:  0.947999954224
    Merge Sort Time:  0.0239999294281
    Quick Sort Time:  0.0119998455048
    **************************
    Size=  30000
    **************************
    Insertion Sort Time:  96.748000145
    Merge Sort Time:  0.305000066757
    Quick Sort Time:  0.147000074387
    **************************
    Size=  300000
    **************************
    Merge Sort Time:  3.84700012207
    Quick Sort Time:  1.96600008011
    >>>
"""







