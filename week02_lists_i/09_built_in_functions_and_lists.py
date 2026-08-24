import random

# Python has many built-in functions that can work with lists. del, sum(), min,
# max() and len() just to name a few.

# If you want to remove something from the list at a specific index, use the del statement
colors = ['red', 'green', 'blue', 'red', 'purple']
del colors[3]
print(colors)

# sum() can return the sum of a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = sum(numbers)
print(f'the sum of {numbers} = {sum}')

# min() and max() can find the min and max of a list
min_max = []

for x in range(0, 10):
    min_max.append(random.randint(0, 100))

print(min_max)
print(min(min_max))
print(max(min_max))