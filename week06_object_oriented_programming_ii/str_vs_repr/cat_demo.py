from cat import Cat

def main():
   







    cat1 = Cat(name=Whiskers, age=2, color='gray', gender='male', fur_length='short')




    cat1 = Cat('Whiskers', 2, 'gray', 'male', 'short')
    cat2 = Cat('Luna', 4, 'black', 'female', 'long')
    cat3 = Cat('Oliver', 1, 'orange', 'male', 'medium')
    cat4 = Cat('Bella', 3, 'white', 'female', 'short')
    cat5 = Cat('Leo', 5, 'brown', 'male', 'long')

    cat_list = [cat1, cat2, cat3]
    
    print(cat_list)

    # # print(cat1)
    # for cat in cat_list:
    #     print(cat)

    # print(cat_list)

    # # Using the __str__() method when printing the object
    # print('Print cat1 using print(cat1) (calls __str__()):')
    # print(cat1)
    # print()
    
    # # Using the __str__() method when converting the object to a string
    # print('Print cat1 using string concatentation and the str(cat1) function (calls __str__()): ')
    # print('Cat Information is:\n' + str(cat1))
    # print()

    # # Using the __str__() method when printing the object in an f-string
    # print('Print cat1 using an f-string (calls __str__())')
    # print(f'{cat1}')

    # # Creating a list of Cats
    # cat_list = [cat1, cat2, cat3, cat4, cat5]

    # # When you print the list without looping through it, this will use the __repr__() function.
    # print(cat_list)



if __name__ == '__main__':
    main()