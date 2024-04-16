# File: FunctionExamples.py
# Student:  Yejin Hong
# UT EID:   yh25386
# Course Name: CS303E
# 
# Date Created: 02/22/24
# Description of Program: function examples 

import math

#----------------------------------------------------------------------
# 1. Write a function to return the sum of three numbers.  I did this
#    one for you.

def sum3Numbers (x, y, z):
    """Return the sum of the three parameters."""
    _3rd_ = 1
    return x + y + z

#----------------------------------------------------------------------
# 2. Write a function to return the product of three numbers.

def multiply3Numbers( x, y, z ):
    return x * y * z

#----------------------------------------------------------------------
# 3. Write a function to return the sum of up to 3 numbers.  It should
#    accept 1, 2, or 3 parameters.  Hint: any parameter not given
#    defaults to 0.

def sumUpTo3Numbers (x, y = 0, z = 0):
    return x + y + z
#----------------------------------------------------------------------
# 4. Write a function to return the product of up to 3 numbers.  It
#    should accept 1, 2, or 3 parameters.  Hint: what should the
#    default be in this case?

def multiplyUpTo3Numbers (x, y=1, z=1 ):  # supply default args
    return x * y * z
#----------------------------------------------------------------------
# 5. Write a function that takes 2 numbers as input and prints them
#    out in ascending order.  Make sure it works if they are equal.

def printInOrder( x, y ):
    if x <= y:
        print(x, y)
    else:
        print(y, x)
#----------------------------------------------------------------------
# 6. Write a function that returns the area of a square, given the length of a side.
#    Print an error message if side is negative. 

def areaOfSquare( side ):
    if side < 0:
        print("Error: Side length cannot be negative.")
    else:
        return side ** 2
#----------------------------------------------------------------------
# 7. Write a function that returns the perimeter of a square, given
#    the length of a side.  Print an error message if side is negative.

def perimeterOfSquare( side ):
    if side < 0:
        print("Error: Side length cannot be negative.")
    else:
        return 4* side
    
#----------------------------------------------------------------------
# 8. Write a function that returns the area of a circle, given the
#    radius.  Use math.pi. Print an error message if radius is negative.

def areaOfCircle( radius ):
    if radius < 0:
        print("Error: Radius cannot be negative.")
    else:
        return math.pi * radius ** 2
#----------------------------------------------------------------------
# 9. Write a function that returns the circumference of a circle given
#    the radius.  Use math.pi. Print an error if radius is negative.

def circumferenceOfCircle( radius ):
    if radius < 0:
        print("Error: Radius cannot be negative.")
    else:
        return 2 * math.pi * radius
    
#----------------------------------------------------------------------
# 10. Write a function: given parameters d1, d2, x, returns whether
#    both d1 and d2 are both factors of (evenly divide) x.  You can
#    assume all values are integers.

def bothFactors( d1, d2, x ):
    if x % d1 == 0 and x % d2 == 0:
        return True
    else:
        return False

#----------------------------------------------------------------------
# 11. Given a value x, compute and print out the area and circumference of a circle with
#    radius x and the area and perimeter of a square with side x.  Use your previous 
#    functions for these computations.  Leave a blank line above and below the printing.

def squareAndCircle( x ):
    if x<0:
        print("Error: Length/radius cannot be negative.")
    else:
        print("Area of square:", areaOfCircle(x))
        print("Perimeter of square:", perimeterOfSquare(x))
        print("Area of circle:", areaOfCircle(x))
        print("Circumference of circle:", circumferenceOfCircle(x))
        
        
#----------------------------------------------------------------------
# 12. Write a function that returns the factorial of a positive
#     integer n.  Use a for loop to compute the factorial.  You can
#     assume the input is an integer, but print an error message if
#     it's not positive and return None.

def factorial( n ):
    if n <= 0:
        print("Erorr: Input must be a positive integer.")
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

#----------------------------------------------------------------------
# 13. Write a function that returns the number of digits in the
#     decimal representation of a number n.  You can assume that
#     n is a positive integer.  E.g., numberLength( 12345 ) = 5.

def numberLength( n ):
    if n <= 0:
        print("Error: Input must be a positive integer.")
    else:
        return len(str(n))

#----------------------------------------------------------------------
# 14. Write a function that sums positive numbers entered by the user
#     and returns the sum.  You can assume that user inputs are
#     numbers (float or int).  If the number entered is negative, print 
#     an error message and continue;  don't add it to the sum.  There 
#     can be any number of inputs.  Stop when the user enters 0. 
#     (Note: This was a problem from Exam1 in an earlier semester.)

def sumPositiveNumbers():
    total_sum = 0
    while True:
        num = float(input("Enter a number (0 to stop): "))
        if num < 0:
            print("Error: Negative number entered. Ignored.")
        elif num == 0:
            break
        else:
            total_sum += num