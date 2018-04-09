

#######################################################################
##    NOTE : IT TAKES AROUND 32.20 seconds to draw the whole picture    ##
#######################################################################

"""
file: art_show.py
author: Ayush Rout
github: https://github.com/cloudkayl
description: draws a weed logo with along with batman logo(Kidding, just a cool design)
"""

#program starts here


import turtle as t
import math

def init():
    """
    init function initializes the canvas with the following:
    pre-conditions: background color set to black, speed set to 0, turtle facing North
    :return: NA
    """
    t.bgcolor('black')
    t.speed(0)
    t.lt(90)
    t.pu
    t.fd(200)
    t.pd()


def fernSize():
    """
    fernSize returns an int value of 1500
    :return: int(1500)
    """
    return 1500


def fern(size):
    """
    fern function recursively draws a christmas tree
    :param size: this is the size of the initial depth of tree
    :return: NA
    """
    if size>4:
        t.fd(size/25)
        t.left(90)
        fern(size*0.3)
        t.rt(90)
        t.right(90)
        fern(size * 0.3)
        t.left(90)
        fern(size * 0.85)
        t.back(size/25)


def drawLogo():
    """
    drawLogo function draws the batman logo
    :return: NA
    """
    myPen = t.Turtle() #initializes turtle as myPen

    myPen.color("white") #sets pen color to white
    myPen.pensize(5) #sets pensize to 5

    zoom = 20

    myPen.left(90)
    myPen.penup()
    myPen.goto(-7 * zoom, 0)
    myPen.pendown()

    for xz in range(-7 * zoom, -3 * zoom, 1): #left semi-oval
        x = xz / zoom
        absx = math.fabs(x)
        y = 1.5 * math.sqrt((-math.fabs(absx - 1)) * math.fabs(3 - absx) / ((absx - 1) * (3 - absx))) * (
        1 + math.fabs(absx - 3) / (absx - 3)) * math.sqrt(1 - (x / 7) ** 2) + (4.5 + 0.75 * (
        math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (
                                                                          1 + math.fabs(1 - absx) / (1 - absx))
        myPen.goto(xz, y * zoom)

    for xz in range(-3 * zoom, -1 * zoom - 1, 1): #bottom semi-oval
        x = xz / zoom
        absx = math.fabs(x)
        y = (2.71052 + 1.5 - 0.5 * absx - 1.35526 * math.sqrt(4 - (absx - 1) ** 2)) * math.sqrt(
            math.fabs(absx - 1) / (absx - 1))
        myPen.goto(xz, y * zoom)

    myPen.goto(-1 * zoom, 3 * zoom)
    myPen.goto(int(-0.5 * zoom), int(2.2 * zoom))
    myPen.goto(int(0.5 * zoom), int(2.2 * zoom))
    myPen.goto(1 * zoom, 3 * zoom)

    for xz in range(1 * zoom + 1, 3 * zoom + 1, 1):
        x = xz / zoom
        absx = math.fabs(x)
        y = (2.71052 + 1.5 - 0.5 * absx - 1.35526 * math.sqrt(4 - (absx - 1) ** 2)) * math.sqrt(
          math.fabs(absx - 1) / (absx - 1))
        myPen.goto(xz, y * zoom)

    for xz in range(3 * zoom + 1, 7 * zoom + 1, 1):
        x = xz / zoom
        absx = math.fabs(x)
        y = 1.5 * math.sqrt((-math.fabs(absx - 1)) * math.fabs(3 - absx) / ((absx - 1) * (3 - absx))) * (
        1 + math.fabs(absx - 3) / (absx - 3)) * math.sqrt(1 - (x / 7) ** 2) + (4.5 + 0.75 * (
        math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (
                                                                          1 + math.fabs(1 - absx) / (1 - absx))
        myPen.goto(xz, y * zoom)

    for xz in range(7 * zoom, 4 * zoom, -1):
        x = xz / zoom
        absx = math.fabs(x)
        y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(absx - 4) / (absx - 4))
        myPen.goto(xz, y * zoom)

    for xz in range(4 * zoom, -4 * zoom, -1):
        x = xz / zoom
        absx = math.fabs(x)
        y = math.fabs(x / 2) - 0.0913722 * x ** 2 - 3 + math.sqrt(1 - (math.fabs(absx - 2) - 1) ** 2)
        myPen.goto(xz, y * zoom)

    for xz in range(-4 * zoom - 1, -7 * zoom - 1, -1):
        x = xz / zoom
        absx = math.fabs(x)
        y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(absx - 4) / (absx - 4))
        myPen.goto(xz, y * zoom)

    myPen.penup()
    myPen.goto(600,600)


def drawFigure():
    """
    draws the christmas tree design and the logo
    :return: NA
    """
    init()
    t.hideturtle()
    t.pu()
    t.goto(0, 0)
    t.pd()
    t.pencolor('green')
    idx=0
    while idx<8: #iteratively draws a single christmas tree 8 times to draw a design
        fern(fernSize())
        t.right(45)
        idx+=1
    drawLogo()


def main():
    """
    main function calls the drawFigure function but with a condition that it draws instantly
    :return: NA
    """
    t.title("Ayush Rout")
    t.tracer(0,0)
    t.pu()
    t.goto(0,0)
    drawFigure()
    t.update()
    print("Completed Drawing!")
    t.done()
    t.getscreen().getcanvas().postscript(file='artShow.eps', colormode = 'color')


if __name__ == '__main__':
    main()
#program ends here


"""
Author: Ayush Rout
File: art_show.py
language: Python3
email: axr6077@rit.edu
"""
