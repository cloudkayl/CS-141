"""
file: priority_queue.py
author: Ayush Rout
github: https://github.com/cloudkayl
description: this program removes highest priority item from a priority list
"""

"""
SOLUTIONS TO QUESTIONS:
1. What is the complexity for finding the highest priority element in your priority queue?  O(1)
2. What is the complexity for determining where to insert a new element into your priority queue?  O(logN) where the base of log is 2 
3. What is the complexity for adding a new element to your priority queue assuming you have already 
   calculated the location?  O(N)
4. What is the complexity for removing the highest priority element from your priority
   queue implementation?  O(1) 
5. Based on the previous answers, in what way is your priority queue implementation
   better, or worse, than using the built-in Python list operations on an unordered list?
   Its better cause built-in python functions has time complexity of O(N) or higher but my priority queue implementation got time
   complexity of either O(logN) or O(1) 
"""

#program starts here

def list():
    """
    User-defined list
    :return: a list of numbers(int)
    """
    return [2,4,5,2,3,10,16,19]
pq = list() #variable to store the list



def sort(lst):
    """
    this is the insertion sort function that sorts the list
    :param lst: the list that its sorting
    :return: sorted list
    """
    for mrk in range(0, len(lst)-1):
        insert(lst,mrk)

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


def binary_search_insert(target, list):
    """
    this function binary-searches a proper position where the item (which is to be added in the list)
    and returns the index of that position where the item will be added
    :param target: the item which is being put into list and then sorted
    :param list: the list to which the item is being added
    :return: result, the index at which the item is to be placed
    """
    if len(list) == 0:
        return 0
    U = len(list) - 1
    L = 0
    result = 0
    if target <= list[0]:
        result = 0
    elif target >= list[len(list) - 1]:
        result = len(list)
    else:
        while L <= U:
            M = int((L + U) / 2)
            if list[M] <= target:
                L = M + 1
            else:
               result = M
               U = M - 1
    return result


def enqueue(list, item):
        """
        this function takes two parameters list and item, where the item is added in priority order using binary search
        :param list: the list to which the item is being added in priority order
        :param item: the value being added to list
        :return: list, the list containing the new value
        """
        sort(list) #insertion-sorts the existing list first to perform binary-search
        a = binary_search_insert(item, list)
        list[:] = list[:a] + [item] + list[a:]
        return list

def dequeue(list):
    """
    this function takes one parameter list and pops/removes an item from the list which is in the highest priority
    not using list.pop() cause it's not relatively efficient
    :param list: the list from which the items are being popped
    :return: temp, the value/item which was popped/removed
    """
    temp = list[0]
    list[:] = list[1:]
    return temp



def ls():
    """
    function to return a list
    :return: an empty list
    """
    return []

ls = ls() #storing empty list under variable 'ls'

def sampleTest():
    """
    sampleTest function tests the enqueue and dequeue functions with an empty list and adds
    values to list, then printing the highest priority item first after popping the previous
    highest priority items
    """
    enqueue(ls, 15)
    enqueue(ls, -1)
    enqueue(ls, 3)
    enqueue(ls, 20)
    enqueue(ls, -11)
    enqueue(ls, 9)
    enqueue(ls, 0)
    enqueue(ls, -30)
    enqueue(ls, -5)
    print("Highest priority item for list ls is", dequeue(ls))
    print("Next highest priority item for list ls is", dequeue(ls))
    print("Next highest priority item for list ls is", dequeue(ls))
    print("Next highest priority item for list ls is", dequeue(ls))
    print("Next highest priority item for list ls is", dequeue(ls))
    print("Next highest priority item for list ls is", dequeue(ls))
    print("Next highest priority item for list ls is", dequeue(ls))
    print("Next highest priority item for list ls is", dequeue(ls))


def main():
    """
    main function calls the non-trivial test functions enqueue and dequeue and prints the highest priority item
    first and then prints the next highest priority items after popping the previous highest priority items
    """
    enqueue(pq, -56)
    enqueue(pq, 44)
    enqueue(pq, 32)
    enqueue(pq, -19)
    enqueue(pq, 11)
    enqueue(pq, 13)
    enqueue(pq, 15)
    enqueue(pq, 5)
    enqueue(pq, 0)
    print("Highest priority item for list pq is", dequeue(pq))
    print("Next highest priority item for list pq is", dequeue(pq))
    print("Next highest priority item for list pq is", dequeue(pq))
    print("Next highest priority item for list pq is", dequeue(pq))
    print("Next highest priority item for list pq is", dequeue(pq))
    print("Next highest priority item for list pq is", dequeue(pq))
    print("Next highest priority item for list pq is", dequeue(pq))
    print("Next highest priority item for list pq is", dequeue(pq))


if __name__ == "__main__":  # execute only if run as a script
    """
    __name__ is set to "__main__" when it is read from standard input or a script; the scope where
    top-level code executes 
    """
    sampleTest() #test functions
    main() #test functions
    print("") #skips a line
    print("Updated list ls:", ls) #prints the list ls after enqueue and dequeue function tests on it
    print("Updated list pq:", pq) #prints the list pq after enqueue and dequeue function tests on it


#program ends here

"""
Author: Ayush Rout
File: priority_queue.py
language: Python3
email: axr6077@rit.edu
"""