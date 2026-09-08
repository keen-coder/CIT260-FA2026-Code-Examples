# ------------------------------------------------------------------------------
# File:         06_list_slicing.py
# Description:  Demonstrates how to use slicing syntax to get a copy of a portion
#               of a list.
# ------------------------------------------------------------------------------

# A slice is a span of items extracted from a sequence. Slicing a list means
# that you get a span of elements from the list.

# Slicing Syntax: list_name[start : end : step]
#   start:  the starting index of the slice (default is 0)
#   end:    the ending index of the slice (default is len(list_name)). end index
#           is not included in the slice
#   step:   allows elements to be skipped based on the step value (default is 1)

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 
        'Saturday']

days_one = days[1:2]
day = days[1]
print(days_one)
print(day)

# Get the days from Monday to Thursday
days_slice = days[1:5]
print(days_slice)

# Get the days from Sunday to Thursday
# start value is omitted so defaults to 0
days_slice = days[:5]
print(days_slice)

# get the days from Tuesday to the end of the list
days_slice = days[2:]
print(days_slice)

# get every other day starting with Sunday
days_slice = days[::2]
print(days_slice)

# omitting start and end gives you a COPY of the original list
days_copy = days[:]
print(days_copy)

# Shows that the second list is a copy and changing the copy does not change 
# the original.
print(f'days =\t\t{days}')
print(f'days_copy =\t{days_copy}')
days_copy[3] = 78
print(f'days =\t\t{days}')
print(f'days_copy =\t{days_copy}')

# Negative values can be used to get positions relative to the end of the list
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 
        'Saturday']
days_slice = days[-5:-1] # [2, 6]
print(days_slice)

# You can get a reverse of a list using the following:
days_reverse = days[::-1]
print(days_reverse) 

# You can even assign values using slicing
slice_assign = [0] * 10 # Start with a list of default values to make sure the positions exist
list_a = [1, 3, 5, 7, 9]
list_b = [2, 4, 6, 8, 10]
print(slice_assign)
slice_assign[0::2] = list_a
print(slice_assign)
slice_assign[1::2] = list_b
print(slice_assign)

listA = [1, 2, 3, 4, 5]
listA[1:4] = ['red', 'green', 'blue']
print(listA)

# You can insert values as well without overwriting any values
list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [100, 200, 300]

# Note how the start and end are the same
# This will select an 'empty slice' and basically just insert all values at
# the given postion.
list_a[3:3] = list_b
print(list_a)

# You can even delete a whole chuck of items from your list
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want to remove values 4 6 8 and 10 from the list
del list_a[3::2]
print(list_a)