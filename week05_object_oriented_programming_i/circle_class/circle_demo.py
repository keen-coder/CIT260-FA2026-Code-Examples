from circle import Circle


def main():

    # Create a default circle
    circle1 = Circle()

    # Create a circle given a radius
    circle2 = Circle(5.7)

    # Print the area of circle1
    print(f'The area of the circle of radius {circle1.get_radius()} is {circle1.area()}')

    # Print the area of circle1
    print(f'The area of the circle of radius {circle2.get_radius()} is {circle2.area()}')

if __name__ == '__main__':
    main()