""""
file:zigzagBW.py
language: Python3
author: axr6077@rit.edu
github: https://github.com/cloudkayl 
description: draws black and white zigzags recursively according to the number of depths given by user
"""""



#program starts here
import turtle



"""""
init() function initializes the turtle with the following conditions:
       pen is up
       facing north
       speed set to 7
"""
def init():
    turtle.up()
    turtle.left(90)
    turtle.speed(7)



def drawZigZag0(size):
    pass



#draws level 1 zigzag that's just an inverted z
def drawZigZag1(size):
    turtle.forward(size/2)
    turtle.right(90)
    turtle.forward(size)
    turtle.back(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.back(size)
    turtle.right(90)
    turtle.forward(size/2)



#draws level 2 zigzag, but with branches
def drawZigZag2(size):
    turtle.forward(size/2)
    turtle.right(90)
    turtle.forward(size)

#second zigzag
    turtle.left(90)
    turtle.forward(size/2)
    turtle.right(90)
    turtle.forward(size/2)
    turtle.back(size/2)
    turtle.right(90)
    turtle.forward(size/2)
    turtle.right(90)
    turtle.forward(size/2)
    turtle.back(size/2)
    turtle.right(90)
    turtle.forward(size/2)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)

#new zigzag
    turtle.forward(size/2)
    turtle.right(90)
    turtle.forward(size/2)
    turtle.back(size/2)
    turtle.right(90)
    turtle.forward(size/2)
    turtle.right(90)
    turtle.forward(size/2)
    turtle.back(size/2)
    turtle.right(90)
    turtle.forward(size/2)
    turtle.right(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size/2)







#this function recursively draws the zigzag with the user input 'depth' that is number of line segments from start to the end of recursive zigzags
def drawZigZag(size, depth):
    if depth > 0:
        turtle.forward(size/2)
        turtle.right(90)
        turtle.forward(size)

        turtle.left(90)
        drawZigZag(size/2, depth - 1)
        turtle.left(90)

        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)

        turtle.right(90)
        drawZigZag(size/2, depth - 1)
        turtle.right(90)

        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size/2)



#main function that calls the defined functions under one block
def main():
    init()
    turtle.down()
    def input_check():
        size = int(input("Enter the size of the zigzag: "))
        depth = int(input("Input the number of depths needed: "))
        if depth < 0 or size < 0:
            print("Hey. Your input must be non-negative integer!")
            size = int(input("Enter the size of the zigzag: "))
            depth = int(input("Input the number of depths needed: "))
            drawZigZag(size, depth)
        else:
            drawZigZag(size, depth)
    input_check()
    turtle.up()
    turtle.done()
#main() function definition ends here



#calling the main function
main()

"""""
Author: Ayush Rout
File: zigzagBW.py
language: Python3
email: axr6077@rit.edu
"""
