# Table of student data
students = [
    ["Name",    "Age", "Grade"],
    ["Alice",   20,    "A"],
    ["Bob",     22,    "B"],
    ["Charlie", 21,    "C"]
]

for row in students:
    print(row)

# Printing a 2D List row by row (no indexing)
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row in matrix:
    for col in row:
        print(col, end=' ')
    print()

print()
# Printing a 2D List row by row (with indexing)
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row in range(0, len(matrix)):
    for col in range(0, len(matrix[row])):
        print(matrix[row][col], end=' ')
    print()

print()


# Printing a 2D list col by col with indexing
# NOTE: This only works if your list dimensions are the same
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row in range(0, len(matrix)):
    for col in range(0, len(matrix[row])):
        print(matrix[col][row], end=' ')
    print()
print()

# # Printing a 2D list col by col when the dimensions are not uniform

# matrix = [[1, 2, 3],
#           [4, 5],
#           [6],
#           [7, 8, 9, 10]]

# # Find the number of columns
# # Use a list comprehension to create a list of row lengths
# # Find the maximum value from the resulting list comprehension
# print([len(row) for row in matrix])
# max_cols = max([len(row) for row in matrix])

# for col in range(max_cols):
#     for row in range(len(matrix)):
#         if col < len(matrix[row]):  # only print if element exists
#             print(matrix[row][col], end=" ")
#     print()

# Col by Col non-jagged, non-uniform
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12]]

print('col by col print')
for col in range(len(matrix[0])):
    for row in range(len(matrix)):
        print(matrix[row][col], end=" ")
    print()


# Setup a 2D list given predetermined dimensions

rows = 5
cols = 7

# Create a table with default values with 5 rows and 10 columns
# You can use a loop later to populate the table with other data.
table = [[0]*cols]*rows

for row in range(len(table)):
    for col in range(len(table[row])):
        print(table[row][col],'', end='')
    print()

table = []

for row in range(rows):
    table.append([])
    for col in range(cols):
        table[row].append(0)

print(table)
