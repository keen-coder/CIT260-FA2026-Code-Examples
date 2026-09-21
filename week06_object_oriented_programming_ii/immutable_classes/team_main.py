from player import Player
from team import Team

def main():
    bob = Player(42, 'Bob')
    team = Team('Wildcats', [bob])


    print(team)

if __name__ == '__main__':
    main()