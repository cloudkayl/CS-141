""""
file: fruitfulFun.py
author: Ayush Rout
date: 09.15.2017
language: Python3
author: axr6077@rit.edu
github: https://github.com/cloudkayl 
"""""



#program starts here
"""""
sumSquare() function finds the sum of all of squares of n numbers from 0 to n
"""
def sumSquares(n):
    if not (n):
        return 0
    else:
        return (n * n) + sumSquares(n - 1)


"""
sumSquaresAccum() function finds the sum of all of squares of n numbers from 0 to n but this time with accumulator
"""


def sumSquaresAccum(n, a):
    if not (n):
        return a
    else:
        return sumSquaresAccum(n - 1, a + (n * n))


"""
sumSquares() takes a single parameter, n, representing the number of terms in the summation, and makes 
the initial call to sumSquaresAccum with appropriate initial values for any accumulation parameters
"""


def sumSquaresTR(n):
    return sumSquaresAccum(n, 0)


"""
stairClimb() uses given number of stair steps, returns possible amount of moves that can be used to
climb them, using either 1, 2, or 3 step moves up the stairs
"""


def stairClimb(n):
    if (n == 1) or (n == 2):
        return n
    elif n == 3:
        return 4
    else:
        return stairClimb(n - 1) + stairClimb(n - 2) + stairClimb(n - 3)


"""
stairClimbAccum() uses given number of stair steps, and returns possible amount of moves
that can be used to climb them, using either 1, 2, or 3 step moves up the stairs
"""


def stairClimbAccum(n, a, b, c):
    if (n == 1) or (n == 2):
        return n
    elif n == 3:
        return c
    else:
        return stairClimbAccum(n - 1, b, c, a + b + c)


"""
starClimbTR() that takes a single parameter, n, representing the number of stairs, and makes the initial call to 
stairClimbAccum with appropriate initial values for any accumulation parameters
"""


def stairClimbTR(n):
    return stairClimbAccum(n, 1, 2, 4)



#sumSquaresTest() calls both types of recursive square summing functions, prints and compares their output  with the correct ones
def sumSquaresTest():
    print('Non-TR Sum of Squares test...')
    print('Sum of Squares Test')
    print('n=0: 0', sumSquares(0))
    print('n=1: 1', sumSquares(1))
    print('n=2: 5', sumSquares(2))
    print('n=3: 14', sumSquares(3))
    print('n=4: 30', sumSquares(4))
    print('n=5: 55', sumSquares(5))
    print('n=6: 91', sumSquares(6))
    print('')

    print('TR Sum of Squares test...')
    print('Sum of Squares Test')
    print('n=0: 0', sumSquaresTR(0))
    print('n=1: 1', sumSquaresTR(1))
    print('n=2: 5', sumSquaresTR(2))
    print('n=3: 14', sumSquaresTR(3))
    print('n=4: 30', sumSquaresTR(4))
    print('n=5: 55', sumSquaresTR(5))
    print('n=6: 91', sumSquaresTR(6))
    print('')



#stiarClimbTest() calls both types of recursive stair step solving functions printing and comparing their outputs with the correct ones
def stairClimbTest():
    print('Non-TR Stair Climbing test...')
    print('Stair Climbing test')
    print('n=1 1', stairClimb(1))
    print('n=2 2', stairClimb(2))
    print('n=3 4', stairClimb(3))
    print('n=4 7', stairClimb(4))
    print('n=5 13', stairClimb(5))
    print('n=6 24', stairClimb(6))
    print('')

    print('TR stair climbing test...')
    print('Stair Climbing test')
    print('n=1 1', stairClimbTR(1))
    print('n=2 2', stairClimbTR(2))
    print('n=3 4', stairClimbTR(3))
    print('n=4 7', stairClimbTR(4))
    print('n=5 13', stairClimbTR(5))
    print('n=6 24', stairClimbTR(6))
    print('')


#since script is executed and not imported
if __name__ == '__main__':
    sumSquaresTest()
    stairClimbTest()
    
    
#program ends here


"""""
Author: Ayush Rout
File: zigzagBW.py
language: Python3
email: axr6077@rit.edu
"""