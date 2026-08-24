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
print(days_one)

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
days_slice = days[-5:-1] # [2, 6]
print(days_slice)

# You can get a reverse of a list using the following:
days_reverse = days[::-1]
print(days_reverse) 