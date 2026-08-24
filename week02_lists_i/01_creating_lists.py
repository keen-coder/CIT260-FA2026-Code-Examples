# ------------------------------------------------------------------------------
# File:         01_creating_lists.py
# Description:  Demonstrates many different ways in which you can create lists.
# ------------------------------------------------------------------------------

# The first and simplest way to create a list is to simply hard code a list in
# your program. Lists contain a comma-separated sequence of elements surrounded
# by square brackets. Lists can contain any type of data and are usually assigned
# to a variable name.

import random

numbers = [32, 56, 19, 123, 49548]
costs = [4.56, 23.90, 582.23]
people = ['Abby', 'George', 'Samantha', 'Susie', 'Kevin']

# Lists in Python can also have mixed data-types, but these are harder to 
# consistently process.
student_info = ['Jane Smith', '5705555555', 23, 4.5]

# Lists can also be created using the range() and list() built-in functions
numbers = list(range(5))            # [0, 1, 2, 3, 4]
numbers = list(range(1, 10, 5))     # [1, 6]

# You could even use the random module in python to assign random values to 
# a list using a for loop. Here we create a list of 10 random values ranging 
# from 25 to 43 (non-inclusive).
random_list = []
for x in range(10):
    random_list.append(random.randint(25, 43))

# Lists can also be created using the repetition operator (*)
zeros = [0] * 7     # [0, 0, 0, 0, 0, 0, 0]

list1 = [1, 2, 3]
list2 = list1 * 3   # [1, 2, 3, 1, 2, 3, 1, 2, 3]