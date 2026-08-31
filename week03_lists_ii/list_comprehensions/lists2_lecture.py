# List Comprehension Syntax:
# result = [result_expression iteration_expression filter_expression]
#   result_expression: what you want to do to the result that is plugged into
#                      the resulting list. you don't have to do anything to the
#                      result, or you can alter the value before it is placed
#                      into the result list.
#   iteration_expression: a for loop that iterates over the list
#   filter_expression:  an option if-expression which is applied to each value
#                       to determine if that value should be placed in the resulting
#                       list.

values1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mult10 = [v * 10 for v in values1]
print(mult10)

# for v in values1:
#     mult10.append(v*10)
# print(mult10)


# COPY A LIST
copy = [v for v in values1]

# TRANSFORM A LIST OF NUMBERS (squares, cubes, >, <, -/+)
values1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cubes = [v ** 3 for v in values1]
print(cubes)

values2 = [-1, 10, -34, 50, 60, -216, -42, 1000, -7]
negatives = [v for v in values2 if v < 0]
print(negatives)

signs = ['-' if v < 0 else '+' for v in values2]
print(signs)



# STRINGS: (lengths of words)
games = ['Minecraft', 'Elden Ring', 'Grounded', 'Fallout 76', 'Diablo II', 'Last Epoch', 'Hollow Knight', 'Silksong', 'Hollow Knight: Silksong', 'Final Fantasy XIV', 'Guild Wars 2']

name_lengths = [g for g in games if len(g) < 11]
print(name_lengths)


# FILTERING

# CREATE A LIST OF ALL CHARACTERS IN A STRING EXCEPT THE SPACES
string1 = 'the quick brown fox jumped over the lazy@dog!'
string2 = [l for l in string1 if l != ' ']
print(string2)


# CREATE A LIST OF BOOLEANS FOR NUMBERS > < 10

# Float value Data Transformation Example (Do together in class)

# Read the data
with open('week03_lists_ii/list_comprehensions/mixed_values.txt', 'r') as f:
    data = [float(line.strip()) for line in f if line.strip().replace('.','',1).isdigit()]
    print(data)

# Process the data with a list comprehension. Keep only valid price data.
# Use .replace(,,1) and .isdigit()