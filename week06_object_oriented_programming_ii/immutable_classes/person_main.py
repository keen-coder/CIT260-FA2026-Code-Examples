from birthday import Birthday
from person import Person

def main():
    # Create a birthday and a person.
    bday = Birthday(1,1,1970)
    person = Person('Sue Smith', 33, bday, ['red', 'orange', 'green'])
    # Person and Birthday should both be immutable


    # If my Birthday class was not immutable (in this case if it has a setter),
    # Then I would be able to do change the person's birthday
    person.get_birthday().set_month(100) # This line of code shouldn't work if 
                                         # Birthday is immutable (has no setters)

    # If my Person class didn't account for the list, then I would be able to 
    # bypass Person's immutability and change the list anyway
    person.get_fav_colors()[0] = 'PINK' # This should not work if I correctly
                                        # stored my list of colors as a tuple                                     



if __name__ == '__main__':
    main()