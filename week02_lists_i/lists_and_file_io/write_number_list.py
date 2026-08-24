# This program saves a list of numbers to a file.

PATH = 'week02_lists_i/lists_and_file_io/'

def main():
    # Create a list of numbers.
    numbers = [1, 2, 3, 4, 5, 6, 7]

    # Write the list to the file.
    with open(PATH + 'numberlist.txt', 'w') as outfile:
        for item in numbers:
            outfile.write(str(item) + '\n')

# Call the main function.
if __name__ == '__main__':
    main()