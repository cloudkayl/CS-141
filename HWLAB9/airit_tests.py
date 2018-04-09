"""
Test airit_simulation.py
file: airit_tests.py
author: Ayush Rout
"""

from airit_simulation import *

def main():
    """
    this function contains the test functions to the functions defined in airit_simulation.py
    """
    #################################
    ####file: passengers_small.txt###
    #################################
    file = open("passengers_small.txt")
    gate = mkEmptyQueue()
    plane = mkEmptyStack()
    passenger = read_passenger(file)
    gate.max = 10
    Aircraft.maxCapacity = 10
    while file.readline() != None:
        for line in file:
            while line != "":
                line_up(Gate, passenger, file)
                boarding(gate, plane)
    deplane()

    # file: passengers_small.txt
    gate = mkEmptyQueue()
    plane = mkEmptyStack()
    passenger = read_passenger(file)
    gate.max = 0
    Aircraft.maxCapacity = 10
    while file.readline() != None:
        for line in file:
            while line != "":
                line_up(Gate, passenger, file)
                boarding(gate, plane)
    deplane()

    # file: passengers_small.txt
    gate = mkEmptyQueue()
    plane = mkEmptyStack()
    passenger = read_passenger(file)
    gate.max = 10
    Aircraft.maxCapacity = 0
    while file.readline() != None:
        for line in file:
            while line != "":
                line_up(Gate, passenger, file)
                boarding(gate, plane)
    deplane()

    # file: passengers_small.txt
    gate = mkEmptyQueue()
    plane = mkEmptyStack()
    passenger = read_passenger(file)
    gate.max = 0
    Aircraft.maxCapacity = 0
    while file.readline() != None:
        for line in file:
            while line != "":
                line_up(Gate, passenger, file)
                boarding(gate, plane)
    deplane()



    #################################
    ###file: passengers_large.txt####
    #################################
    file1 = open("passengers_large.txt")
    gate = mkEmptyQueue()
    plane = mkEmptyStack()
    passenger = read_passenger(file)
    gate.max = 10
    Aircraft.maxCapacity = 10
    while file1.readline() != None:
        for line in file:
            while line != "":
                line_up(Gate, passenger, file1)
                boarding(gate, plane)
    deplane()

    # file: passengers_large.txt
    gate = mkEmptyQueue()
    plane = mkEmptyStack()
    passenger = read_passenger(file1)
    gate.max = 0
    Aircraft.maxCapacity = 10
    while file1.readline() != None:
        for line in file1:
            while line != "":
                line_up(Gate, passenger, file1)
                boarding(gate, plane)
    deplane()

    # file: passengers_large.txt
    gate = mkEmptyQueue()
    plane = mkEmptyStack()
    passenger = read_passenger(file1)
    gate.max = 10
    Aircraft.maxCapacity = 0
    while file1.readline() != None:
        for line in file1:
            while line != "":
                line_up(Gate, passenger, file1)
                boarding(gate, plane)
    deplane()

    # file: passengers_large.txt
    gate = mkEmptyQueue()
    plane = mkEmptyStack()
    passenger = read_passenger(file1)
    gate.max = 0
    Aircraft.maxCapacity = 0
    while file1.readline() != None:
        for line in file1:
            while line != "":
                line_up(Gate, passenger, file1)
                boarding(gate, plane)
    deplane()


    
    #################################
    #file: passengers_very_small.txt#
    #################################
    file2 = open("passengers_very_small.txt")
    gate = mkEmptyQueue()
    plane = mkEmptyStack()
    passenger = read_passenger(file2)
    gate.max = 10
    Aircraft.maxCapacity = 10
    while file.readline() != None:
        for line in file2:
            while line != "":
                line_up(Gate, passenger, file2)
                boarding(gate, plane)
    deplane()

    # file: passengers_small.txt
    gate = mkEmptyQueue()
    plane = mkEmptyStack()
    passenger = read_passenger(file2)
    gate.max = 0
    Aircraft.maxCapacity = 10
    while file.readline() != None:
        for line in file2:
            while line != "":
                line_up(Gate, passenger, file2)
                boarding(gate, plane)
    deplane()

    # file: passengers_small.txt
    gate = mkEmptyQueue()
    plane = mkEmptyStack()
    passenger = read_passenger(file2)
    gate.max = 10
    Aircraft.maxCapacity = 0
    while file.readline() != None:
        for line in file2:
            while line != "":
                line_up(Gate, passenger, file2)
                boarding(gate, plane)
    deplane()

    # file: passengers_small.txt
    gate = mkEmptyQueue()
    plane = mkEmptyStack()
    passenger = read_passenger(file2)
    gate.max = 0
    Aircraft.maxCapacity = 0
    while file.readline() != None:
        for line in file2:
            while line != "":
                line_up(Gate, passenger, file2)
                boarding(gate, plane)
    deplane()


if __name__ == '__main__': # execute only if run as a script
    """
    __name__ is set to "__main__" when it is read from standard input or a script; the scope where
    top-level code executes 
    """
    main()
