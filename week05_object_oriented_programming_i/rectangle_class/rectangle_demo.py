from rectangle import Rectangle

def main():
    # Default rectangle
    rect1: Rectangle = Rectangle()
    rect2: Rectangle = Rectangle(10.43, 34.29)

    # Rectangle 1 information
    print(f'Rectangle 1:')
    print(f'\theight = {rect1.get_height()}')
    print(f'\twidth = {rect1.get_width()}')
    print(f'\tperimeter = {rect1.perimeter()}')
    print(f'\tarea = {rect1.area()}')
    print()
    
    # Rectangle 1 with __str__ method
    print(rect1)
    print()

    # Rectangle 2 information
    print(f'Rectangle 2:')
    print(f'\theight = {rect2.get_height()}')
    print(f'\twidth = {rect2.get_width()}')
    print(f'\tperimeter = {rect2.perimeter()}')
    print(f'\tarea = {rect2.area()}')
    print()

    # Rectangle 2 with __str__ method
    print(rect2)







if __name__ == '__main__':
    main()