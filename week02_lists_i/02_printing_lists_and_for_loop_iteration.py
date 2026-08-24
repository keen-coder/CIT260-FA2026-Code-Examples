# ------------------------------------------------------------------------------
# File:         02_printing_lists_and_for_loop_iteration.py
# Description:  Demonstrates how to print out lists using the print() statement.
#               Also shows how to iterate over lists using loops and printing
#               using loops.
# ------------------------------------------------------------------------------

# Printing a list using a simple print statement. Take note of how the list
# appears in the console when you execute the code.

colors = ['cerulean', 'vermilion', 'sage', 'orchid', 'amber', 
         'teal', 'mauve', 'crimson', 'jade', 'periwinkle']
print(colors)

# You can also iterate over a list using a for loop. This allows you to process
# the list one element at a time.

# Printing the list all in one line, elements separated by spaces
for c in colors:
    print(c, end=' ')

print()

# Printing 5 colors per line, elements separated by /
count = 1

for c in colors:
    if count % 5 == 0:
        print(c, end='\n')
    else:
        print(c, end='/')
    count+=1

print()

# Print each color, one color per line.
for c in colors:
    print(c)

# NOTE: The variable in the for loop which is assigned each element of the list
# CANNOT be used to change the contents of the list

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    n = 100
print(numbers)