

# =======================================
# Scope, Namespace and Recursion
# =======================================

# There are some unusual aspects of scope and namespace in python that can be a little confusing
# We will review the basics here and then discuss the behavior that may be strange compared other languages


# Python allows functions to be nested in other functions.
# This has an impact on scope in some unexpected ways.

# =======================
# Recursion
# =======================

# One reason to nest a function within another function is to perform initialization before a recursive function call
# A recursive function is a function that calls itself
# This can be very useful when dealing with structures that contain themselves such as directories in a computer file system
# or for computing mathematical functions that are defined recursively.

# The mathematical "Factorial" function is the product of all the numbers from 1 to n
# "Factorial" is the product of an integer and all the integers below it; e.g., factorial four ( 4! ) is equal to 24.
# Factorial 4 = 1x2x3x4 = 24

# We will create this function named "fact" to calculate factorial of any number you pass.
# I have commented out this code with the print statements that help follow the logic.
# We will use the "fact" function after this one that has no optional print statement

# NOTE that 0 factorial is 1. Here is an explanation about that
# https://www.khanacademy.org/math/precalculus/prob-comb/combinatorics-precalc/v/zero-factorial-or-0


def fact(n):  # we will pass argument "n" when we call function "fact"
    """ Calculate n! iteratively """
    result = 1
    print("Initial Result = {}".format(result)) # Optional print. To show initial result.

    if n > 1:
        for f in range(2, n + 1):
            print("f = {}".format(f))  # optional print
            result *= f
            print("New Result_1 = {}".format(result))  # Optional print
    return result

for i in range(10):
    print("i = {} and New Result_2 = {}".format(i, fact(i)))  # New Result is calculated from fact(i). It will be 1 if i is 0 or 1
    print("=" * 30)


# We will use this "fact" function without the optional print statements


def fact(n):  # we will pass argument "n" when we call function "fact"
    """ Calculate n! iteratively """
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result

for i in range(15):
    print("{} Factorial = {}".format(i, fact(i)))


# ====================
# Recursive function
# ====================

# Now we will write a recursive equivalent of above code.
# NOTE: n Factorial is written as n!
# This code is producing the same factorials as above code but is now using a recursive function
# The recursion here is where it calls itself on "factorial(n-1)"

# How it works
# Note that if you give n = 4, it loops through n until n = 2 and then it returns a value
# so n=4 calls n=3, which in turn calls n=2 which calls n=1
# n=1 returns 1, which is passed to n=2 to give result 2, which is then passed to n=3 to give result 6
# which is then passed to n=4 to give result 24
# n = 4, n-1 = 3
# n = 3, n-1 = 2
# n = 2, n-1 = 1

# so recursive functions call themselves until they get a return which in turn is looped upwards to get final result
#


def factorial(n):
    """ n! can also be defined as n * (n-1)! """
    """ Calculates n! recursively """
    if n <= 1:
        return 1
    else:
        print("n = {}, n-1 = {}".format(n, (n - 1)))         # Optional print to show n and n-1
        print("n ({}) factorial = {}".format(n, (n * factorial(n-1))))  # Optional print to show n x (n-1)!
        return n * factorial(n-1)


for i in range(5):
    print("Hence {} Factorial = {}".format(i, factorial(i)))
    print("=" * 20)


# ===================================================
# Fibonacci numbers: calculate using recursive code:
# ===================================================

# https://en.wikipedia.org/wiki/Fibonacci_number
# In mathematics, the Fibonacci numbers are the numbers in the following integer sequence, called the Fibonacci sequence,
# and characterized by the fact that every number after the first two is the sum of the two preceding ones:
# 1,1,2,3,5,8,13,21,34,55,89,144,....
# 0,1,1,2,3,5,8,13,21,34,55,89,144,...

# Fibonnacci sequence appear in nature. See this link
# https://en.wikipedia.org/wiki/Fibonacci_number#In_nature

# We will now create a Fibonacci function and call it "fib"

def fib(n):
    """ F(n) = F(n-1) + F(n-2) """
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

# We are passing a range starting from 0
# Position  = 0,1,2,3,4,5,6,7, 8, 9, 10, 11, 12
# Fibonacci = 0,1,1,2,3,5,8,13,21,34,55, 89, 144,

for i in range(6):
    print("Position {} Fibonacci = {}".format(i, fib(i)))
    print("=" * 25)


# NOTE that above code to calculate fibonacci takes a long time if you pass it a number above 36
# This is because it is an inefficient way of calculating fibonacci because it has to call itself
# twice (n-1) & (n-2) for each number (n)

# Recursive functions can be useful but if there is a simple interactive approach, that will always be better
# Seeing how long it takes to calculate first 35 numbers

# We will now make an iterative approach that runs a lot faster to calculate fibonacci number

# ===================================
# Fibonnaci: calculate with recursive
# ===================================
# This is same as above code without optional prints

def fib(n):
    """ F(n) = F(n-1) + F(n-2) """
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

for i in range(36):
    print("Position {} Fibonacci = {}".format(i, fib(i)))






# ==================================================
# fibonacci numbers: using iterative function
# ==================================================

# Position  = 0,1,2,3,4,5,6,7, 8, 9, 10, 11, 12
# Fibonacci = 0,1,1,2,3,5,8,13,21,34,55, 89, 144,


# def fibonacci(n):
#     if n == 0:
#         result = 0
#     elif n == 1:
#         result = 1
#     else:
#         n_minus1 = 1  # if n = 2, then n_minus1 = 1
#         n_minus2 = 0  # if n = 2, then n_minus2 = 0
#
#         for f in range(1, n):  # NOTE: Range here is (1, n)
#             print("iteration {}".format(f))  # Optional. shows iteration of the range
#             print("Print 1: n = {} : n_minus2 = {} : n_minus1 = {}".format(n, n_minus2, n_minus1))  # Optional print
#             result = n_minus2 + n_minus1
#             print("Print 1: result = n_minus2 + n_minus1 = {} + {} = {}".format(n_minus2, n_minus1, result))
#             n_minus2 = n_minus1
#             print("Print 1: New n_minus2 = n_minus1 = {}".format(n_minus2))
#             n_minus1 = result
#             print("Print 1: New n_minus1 = result = {}".format(n_minus1))
#
#     return result  # Make sure this return is in same indent as else
#
# for i in range(5):
#     print("Print 2: {} fibonacci = {}".format(i, fibonacci(i)))
#     print("=" * 25)

# ================================

# This is same code as above but without the optional prints
# If you run this passing 36 as argument, you see it runs much faster than code Recursive function above
# This is because it does not use recursion (i.e. repeat itself) to get new result

# def fibonacci(n):
#     if n == 0:
#         result = 0
#     elif n == 1:
#         result = 1
#     else:
#         n_minus1 = 1  # if n = 2, then n_minus1 = 1
#         n_minus2 = 0  # if n = 2, then n_minus2 = 0
#         for f in range(1, n):  # NOTE: Range here should be (1, n) and not (1 n+1) like in recursion. otherwise you get wrong numbers
#             result = n_minus2 + n_minus1
#             n_minus2 = n_minus1
#             n_minus1 = result
#     return result
#
# for i in range(36):
#     print("{} fibonacci = {}".format(i, fibonacci(i)))


# =================================================
# How to compare Recursive and Iterative functions
# =================================================


# Fibonnaci: Using Recursive function:
# ====================================

def fib(n):
    """ F(n) = F(n-1) + F(n-2) """
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

# Fibonnaci: Using Iterative function:
# ====================================

def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1  # if n = 2, then n_minus1 = 1
        n_minus2 = 0  # if n = 2, then n_minus2 = 0
        for f in range(1, n):  # NOTE: Range here should be (1, n) and not (1 n+1) like in recursion. otherwise you get wrong numbers
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result

# We will call both methods using this for loop and see the results they produce
# Notice that both Recursive and Iterative codes are producing same results
# But Recursive has r

for i in range(36):
    print("{} fibonacci: Recursive = {}: Iterative = {}".format(i, fib(i), fibonacci(i)))

















