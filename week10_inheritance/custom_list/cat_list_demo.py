from cat import Cat
from cat_list import CatList

def main():

    # Create 20 cats 
    cat1 = Cat("Whiskers", 2, "gray", 'male', 'short')
    cat2 = Cat("Luna", 4, "black", "female", 'long')
    cat3 = Cat("Oliver", 1, "orange", "male", 'medium')
    cat4 = Cat("Bella", 3, "white", "female", 'short')
    cat5 = Cat("Leo", 5, "brown", "male", 'long')
    cat6 = Cat("Milo", 2, "tabby", "male", 'medium')
    cat7 = Cat("Chloe", 6, "calico", "female", 'long')
    cat8 = Cat("Simba", 4, "golden", "male", 'short')
    cat9 = Cat("Nala", 3, "tan", "female", 'medium')
    cat10 = Cat("Max", 7, "black", "male", 'short')
    cat11 = Cat("Daisy", 1, "white", "female", 'short')
    cat12 = Cat("Oreo", 12, "black and white", "male", 'medium')
    cat13 = Cat("Shadow", 5, "black", "female", 'long')
    cat14 = Cat("Tiger", 8, "orange", "male", 'short')
    cat15 = Cat("Lucy", 4, "gray", "female", 'medium')
    cat16 = Cat("Smokey", 6, "smoke", "male", 'long')
    cat17 = Cat("Mittens", 2, "tabby", "female", 'short')
    cat18 = Cat("Cleo", 9, "calico", "female", 'medium')
    cat19 = Cat("Jasper", 3, "cream", "male", 'long')
    cat20 = Cat("Penny", 5, "brown", "female", 'short')

    # You can start with an empty CatList and then append the cats one by one
    # cat_list1: CatList = CatList()
    # cat_list1.append(cat1)
    # cat_list1.append(cat2)
    # cat_list1.append(cat3)

    # You can also make a list of cats and then use the whole list in the constructor
    cats: list = [cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8, cat9, 
                  cat10, cat11, cat12, cat13, cat14, cat15, cat16, cat17, 
                  cat18, cat19, cat20]
    
    # Make sure you use the asterisk to unpack all the cats into the *args argument.
    cat_list2: CatList = CatList(*cats)

    print(cats)












if __name__ == '__main__':
    main()