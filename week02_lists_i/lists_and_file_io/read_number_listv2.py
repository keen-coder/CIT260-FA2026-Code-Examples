# This program reads numbers from a file into a list.

PATH = 'week02_lists_i/lists_and_file_io/'

def main():
    # Read the contents of the file into a list.
    with open(PATH + 'numberlist.txt', 'r') as infile:
        numbers = infile.readlines()
        print(numbers)

    # Convert each element to an int.
    for index in range(len(numbers)):
        numbers[index] = int(numbers[index])

    # Print the contents of the list.
    print(numbers)

# Call the main function.
if __name__ == '__main__':
    main()