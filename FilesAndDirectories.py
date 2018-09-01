
# ===============================================
# OS File system, Recursion
# ===============================================

# There are useful places where recursive functions can be very useful.
# For example if we want to get a directory listing of computer file system
# Modern computer file systems are recursive in the sense that a directory can itself contain other directories
# So once a function has listed all the objects in one directory, it can call itself again for all
# the objects that are themselves directories. This is a good use for a recursive function.

# We will import the "OS Module" to get directory listing
# this is also useful for checking if something is in a directory

# We will write a function that will also verify if the directory passed to it does in fact exist
# before it attempts to do anything else

# If you want to list the subdirectories, the "OS Module" provides a "walk" function that will do that for you
# check here for more info on "walk" function
# https://docs.python.org/3/library/os.html

# os.walk(top, topdown=True, onerror=None, followlinks=False)
# Generate the file names in a directory tree by walking the tree either top-down or bottom-up.
# For each directory in the tree rooted at directory top (including top itself),
# it yields a 3-tuple (dirpath, dirnames, filenames).

# os.walk() function returns a tuple containing directory name and two lists
# root = directory
# directories = list 1
# files = list 2

# When we run this code, it generates the directory and files under this windows file system
# C:\Users\moe\Documents\Python\IdeaProjects\33_ScopeAndNamespace
# This is where the root file is located. then it lists idea as a subdirectory and also lists the files under root 33_ScopeAndNamespace
# It also goes to subfolder .idea and lists the files under it.

import os

listing  = os.walk('.')  # NOTE: '.' is the current directory where 33_ScopeAndNamespace exists

for root, directories, files in listing:  #
    print("root = {}".format(root))
    for d in directories:
        print("directory = {}".format(d))
    for file in files:
        print("file = {}".format(file))

# ===========================================

# Now we will create a function that checks to make sure the directory passed to the function actually exists.
# Then it will call a nested function that will recursively visit all subdirectories and display its contents.


import os

def list_directories(s):

    def dir_list(d):
        # if using global, it gives error "NameError: name 'tab_stop' is not defined"
        # global keyword tells python to look for variable in the global scope, which is the modules namespace


        # global tab_stop  # commented out because it gives error

        # nonlocal keyword tells python to look for variable in the enclosing scopes.
        # it will not check the variable in the global namespace
        # here we have an embedded function that we did not have in the blackjack program, and that's why global keyword did not work

        nonlocal tab_stop  # use nonlocal (python 3) to specify scope of a variable
        files = os.listdir(d)  # listdir is a OS module function that Return a list containing the names of the entries in the directory given by path
        for f in files:
            current_dir = os.path.join(d, f)  # Joins directory (d) and file (f) and makes a path
            if os.path.isdir(current_dir):  # Checks if os.path is directory current_dir
                print("\t" * tab_stop + "Directory " + f)
                tab_stop += 1
                dir_list(current_dir)  # calls function dir_list(itself) again. recursion
                tab_stop -= 1
            else:
                print("\t" * tab_stop + f)  # if its not a directory, we print the details of that file.

    tab_stop = 0  # We initialize tab_stop here. This is to indent or tab the results

    # Now we make sure that the starting directory passed to this function actually exists.
    if os.path.exists(s):
        print("Directory listing of " + s)
        # Then it will call nested function dir_list that will recursively visit all subdirectories and display their contents.
        # NOTE that dir_list function is only needed in this list_directories function, hence can be defined inside list_directories function
        # This is a function within a function
        dir_list(s)  # function dir_list is called here
    else:
        print(s + " does not exist")

# Call list_directories function and give it current file location '.'

list_directories('.')

# Note that the only things that create scope in python are:
# Modules, Functions, and classes



