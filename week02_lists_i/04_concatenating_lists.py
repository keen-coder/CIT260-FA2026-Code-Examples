# ------------------------------------------------------------------------------
# File:         04_concatenating_lists.py
# Description:  Demonstrates how to use the + operator to concatenate two or more
#               lists into a new list.
# ------------------------------------------------------------------------------

# Lists can be concatenated (combined) into a new list using the + operator.
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = list1 + list2
print(list3)    # prints [1, 2, 3, 4, 5, 6, 7, 8]

# The += operator also works
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list1 += list2
print(list1)    # prints [1, 2, 3, 4, 5, 6, 7, 8]

# Example with strings
girl_names = ['Joanne', 'Karen', 'Lori']
boy_names = ['Chris', 'Jerry', 'Will']
all_names = girl_names + boy_names
print(all_names)    # ['Joanne', 'Karen', 'Lori', 'Chris', 'Jerry', 'Will']