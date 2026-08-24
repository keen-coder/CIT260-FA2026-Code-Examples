# ------------------------------------------------------------------------------
# File:         03_indexing_len_function_indexing_with_for_loop.py
# Description:  Demonstrates how to use the len() function to get the length /
#               size of the list. Also demonstrates indexing with lists and using
#               list indexing with for loops.
# ------------------------------------------------------------------------------

# Indexing allows you to access specific elements of a lists. The index of a list
# always starts from 0 and goes to len(list) - 1. Indexes that are greater than
# the maximum index will cause your program to crash with an IndexError

animals = ['tiger', 'otter', 'falcon', 'panda', 'koala', 'dolphin', 'lemur']
print(animals[0])   # prints 'tiger'
print(animals[4])   # prints 'panda'
print(animals[6])   # prints 'lemur'
print(animals[len(animals) - 1])
# print(animals[7])   # Crashes the program with an IndexError

# The built-in len() function can tell you the size/length (number of elements)
# that are in the list.
num_animals = len(animals)
print(num_animals) # prints 7

# Using a combination of indexing, the len() function, and the range() function,
# you can also iterate over a list. This method gives you more control over how 
# you might want to iterate over the list.

# Iterating over a list from beginning to end with indexing
for index in range(len(animals)):
    print(animals[index], end=' ')
print()

# Iterating over a list backwards
index = len(animals) - 1
while index >= 0:
    print(animals[index], end=' ')
    index -= 1
print()

# Iterating over a list starting at index 0 and skipping every other element.
for index in range(0, len(animals), 2):
    print(animals[index], end=' ')