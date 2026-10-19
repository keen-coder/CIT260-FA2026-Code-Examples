from cat import Cat

class CatList(list[Cat]):
    
    # Allows you to create an empty cat list or a new cat list given a normal
    # list.

    # Review how the *args parameter works
    def __init__(self, *cats: list[Cat]):
        print(cats[1])
        
        # Add each cat to itself (CatList is a list since it is a subclass of list)
        for cat in cats:
            self.append(cat)

    def print_cats(self):
        for cat in self:
            print(cat)

    def fur_length_count(self, fur_length):
        count = 0

        for cat in self:
            if cat.get_fur_length() == fur_length:
                count += 1

        return count

    def oldest_cat(self):

        current_old_cat = self[0]

    
        for i in range(1, len(self)):
            next_cat = self[i]

            if next_cat.get_age() > current_old_cat.get_age():
                current_old_cat = next_cat
            
        return current_old_cat


