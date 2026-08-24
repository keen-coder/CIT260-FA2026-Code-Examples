PATH = 'week01_review/chapter06/'

def main():
    # open the file in read mode using the 'r' argument
    input_file = open(PATH + 'my_data.txt', 'r')
   
    file_data = input_file.readlines()

    print(file_data)

if __name__ == '__main__':
    main()