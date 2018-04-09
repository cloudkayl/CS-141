"""""
File: card_design1.py
Description: Its a simple program to draw a card with basic designs and a letter
Name: Ayush Rout
"""""


import turtle as t


#function to initialize program with turtle speed and orientation
def initialize():
    t.speed(6)
    t.left(90)

#function to draw border
def drawBorder():
    t.pd()
    t.forward(350)
    t.left(90)
    t.forward(225)
    t.left(90)
    t.forward(350)
    t.left(90)
    t.forward(225)


#Function to draw the letter Q
def drawText():
    t.write("Q", align="center", font=("Arial", 60) )



#Function to draw design(crown)
def drawCrown():
    t.pd()
    t.pencolor("Black")
    t.forward(40)
    t.right(70)
    t.forward(60)
    t.right(150)
    t.forward(60)
    t.left(120)
    t.forward(70)
    t.right(160)
    t.forward(70)
    t.left(120)
    t.forward(60)
    t.right(150)
    t.forward(60)
    t.right(70)
    t.forward(40)



#Function to bring back turtle to initial position
def initialPos():
    t.up()
    t.forward(112.5)
    t.right(90)
    t.forward(135)
    t.left(90)



#main function starts here
def main():
    initialize()
    drawBorder()
    t.left(90)
    t.up()
    t.forward(150)
    t.left(90)
    t.forward(112.5)
    t.pencolor("red")
    drawText()
    t.right(90)
    t.up()
    t.forward(100)
    t.left(90)
    t.fillcolor("red")
    t.begin_fill()
    drawCrown()
    t.end_fill()
    t.left(90)
    t.up()
    t.forward(115)
    t.left(90)
    t.fillcolor("red")
    t.begin_fill()
    drawCrown()
    t.end_fill()
    t.pencolor("Black")
    initialPos()



#calling main function
main()

#program ends here
t.done()




"""""
Author: Ayush Rout
Link: https://github.com/cloudkayl
"""""

