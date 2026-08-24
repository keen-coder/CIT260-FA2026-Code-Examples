# ------------------------------------------------------------------------------
# File:         05_list_mutability.py
# Description:  Demonstrates how to use the + operator to concatenate two or more
#               lists into a new list.
# ------------------------------------------------------------------------------

# Lists are MUTABLE. Mutable objects in python are objects whose contents can
# be changed after the object has been created. By using indexing, we can assign
# a new value to that specific index (position) in a list.
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Change index 0 to 99
numbers[0] = 99
numbers[2] += 1
print(numbers)

# NOTE: The index must be within bounds or else you will raise an IndexError
# numbers[10] = 42    # Raises an IndexError

# Initalize 