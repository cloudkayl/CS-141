"""""
File: card_design.py
Description: Its a simple program to draw two playing cards
Name: Ayush Rout
"""""


#importing turtle
import turtle as t



#function to initialize
def initialize():
    t.speed(6) #setting turtle speed to 6
    t.left(90) #setting required initial orientation

    

#function to draw border
def drawBorder():
    t.forward(350)
    t.left(90)
    t.forward(225)
    t.left(90)
    t.forward(350)
    t.left(90)
    t.forward(225)
    t.left(90)
    t.up()
    t.forward(50)
    t.left(90)
    t.forward(50)
#drawBorder Function ends here
    


#fucntion to draw border for the second card
def drawBorder2():
    t.forward(350)
    t.left(90)
    t.forward(225)
    t.left(90)
    t.forward(350)
    t.left(90)
    t.forward(225)
    t.left(90)
    t.up()
    t.forward(50)
    t.left(90)
    t.forward(20)
#Function for drawing the border of second card ends here

    


#funciton to draw the smaller diamond 
def drawLeftcorner():
    t.pencolor("red")
    t.left(45)
    t.down()
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.up()
    t.right(45)
#fucntion to draw smaller diamond ends here
    



#function to draw the center diamond
def drawCenterDesign():
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.right(135)
    t.up()
    t.forward(120)
##function to draw the center diamond ends here

    


#function to draw the letter "Q" on card
def drawText():
    t.write("Q", font=("Arial", 60) )
#function end

    


#function to draw corner clubs
def cornerClub():
    t.fd(20)
    t.pd()
    t.right(73)
    t.circle(10,290)
    t.right(180)
    t.circle(10, 290)
    t.right(180)
    t.circle(10, 290)
    t.right(167)
    t.fd(10)
    t.left(90)
    t.fd(5)
    t.left(90)
    t.fd(10)
    t.right(90)
#fucntion to draw corner clubs ends here
    



#function to draw club shape
def club():
    t.speed(9)
    t.right(73)
    t.circle(30,290)
    t.right(180)
    t.circle(30, 290)
    t.right(180)
    t.circle(30, 290)
    t.right(167)
    t.fd(30)
    t.left(90)
    t.fd(11.7)
    t.left(90)
    t.fd(30)
    t.right(90)
#function to draw club shape ends here

    



#main function starts here
def main():
    initialize()
    drawBorder()
    t.fillcolor("red")
    t.begin_fill()
    drawLeftcorner()
    t.end_fill()
    t.forward(30)
    t.left(90)
    t.forward(69)
    t.right(45)
    t.down()
    t.fillcolor("red")
    t.begin_fill()
    drawCenterDesign()
    t.end_fill()
    t.left(90)
    t.forward(27)
    drawText()
    t.up()
    t.forward(80)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(47)
    t.fillcolor("red")
    t.begin_fill()
    drawLeftcorner()
    t.end_fill()
    t.left(90)
#first card's code ends here

#second card's code starts here
    t.up()
    t.forward(300)
    t.right(90)
    t.forward(300)
    t.left(90)
    t.forward(10)
    t.right(180)
    t.pencolor("black")
    t.forward(10)
    t.right(180)
    t.forward(225)
    initialize()
    t.pd()
    t.pencolor("black")
    drawBorder2()
    t.up()
    t.fillcolor("black")
    t.begin_fill()
    cornerClub()
    t.end_fill()
    t.up()
    t.right(90)
    t.fd(75)
    t.left(90)
    t.fd(68)
    t.right(180)
    t.pd()
    t.fillcolor("black")
    t.begin_fill()
    club()
    t.end_fill()
    t.up()
    t.left(90)
    t.fd(180)
    t.left(90)
    t.fd(90)
    t.right(180)
    t.fillcolor("black")
    t.begin_fill()
    cornerClub()
    t.end_fill()
#second card's code ends here
    t.pu()
    t.fd(64)
    t.right(90)
    t.fd(90)
    t.write("K", align="center", font=("Arial", 50, "bold"))
    t.up()
    t.fd(350)
    t.right(90)
    t.forward(180)
    t.pd()
    t.write("Diamond and Club", align="center", font=("Arial", 60, "bold"))
    t.left(90)
    t.pu()
    t.fd(100)
    t.pd()
    t.write("CS LAB 1", align="center", font=("Arial", 60, "bold"))
    t.right(90)
#main function ends here



#calling the main function
main()




#program ends here
t.done()





""""
Code by Ayush Rout
HW1, CS LAB 1
Contact: axr6077@rit.edu
"""
