"""
file: airit_simulation.py
author: Ayush Rout
github: https://github.com/cloudkayl
description: This program runs a simulation of AIRRIT.
"""

from linked_code import *
from myQueue import *
from myStack import *

# structure definitions
Passenger = struct_type("Passenger", (str, 'name'), (str, 'ticket'), (bool,'bag')) # structure for passengers/students
Gate = struct_type("Gate", (int, "max"), (Queue, 'Zone1'), (Queue, 'Zone2'), (Queue, 'Zone3'),\
                   (Queue, 'Zone4'), (int, 'currCapacity')) # structure for the gates at airport
Aircraft = struct_type("Aircraft", (int, "maxCapacity"), (Stack, 'without_bag'), (Stack, 'with_bag')) # structure for aircraft
# creating objects for the structures
aircraft = mkEmptyStack()
gate = mkEmptyQueue()

def check_file():
    """
    asks the user for file input and checks if that file is in valid format that is, in .txt format
    :return: f, the file
    """
    while True:
        f = input("Passenger data file: ")
        if f.endswith(".txt"):
            return f
        else:
            print("Invalid file format! Try again...")

def read_passenger(file):
    """
    this function reads from the file where data is in a specific format and returns a passenger along with their
    details
    :param file: the opened file it's reading from
    :return: the Passenger structure containing details of a single passenger
    """
    words = file.readline().strip().split(',')
    if words == None:
        return None
    return Passenger(words[0], words[1], (eval(words[2])))

def line_up(gate, stu, file):
    """
    this function simulates the line up at a gate at the airport with four zones. The passengers are segregated into
    different zones according to the first digit of their ticket numbers.
    :param gate: queue, the gate where the passengers are lining up
    :param stu: structure, contains details of the passenger lined up for boarding
    :param file: the file it's reading passenger details from
    :return: NONE
    """
    gate.currCapacity = 0
    while gate.currCapacity < gate.max:
        stu = read_passenger(file)
        if stu.ticket[0] == '1':
            enqueue(gate.Zone1, stu)
        elif stu.ticket[0] == '2':
            enqueue(gate.Zone2, stu)
        elif stu.ticket[0] == '3':
            enqueue(gate.Zone3, stu)
        elif stu.ticket[0] == '4':
            enqueue(gate.Zone4, stu)
        gate.currCapacity += 1
    if gate.currCapacity == gate.max:
        print("The gate is full; remaining passengers must wait.")


def boarding(gate, aircraft):
    """
    this function simulates the boarding of an aircraft
    :param gate: queue, the gate from where the passengers board the aircraft
    :param aircraft: stack, the aircraft where passengers are boarding
    :return: NONE
    """
    # Zone4
    while not emptyQueue(gate.Zone4) and not Aircraft.maxCapacity:
        stu = front(gate.Zone4)
        dequeue(gate.Zone4)
        push(aircraft, stu)
    # Zone3
    while not emptyQueue(gate.Zone3) and not Aircraft.maxCapacity:
        stu = front(gate.Zone3)
        dequeue(gate.Zone3)
        push(aircraft, stu)
    # Zone2
    while not emptyQueue(gate.Zone2) and not Aircraft.maxCapacity:
        stu = front(gate.Zone2)
        dequeue(gate.Zone2)
        push(aircraft, stu)
    # Zone1
    while not emptyQueue(gate.Zone1) and not Aircraft.maxCapacity:
        stu = front(gate.Zone1)
        dequeue(gate.Zone1)
        push(aircraft, stu)

def deplane():
    """
    it simulates the deplaning of an aircraft
    :return: Passenger object containing the details of the passengers that are leaving the aircraft
    """
    Aircraft.currCapacity = Aircraft.max
    while not emptyStack(Aircraft.without_bag) and Aircraft.currCapacity != 0:
        if Passenger.bag == False:
            passenger_without_bag = top(Aircraft.without_bag)
            pop(Aircraft.without_bag)
            Aircraft.currCapacity -= 1
    if Aircraft.currCapacity == 0:
        pass
    else:
        while not emptyStack(Aircraft.with_bag) and Aircraft.currCapacity != 0:
            passenger_with_bag = top(Aircraft.with_bag)
            pop(Aircraft.with_bag)
            Aircraft.currCapacity -= 1
    return Passenger

def main():
    """
    this is the main function that contains the function calls and overall manages the whole simulation.
    :return: NONE
    """
    fd = open(check_file())
    cap = input("Gate Capacity: ")
    air_cap = input("Aircraft Capacity: ")
    print("Beginning simulation...")
    print("Passengers are lining up at the gate...")
    gate.max = cap
    while fd.readline() != None:
        Aircraft.maxCapacity = air_cap
        for line in fd:
            while line != "":
                line_up(Gate, Passenger, fd)
                boarding(gate, aircraft)
        print("People are disembarking...")
        deplane()
    print("Simulation complete; all passengers are at their destination!")

main()
# program ends here

"""
Author: Ayush Rout
File: airit_simulation.py
language: Python3
email: axr6077@rit.edu
"""
