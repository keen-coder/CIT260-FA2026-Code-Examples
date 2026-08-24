import snippets

# To append data to a file, (add data to the end of the file without deleting the old data), 
# open the file in append mode.

PATH = 'week01_review/chapter06/'

def main():
    # open the file in write mode
    # Note the relative path used here.  This will put the output file in the chapter06 package
    output_file = open(PATH + 'append_data.txt', 'a')

    output_file.write("\nThis is new data, and should be added to the end.")

    output_file.close()    

if __name__ == '__main__':
    main()