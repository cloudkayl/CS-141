""""
file: conditionals.py
language: Python3
author: axr6077@rit.edu
github: https://github.com/cloudkayl 
description: (Week 2 cs141 Homework) Program to test a function that determines if the larger of two integers is evenly divisible
by the smaller integer
"""""


#program starts here

"""""
divisible() function to determine if larger of two integers is evenly divisible by the smaller interger
"""
def divisible(p, q):
    if p<0 or q<0:
        print("Inputs must be positive integers!")
    elif p==q:
        print("Those integers are equal")
    elif q!=p:
        if q > p:
            if q % p == 0:
                print(q,"is evenly divisible by", p)
            else:
                print(q,"is not evenly divisible by",p)
        elif p > q:
                if p % q == 0:
                    print(p,"is evenly divisible by", q)
                else:
                    print(p,"is not evenly divisible by",q)
#divisible() function ends here




"""""
test_divisible() function tests divisible function by calling it several times with different inputs
"""
def test_divisible():
    divisible(4,8)
    divisible(10,50)
    divisible(5,8)
    divisible(9, 10)
    divisible(10, 45)
    divisible(57, 114)
    divisible(5, 18)
#test_divisible function ends here




"""""
squared() function determines if the square of the first parameter is equal to the second parameter
"""
def squared(m, n):
    if m*m == n:
        print(m,"squared IS",n)
    else:
        print(m,"squared IS NOT",n)
#squared() function ends here




"""""
test_squared() function tests squared function by calling it several times with different inputs
"""
def test_squared():
    squared(10,100)
    squared(100, 50)
    squared(8,64)
    squared(11,121)
    squared(20,70)
    squared(90,100)
    squared(70,4900)
#test_squared() function ends here




"""""
main() function calls all the function calls including calls to test functions
"""
def main():
    test_divisible()
    test_squared()
#main() function ends here




"""""
Calling the main() function
"""
main()
#end of code




"""""
Author: Ayush Rout
File: conditionals.py
language: Python3
email: axr6077@rit.edu
"""












