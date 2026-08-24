# This program reads numbers from a file into a list.

PATH = 'week02_lists_i/lists_and_file_io/'

def main():
    numbers = []
    # Read the contents of the file into a list.
    with open(PATH + 'numberlist.txt', 'r') as infile:
        for item in infile:
            numbers.append(int(item))
    
    # Print the contents of the list.
    print(numbers)

# Call the main function.
if __name__ == '__main__':
    main()