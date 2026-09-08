import math

def main():
    colors = ['Blue', 'red', 'orange', 'green', 'blue', 'pink', 'blue', 'Purple', 'green']

    colors.sort(key=str.lower)

    print(colors)



if __name__ == '__main__':
    main()