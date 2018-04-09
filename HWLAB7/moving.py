"""
file: moving.py
author: Ayush Rout
github: https://github.com/cloudkayl
description: It implements three greedy ways to pack items into boxes whose capacities are provided and prints
             the strategy in which it was successful and in which it wasn't along with the items it couldn't
             successfully pack and in which strategy.
"""

# program starts here
from rit_lib import *  # the rit_lib.py class downloaded from https://cs.rit.edu/~csci141/lib/rit_lib.py

# initializing structures
Box = struct_type("Box", (int,"capacity"), (int,"filled"), (list,"items"))
Item = struct_type("Item", (str,"name"), (int,"weight"))



def create_Box(l = 1, m = 0, n = [] ):
    """
    creates a box
    :param l: capacity of the box
    :param m: weight already in the box
    :param n: the items being put in the created box
    :return: the box we created
    """
    return Box(int(l), int(m), list(n))

def addItem(box, item):
    """
    adds item to the box and returns whether or not it could fit that item
    :param box: the box its adding the item to
    :param item: the item that is being added to box
    :return: returns a boolean value that is, TRUE if success and FALSE if failed
    """
    if box.filled + item.weight < box.capacity:
        box.items.append(item)
        box.filled = box.filled + item.weight
        return True
    else:
        return False


def create_Item(n="Item", w=1):
    """
    creates an item
    :param n: name of item
    :param w: weight of the item
    :return: the item we created
    """
    return Item(str(n), int(w))

def rem_capacity(box):
    """
    determines the left space in a box
    :param box: the box its checking the left space with
    :return: the weight the box can still fit
    """
    return box.capacity - box.filled

def split_even_odd(i):
    """
    splits a list into two lists: one with odd indices and the other with even
    :param i: the original list to split
    :return: two lists, i.e. odd and even indexed lists
    """
    even = []
    odd = []
    Even = True
    for idx in range(len(i)):
        if Even:
            even.append(i[idx])
        else:
            odd.append(i[idx])
        Even = not (Even)
    return even, odd

def check_large(obj1, obj2):
    """
    takes two objects and checks whether the first is bigger than the second or not
    :param obj1: the first object
    :param obj2: the second object
    :return: whether the first is bigger than the second or not in BOOLEAN terms
    """
    if type(obj1) == Box and type(obj2) == Box:
        if obj1.capacity > obj2.capacity:
            return True
    elif type(obj1) == Item and type(obj2) == Item:
        if obj1.weight > obj2.weight:
            return True
    else:
        if obj1>obj2:
            return True
    return False

def merge_list(left, right):
    """
    combines two lists into one
    :param left: first list
    :param right: second list
    :return: combined list
    """
    l = 0
    r = 0
    merge = []
    while l < len(left) and r < len(right):
        if check_large(left[l], right[r]):
            merge.append(left[l])
            l = l + 1
        else:
            merge.append(right[r])
            r = r + 1

    if l < len(left):
        merge.extend(left[l:])
    elif r < len(right):
        merge.extend(right[r:])
    return merge

def sort(l):
    """
    sorts a list by the divide and conquer algorithm using recursion
    :param l: unsorted list that is to be sorted
    :return: the sorted list
    """
    if not (len(l)):
        return l
    elif len(l) == 1:
        return l
    else:
        evens, odds = split_even_odd(l)
        return merge_list(sort(evens), sort(odds))

def maxSpace(box):
    """
    checks the list of boxes 'box' to return the index of the box that has largest remaining capacity
    :param box: list of boxes
    :return: the index of the box that has largest remaining capacity
    """
    empty = 0
    notEmpty = 0
    for idx in range(len(box)):
        if rem_capacity(box[idx]) > rem_capacity(box[empty]):
            notEmpty = notEmpty + 1
            empty = idx
    return empty

def minSpace(box, item):
    """
    Finds the box with least space left with the item 'item' inside
    :param box: list of boxes 'item' is being placed in
    :param item: the item being placed in boxes
    :return: index of box that the item will go in, -1 if it doesn't fit any
    """
    empty = 0
    notEmpty = 0
    for idx in range(len(box)):
        if rem_capacity(box[idx]) >= item.weight:
            notEmpty = notEmpty + 1
            if rem_capacity(box[empty]) < item.weight or rem_capacity(box[idx]) - item.weight < rem_capacity(box[empty]) -\
                                                        item.weight:
                empty = idx
    if not (notEmpty):
        return -1
    return empty

def pop(items, lst):
    """
    Pops/removes the items from the list at the indices listed in 'lst'
    :param items: list of items objects are being removed from
    :param lst: list of indices being removed from items
    :return: NA
    """
    lst = sort(lst)
    for idx in lst:
        items.pop(idx)

def print_results(boxes, items, left, greed):
    """
    prints the results of the greedy strategies
    :param boxes: list of boxes in the test/given file
    :param items: list of items in the test/given file
    :param left: list of items that didn't fit into any box
    :param greed: number allotted to greedy algorithms
    :return: bool value to whether the greedy algorithm worked
    """
    print("\nResults of Greedy Strategy", greed, ":")
    if len(left):
        print("Could not fit all of the items!")
    else:
        print("All items successfully packed!")

    for b in range(len(boxes)):
        print("Box", b, "of capacity", boxes[b].capacity, "contains :")
        for i in range(len(boxes[b].items)):
            print("  ", boxes[b].items[i].name, "of weight", boxes[b].items[i].weight)

    if len(left):
        for l in left:
            print(l.name, "of weight", l.weight, "was left behind")
        return False
    return True

def greed1_roomiest(boxes, items):
    """
    It uses the strategy of running through the boxes, largest to smallest, and putting the item
    into the box that will have to most leftover space after the item is placed in it.
    :param boxes: list of boxes where the items are being put in
    :param items: list of items to be fit in boxes
    :return: it returns whether the greedy strategy was successful or not
    """
    left = []
    for idx in range(len(items)):
        max = maxSpace(boxes)
        if boxes[max].capacity - boxes[max].filled > items[idx].weight:
            if not(addItem(boxes[max], items[idx])):
                left.append(items[idx])
        else:
            left.append(items[idx])
    return print_results(boxes, items, left, 1)

def greed2_tightest(boxes, items):
    """
    It uses the strategy of running through the items from largest to smallest. Then, it finds the
    box that will have the least amount of space leftover with the item inside and places
    it in that box. If the item does not fit in any box, it is left out.
    :param boxes: list of boxes where the items are being put in
    :param items: list of items to be fit in boxes
    :return: it returns whether the greedy strategy was successful or not
    """
    left = []
    for idx in range(len(items)):
        min = minSpace(boxes, items[idx])
        if rem_capacity(boxes[min]) > items[idx].weight:
            addItem(boxes[min], items[idx])
        else:
            left.append(items[idx])
    return print_results(boxes, items, left, 2)

def greed3_oneBox(boxes, items):
    """
    Fills each box from largest to smallest, with the largest to smallest items. Items
    that don't fit any box are left out
    :param boxes: list of boxes where the items are being put in
    :param items: list of items to be fit in boxes
    :return: it returns whether the greedy strategy was successful or not
    """
    left = []
    delete = []
    for idx in range(len(boxes)):
        for idx1 in range(len(items)):
            if rem_capacity(boxes[idx]) >= items[idx1].weight:
                addItem(boxes[idx], items[idx1])
                delete.append(idx1)
        pop(items, delete)
        delete = []
    for i in items:
        left.append(i)
    return print_results(boxes, items, left, 3)

def read_input(file, box, item):
    """
    reads from the user file to get a list of boxes and items
    :param file: name of the file the program is reading from
    :param box: list of boxes to be added with boxes from the file
    :param item: list of items to be added with items from the file
    :return: NA
    """
    fd = open(file)
    idx = 0
    for line in fd:
        s = line.strip().split(' ')
        if not (idx):
            for idx1 in s:
                box.append(create_Box(int(idx1)))
        else:
            item.append(create_Item(s[:-1], int(s[-1])))
        idx +=1
    fd.close()

def check_file():
    """
    asks the user for file input and checks if that file is in valid format that is, in .txt format
    :return: f, the file
    """
    f = "items"
    while len(f):
        print("Enter the file: ")
        f = input()
        if f.endswith(".txt"):
            return f
        else:
            print("Input valid file type(.txt format)!")

def main(): #main function
    """
    Includes function calls to the greedy strategies
    :return: NA
    """
    fi = check_file()

    box1, item1 = ([], [])
    read_input(fi, box1, item1)
    box1 = sort(box1)
    item1 = sort(item1)
    greed1_roomiest(box1, item1)

    box2, item2 = ([], [])
    read_input(fi, box2, item2)
    box2 = sort(box2)
    item2 = sort(item2)
    greed2_tightest(box2, item2)

    box3, item3 = ([], [])
    read_input(fi, box3, item3)
    box3 = sort(box3)
    item3 = sort(item3)
    greed3_oneBox(box3, item3)





def testCases():
    # This function tests the program with different test cases of files provided at
    # https://cs.rit.edu/~csci141/pub/Labs/07/
    f_test1 = open("items1.txt")
    f_test2 = open("items2.txt")
    f_test3 = open("items3.txt")
    f_test4 = open("items4.txt")

    # test case with items1.txt
    box1, item1 = ([], [])
    read_input(f_test1, box1, item1)
    box1 = sort(box1)
    item1 = sort(item1)
    greed1_roomiest(box1, item1)

    box2, item2 = ([], [])
    read_input(f_test1, box2, item2)
    box2 = sort(box2)
    item2 = sort(item2)
    greed2_tightest(box2, item2)

    box3, item3 = ([], [])
    read_input(f_test1, box3, item3)
    box3 = sort(box3)
    item3 = sort(item3)
    greed3_oneBox(box3, item3)

    # test case with items2.txt
    box1, item1 = ([], [])
    read_input(f_test2, box1, item1)
    box1 = sort(box1)
    item1 = sort(item1)
    greed1_roomiest(box1, item1)

    box2, item2 = ([], [])
    read_input(f_test2, box2, item2)
    box2 = sort(box2)
    item2 = sort(item2)
    greed2_tightest(box2, item2)

    box3, item3 = ([], [])
    read_input(f_test2, box3, item3)
    box3 = sort(box3)
    item3 = sort(item3)
    greed3_oneBox(box3, item3)

    # test case with items3.txt
    box1, item1 = ([], [])
    read_input(f_test3, box1, item1)
    box1 = sort(box1)
    item1 = sort(item1)
    greed1_roomiest(box1, item1)

    box2, item2 = ([], [])
    read_input(f_test3, box2, item2)
    box2 = sort(box2)
    item2 = sort(item2)
    greed2_tightest(box2, item2)

    box3, item3 = ([], [])
    read_input(f_test3, box3, item3)
    box3 = sort(box3)
    item3 = sort(item3)
    greed3_oneBox(box3, item3)

    # test case with items4.txt
    box1, item1 = ([], [])
    read_input(f_test4, box1, item1)
    box1 = sort(box1)
    item1 = sort(item1)
    greed1_roomiest(box1, item1)

    box2, item2 = ([], [])
    read_input(f_test4, box2, item2)
    box2 = sort(box2)
    item2 = sort(item2)
    greed2_tightest(box2, item2)

    box3, item3 = ([], [])
    read_input(f_test4, box3, item3)
    box3 = sort(box3)
    item3 = sort(item3)
    greed3_oneBox(box3, item3)


if __name__ == '__main__': # execute only if run as a script
    """
     __name__ is set to "__main__" when it is read from standard input or a script; the scope where
     top-level code executes 
    """
    #testCases()
    main()

# program ends here

"""
Author: Ayush Rout
File: moving.py
language: Python3
email: axr6077@rit.edu
"""






