import random
from week08_sets_object_io_oop_i.object__oriented_programming.coin_class.coin import Coin

# The Coin class simulates a coin that can
# be flipped.

# The main function.
def main():
    # Create an object from the Coin class.
    my_coin = Coin()

    # Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())

    # Toss the coin.
    print('I am tossing the coin...')
    my_coin.toss()

    # Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())
    
# Call the main function.
if __name__ == '__main__':
      main()