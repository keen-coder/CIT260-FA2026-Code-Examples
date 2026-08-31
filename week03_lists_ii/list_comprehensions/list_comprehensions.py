PATH = 'week03_lists_ii/list_comprehensions/'

# Copying a list with a list comprehension
# This creates a deep copy as long as all data is immutable.
list1 = [1, 2, 3, 4]
list2 = [item for item in list1]
print('COPY: ', list2)
print()

# Creating a list of squares of numbers 1 ~ 4 
list1 = [1, 2, 3, 4]
list2 = [item**2 for item in list1]
print('SQUARES: ', list2)
print()

# Creates a list of cubes of the values in the original list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cubes = [n**3 for n in numbers]
print('CUBES:', cubes)  
print()

# Creating a list of the lengths of each string from an existing list.
str_list = ['Winken', 'Blinken', 'Nod']
len_list = [len(s) for s in str_list]
print('LENGTHS:', len_list)
print()

# Create a list of values less than 10 from an existing list
list1 = [1, 12, 2, 20, 3, 15, 4]
list2 = [item for item in list1 if item < 10]
print('VALUES < 10:', list2)
print()

# Functions and Methods can be used in the result expression section
words = ["list", "comprehensions", "are", "fun!"]
upper_words = [word.upper() for word in words]
print('UPPERCASE:',upper_words)
print()

# Flatten a nested list
# In this example, note the two for loops, one after another
# These act as nested for loops
#   for row in matrix
#       for num in row
# You could still have an if clause at the end of the loops if necessary
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row] # Note the nested for loop
print('ORIGINAL:', matrix)
print('FLATTENED:', flat)
print()

# Create a list of labels 'even' or 'odd' for an existing list of values
# NOTE: This example uses a conditional expression in the result expression
numbers = [1, 2, 3, 4, 5]
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print('ODD or EVEN:', labels)  # ['odd', 'even', 'odd', 'even', 'odd']
print()

# Read all lines from a file and strip them of whitespace
with open(PATH + 'log.txt') as f:
    lines = [line.strip() for line in f]
    print(lines)

# Print the results
print('LOG FILE CLEANED:')
for line in lines:
    print('\t', line)
print()

# Filter data in a file, choosing only lines that refer to error messages
with open(PATH + 'log.txt') as f:
    errors = [line.strip() for line in f if "ERROR" in line]

# Print the results
print('ONLY ERROR MESSAGES:')
for error in errors:
    print('\t', error)
print()