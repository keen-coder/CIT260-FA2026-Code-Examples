# This program uses the writelines method to save
# a list of strings to a file.

PATH = 'week02_lists_i/lists_and_file_io/'

def main():
    # Create a list of strings.
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas']

    # Write the list to a file.
    with open(PATH + 'cities.txt', 'w') as outfile:
        outfile.writelines(cities)

# Call the main function.
if __name__ == '__main__':
    main()