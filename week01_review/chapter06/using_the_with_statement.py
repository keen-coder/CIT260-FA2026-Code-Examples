# The with statement in python can be used to open a file and automatically close them when
# you are finished with them.
PATH = 'week01_review/chapter06/'

def main():
    sum = 0

    with open(PATH + 'sequence.txt', 'r') as input_file:
        for next_line in input_file:
            num = int(next_line.rstrip('\n'))
            sum += num

            print(num, end=' ')
           
    print()
    print(f'sum = {sum}')
        
    
if __name__ == '__main__':
    main()
