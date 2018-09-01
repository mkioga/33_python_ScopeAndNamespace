# ==========================================
# Two or more levels of function nesting
# ==========================================

# Functions can be nested inside other functions and other functions
# It is however rare to have more than one level of nesting.



def spam1():


    def spam2():


        def spam3():
            z = " spam3 text"
            print("spam3 Locals = {}".format(locals()))  # shows variables local to the function. only variable z in spam3
            return z  # returns "spam3 text"

        y = " spam2 text"
        y += spam3()  # Here y is added to z
        print("spam2 Locals = {}".format(locals()))  # variable y and function spam3 are local to spam2
        return y  # returns "spam2 text spam3 text"

    x = "spam1 text"
    x += spam2()  # concatenates spam1 to spam2 (which includes spam3)

    # NOTE that within spam1, we cannot refer to variables y and z, because variables in an inner scope are not available
    # to the outer scope. However inside spam2, we can refer to x and inside spam3, we can refer to both x and y
    # So inner scope has access to variables defined in outer scope and we can use the outer variables in spam2 and spam3
    # We will change the code in next program to make use of outer scope in spam2 and spam3
    print("spam3 Locals = {}".format(locals()))  # variable x and function spam2 are local to spam1
    return x  # returns "spam1 text spam2 text spam3 text"


print(spam1())  # prints "spam1 text spam2 text spam3 text"




# ==================================================
# How to Make use of outer scope in spam2 and spam3
# ==================================================


def spam1():
    # print("="*20)
    def spam2():

        def spam3():
            print("print3: ================")
            z = " spam3"
            print("print3: z = {}".format(z))
            z += y  # Concatenate z to y
            print("print3: New z = z + y  {}".format(z))
            print("print3: spam3 Locals = {}".format(locals()))  # shows variables local to the function. only variable z in spam3
            return z  # returns "spam3 text"

        y = " spam2 " + x  # Contatenate spam2 and spam1. NOTE: y must exist before spam3 is called.
        print("print2: y = {}".format(y))  # prints ==> print2: y =  spam2 spam1
        # Since we are referring to spam3 here, program shifts to spam3 function and goes through spam3 function steps.
        y += spam3()  # Here y is added to z. Do not combine these assignments.

        print("print2: ===============")  # After going through spam3 steps, it comes back to spam2
        print("print2: New y = y + spam3 = {}".format(y))  # New y = initial y (spam2 spam1) + new spam3 or new z (spam3 spam2 spam1)
        print("print2: spam2 Locals = {}".format(locals()))  # variable y and function spam3 are local to spam2
        return y  # returns "spam2 text spam3 text"

    x = "spam1"  # x must exist before spam2 is called.
    print("print1: x = {}".format(x))
    x += spam2()  # concatenates spam1 to spam2 (which includes spam3)
    # Since we referred to spam2 above, it will shift to spam2 function, run through it (which includes spam3), then return to spam1
    print("print1: ================")
    print("print1: new x = x + spam2 = {}".format(x))
    print("print1: spam1 Locals = {}".format(locals()))  # variable x and function spam2 are local to spam1
    print("print1: ================")
    return x  # returns "spam1 text spam2 text spam3 text"


print("Final print: spam1 = {}".format(spam1()))  # prints "spam1 text spam2 text spam3 text"




# ==================================================
# More demonstration of scope
# ==================================================
#
#
# def spam1():
#     # print("="*20)
#     def spam2():
#
#         def spam3():
#             print("print3: ================")
#             z = " spam3"
#             print("print3: z = {}".format(z))
#             z += y  # Concatenate z to y
#             print("print3: New z = z + y  {}".format(z))
#             print("print3: spam3 Locals = {}".format(locals()))  # shows variables local to the function. only variable z in spam3
#             return z  # returns "spam3 text"
#
#         y = " spam2 " + x  # Contatenate spam2 and spam1
#         print("print2: y = {}".format(y))  # prints ==> print2: y =  spam2 spam1
#         # Since we are referring to spam3 here, program shifts to spam3 function and goes through spam3 function steps.
#         y += spam3()  # Here y is added to z
#
#         print("print2: ===============")  # After going through spam3 steps, it comes back to spam2
#         print("print2: New y = y + spam3 = {}".format(y))  # New y = initial y (spam2 spam1) + new spam3 or new z (spam3 spam2 spam1)
#         print("print2: spam2 Locals = {}".format(locals()))  # variable y and function spam3 are local to spam2
#         return y  # returns "spam2 text spam3 text"
#
#     # Here instead of concatenating "x += spam2()" below, we just do "x = "spam1" + spam2()"
#     # When we run this, we get error "NameError: free variable 'x' referenced before assignment in enclosing scope"
#     # This is because spam2 functions tries to use the value of x
#     # but spam2 is called within the initial assignment to x and x does not yet have a value. Hence the error
#
#     x = "spam1" + spam2()
#     print("print1: x = {}".format(x))
#     # x += spam2()  # concatenates spam1 to spam2 (which includes spam3)
#     # Since we referred to spam2 above, it will shift to spam2 function, run through it (which includes spam3), then return to spam1
#     print("print1: ================")
#     print("print1: new x = x + spam2 = {}".format(x))
#     print("print1: spam1 Locals = {}".format(locals()))  # variable x and function spam2 are local to spam1
#     print("print1: ================")
#     return x  # returns "spam1 text spam2 text spam3 text"
#
#
# print("Final print: spam1 = {}".format(spam1()))  # prints "spam1 text spam2 text spam3 text"


# ========================
# Lessons on functions
# ========================

# (1) Whenever possible, only write functions so they only use local variables and parameters
# (2) Only access global and non-local variables when it is absolutely necessary.
# (3) Make sure to make comments explaining your code logic.


# =================================
# Local scope vs global scope
# =================================

# At the module level, the local scope is same as global scope
# LEGB (Local, Enclosing, Global, Variables) This is the sequence which python follows to determine scope
# it first goes to local then to Endlosing, then Global, then Variables.


def spam1():
    # print("="*20)
    def spam2():

        def spam3():
            print("print3: ================")
            z = " spam3"
            print("print3: z = {}".format(z))
            z += y  # Concatenate z to y
            print("print3: New z = z + y  {}".format(z))
            print("print3: spam3 Locals = {}".format(locals()))  # shows variables local to the function. only variable z in spam3
            return z  # returns "spam3 text"

        y = " spam2 " + x  # Contatenate spam2 and spam1. NOTE: y must exist before spam3 is called.
        print("print2: y = {}".format(y))  # prints ==> print2: y =  spam2 spam1
        # Since we are referring to spam3 here, program shifts to spam3 function and goes through spam3 function steps.
        y += spam3()  # Here y is added to z. Do not combine these assignments.

        print("print2: ===============")  # After going through spam3 steps, it comes back to spam2
        print("print2: New y = y + spam3 = {}".format(y))  # New y = initial y (spam2 spam1) + new spam3 or new z (spam3 spam2 spam1)
        print("print2: spam2 Locals = {}".format(locals()))  # variable y and function spam3 are local to spam2
        return y  # returns "spam2 text spam3 text"

    x = "spam1"  # x must exist before spam2 is called.
    print("print1: x = {}".format(x))
    x += spam2()  # concatenates spam1 to spam2 (which includes spam3)
    # Since we referred to spam2 above, it will shift to spam2 function, run through it (which includes spam3), then return to spam1
    print("print1: ================")
    print("print1: new x = x + spam2 = {}".format(x))
    print("print1: spam1 Locals = {}".format(locals()))  # variable x and function spam2 are local to spam1
    print("print1: ================")
    return x  # returns "spam1 text spam2 text spam3 text"

# At the module level, local scope is same as global scope

print("Final print: spam1 = {}".format(spam1()))  # prints "spam1 text spam2 text spam3 text"
print(locals())  # local scope same as global scope
print(globals())  # local scope same as global scope





