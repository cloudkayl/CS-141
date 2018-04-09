"""
file: droid_factory.py
author: Ayush Rout
github: https://github.com/cloudkayl
description: Simulation of a Droid Factory
"""

#program starts here
from linked_code import *
from myQueue import *
from myStack import *

Droid = struct_type("Droid", (int, "serial_no"), (bool, "arms"), (bool, "legs"), (bool, "head"), (bool, "body"))
FactoryWorker = struct_type("FactoryWorker", (str, "Name"), (Queue, "belt"), (Stack, "container"))

def serial_no():
    """
    returns a serial number for the droid
    :return: int, value = 10001
    """
    return 10001

def check_file():
    """
    asks the user for file input and checks if that file is in valid format that is, in .txt format
    :return: f, the file
    """
    f = "files"
    while len(f):
        print("Enter parts filename: ")
        f = input()
        if f.endswith(".txt"):
            return f
        else:
            print("Input valid file type(.txt format)!")

f = check_file()

def read_file(filename):
    """
    reads a file and converts it into a list
    :param filename: the file its opening
    :return: list, the list of data retrieved from file
    """
    lst = []
    fd = open(f, 'r')
    for line in fd:
        s = fd.readline().strip().split('\n')
        lst.append(str(s))
    return lst

def get_worker_name():
    name = input("Enter the name of the worker:")
    return name

def create_Droid(serial_no):
    """
    creates an empty droid
    :param serial_no: a serial number assigned to droid
    :return: empty queue
    """
    if serial_no == 0:
        return None
    else:
        return Droid(serial_no, False, False, False, False)

def test_create_Droid():
    """
    test function to check if create_Droid works
    """
    create_Droid(10004)

def createQueue():
    """
    creates a queue out of the data read from file
    :return: queue of parts of the droid
    """
    belt = mkEmptyQueue()
    parts = read_file(f)
    for line in parts:
        enqueue(belt, parts)
    return belt

FactoryWorker.container = mkEmptyStack()
con_belt = createQueue()

def build_droid(Droid, serial_no):
    """
    assembles a droid
    :param Droid: the droid its assembling
    :param serial_no: the serial number it's assigned to
    :return: NONE
    """
    value = str(front(con_belt))
    dequeue(con_belt)
    p1 = 'head'
    p2 = 'arms'
    p3 = 'legs'
    p4 = 'body'
    if value == p1:
            if Droid.Head == True:
                print("placing unneeded part back on belt:", p1)
                enqueue(con_belt, p1)
            else:
                Droid.head = True
                print("attaching", p1, "...")
                #dequeue(con_belt)
    elif value == p2:
            if Droid.Head == True:
                print("placing unneeded part back on belt:", p2)
                enqueue(con_belt, p2)
            else:
                Droid.head = True
                print("attaching", p2, "...")
                #dequeue(con_belt)
    elif value == p3:
            if Droid.Head == True:
                print("placing unneeded part back on belt:", p3)
                enqueue(con_belt, p3)
            else:
                Droid.head = True
                print("attaching", p3, "...")
                #dequeue(con_belt)
    elif value == p4:
            if Droid.Head == True:
                print("placing unneeded part back on belt:", p4)
                enqueue(con_belt, p4)
            else:
                Droid.head = True
                print("attaching", p4, "...")
                #dequeue(con_belt)



def main():
    """
    contains all the function calls and prompts user for file input along with prompting user for name
    """
    read_file(f)
    name = get_worker_name()
    print(name, "is starting a shift at the droid factory!")
    S_No = serial_no()
    droid = create_Droid(S_No)
    while con_belt.size != 0:
        print(name, "is building a new droid with serial number", S_No)
        build_droid(droid, S_No)
        if droid.head == True and droid.arms == True and droid.legs == True and droid.body == True:
            push(FactoryWorker.container, serial_no)
        S_No += 1
    print("packing droid into shipping container")
    if con_belt.size == 0:
        print("a shipment of droids is being unloaded..")
        for idx in range(0, droid.serial_no):
            print(droid)

if __name__ == '__main__': # execute only if run as a script
    """
         __name__ is set to "__main__" when it is read from standard input or a script; the scope where
         top-level code executes 
    """
    main()

#program ends here

"""
Author: Ayush Rout
File: droid_factory.py
language: Python3
email: axr6077@rit.edu
"""
