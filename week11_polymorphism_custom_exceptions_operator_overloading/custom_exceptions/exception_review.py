def divide(n: float, d: float) -> float:
    if d == 0:
        raise ValueError('Denominator (d) cannot be 0')
    
    return n / d

def root(x) -> float:
    if x < 0:
        raise ValueError('ERROR: Negative Root')
    
    return x**(1/2)
    
def main():
    try:
        print(divide(10, 0))
    except ValueError as ve:
        print('Recovered from division error')

    try:
        print(root(-10))
    except ValueError as ve:
        print('Recovered from negative root error')

    print('Program continues....')

    colors = ['red', 'green', 'blue']

    try:
        print(colors[100])
    except IndexError as ie:
        print('Recovered from IndexError')

    print('Program continues....')

if __name__ == '__main__':
    main()
