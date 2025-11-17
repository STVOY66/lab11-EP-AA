# https://github.com/STVOY66/lab11-EP-AA
# Partner 1: Ethan Pauly
# Partner 2: Aidan Arjune (Absent)

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def square_root(a):
    try:
        return math.sqrt(a)
    except:
        raise ValueError

def hypotenuse(a, b):
    return math.hypot(a, b)

def mul(a, b):
    return a * b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a

def exp(a, b):
    return math.pow(a, b)

def logarithm(a, b):
    return math.log(b, a)
