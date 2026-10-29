from custom_exceptions import *


def divide(n: float, d: float) -> float:
    if d == 0:
        raise DivisionByZeroError('Denominator (d) cannot be 0')
    
    return n / d

def root(x) -> float:
    if x < 0:
        raise NegativeRootError('ERROR: Negative Root', x)
    
    return x**(1/2)
    
def main():
    try:
        print(divide(10, 0))
    except DivisionByZeroError as dbze:
        print(str(dbze))
        print('Recovered from division error')

    try:
        print(root(-10))
    except NegativeRootError as nre:
        print(nre)
        print('Recovered from negative root error')

    print('Program continues....')

if __name__ == '__main__':
    main()
