import random
from week08_sets_object_io_oop_i.object__oriented_programming.coin_class.coin import Coin

# The main function.
def main():
    # Create an object from the Coin class.
    my_coin = Coin()

    # Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())

    # Toss the coin.
    print('I am tossing the coin...')
    my_coin.toss()

    # But now I'm going to try to cheat! I'm going to try to
    # directly change the value of the object's
    # sideup attribute to 'Heads'.
    # It doesn't work because sideup was declared to be private!
    my_coin.sideup = 'Heads'

    # Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())
    
# Call the main function.
if __name__ == '__main__':
      main()