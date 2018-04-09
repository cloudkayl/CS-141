"""
file: inscribe_poly.py
author: Ayush Rout
language: Python3
github: https://github.com/cloudkayl
"""

import math as m
import turtle as t

def init():
	#fucntion that initializes the canvas with pensize equalling 2 and world coordinates of (-200, -200, 200, 200) and speed=0
    t.setworldcoordinates(-getWorldBorder(), -getWorldBorder(), getWorldBorder(), getWorldBorder())
    t.pensize(2)
    t.speed(0)
    t.up()


def getWorldBorder():
	"""
	Returns 200 as the world coordinates
	"""
	return 200

def newColor(n):
	"""
	function for changing color of the polygons: red, blue and green
	"""
	if not(n%3):
		t.pencolor('red')
	elif not(n%2):
		t.pencolor('blue')
	else:
		t.pencolor('green')

def newRad(r, N):
	"""
	function to get new radius for the subsequent inscribing circles
	"""
	c = m.sqrt((r*r)+(r*r)-2.0*r*r*m.cos((2*m.pi)/N))
	return m.sqrt((r*r)-((c/2)*(c/2)))

def drawPoly(r, N):
	"""
	function to draw a single polygon inside a circle
	"""
	n = N
	c = m.sqrt((r*r)+(r*r)-2.0*r*r*m.cos((2*m.pi)/N))
	t.fd(r)
	t.lt(180-(180*((N-2)/N))/2)
	t.down()
	while n > 0:
		t.fd(c)
		t.lt(360/N)
		n -= 1
	t.rt(180-(180*((N-2)/N))/2)
	t.pencolor('black') #black for circle
	t.lt(90)
	t.circle(r)
	t.rt(90)
	t.up()
	t.back(r)
	return c*N

def drawPolys(r, N, s=0):
	"""
	function to draw multiple polygons
	"""
	if N < 3:
		return s
	else:
		newColor(N)
		return drawPolys(newRad(r, N), N-1, s + drawPoly(r, N))

if __name__ == '__main__':
    init()
    l = int(input("Enter the number of sides(0 to quit):"))
    if l==0:
        exit()
    else:
        print("distance:", drawPolys(150, l))
    t.done()

#program ends here

"""
Author: Ayush Rout
File: zigzagBW.py
language: Python3
email: axr6077@rit.edu
"""
