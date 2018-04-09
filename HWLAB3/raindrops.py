""""
file: raindrops.py
author: Ayush Rout
date: 09.19.2017
language: Python3
author: axr6077@rit.edu
github: https://github.com/cloudkayl 
"""""

#program starts here
import turtle as t
import random as ran
import math as m

#variable initialization
n = int(input("Enter the number of Rain Drops:"))
d = int(input("Enter the number of Ripples per rain drop:"))

#returns maximum number of raindrops that can be accepted from the user
def RAIN_max():
    return 100


#statement to check the max number of raindrops
if n > RAIN_max():
    print("Enter a number within 100")
    exit()
else:
    def init():
        """""
        Initializes the canvas with toggling turtle to invisible, drawing a blue pond and turtle speed to 0. 
        pre-conditions: turtle visible, facing east and pendown
        post-conditions: turtle invisible, at a random position within mentioned coordinates, pendown
        """""
        t.hideturtle()
        t.speed(0)
        t.home()
        t.color("black", "light blue")
        t.begin_fill()
        Draw_Pond()
        t.end_fill()
        t.up()
        t.setpos(ran.randint(-230, 230), ran.randint(-230, 230))
        t.down()



    def Draw_Pond():
        """""
        This function draws the area where the rain drops and ripples are going to be drawn, apparently the pond
        """""
        t.up()
        t.forward(325)
        t.down()
        t.right(90)
        t.forward(325)
        t.right(90)
        t.forward(650)
        t.right(90)
        t.forward(650)
        t.right(90)
        t.forward(650)
        t.right(90)
        t.forward(325)



    def rd(r, n):
        """""
        This function draws the raindrops called recursively at random coordinates with random colors and random radii
        """""
        if n > 0:
            t.up()
            t.setpos(ran.randint(-230, 230), ran.randint(-230, 230))
            t.down()
            randomcol()
            t.begin_fill()
            t.circle(r)
            t.end_fill()
            t.color("black")
            t.right(90)
            t.up()
            t.forward(r * 1.8)
            t.left(90)
            t.down()
            dr1(r * 3  , d)
            rd(randomrad(), n - 1)
        else:
            pass


    def dr1(r1, d):
        """""
        This function draws the ripples called recursively
        """""
        if d > 0:
            t.circle(r1)
            t.right(90)
            t.up()
            t.forward(10)
            t.left(90)
            t.down()
            dr1(r1 + 10, d - 1)
        else:
            pass


#initializing an array of colors
    colors = ["red", "green", "orange", "purple", "black", "yellow", "magenta", "cyan"]

#returns a random color from the array of colors initialized
    def randomcol():
        t.color(ran.choice(colors))


#initializing an array of values that is to be assigned to the radii
radii = [5, 6, 7, 8, 9, 10, 11, 12]



def randomrad():
    """""
    This function returns a random radius for the raindrops
    """""
    return ran.choice(radii)


def main():
    """""
    The main() function calls all the other defined functions and prints the total circumference of the raindrops
    """""
    init()
    rd(randomrad(), n)
    print("Total Circumfrence = ", n * (2 * m.pi * randomrad()))
    t.up()

#calling the main function and ending the program
main()
t.done()



"""""
Author: Ayush Rout
File: raindrops.py
language: Python3
email: axr6077@rit.edu
"""""