from fan import Fan

def main():
    # Default Fan
    fan1: Fan = Fan()
    fan2: Fan = Fan(Fan.FAST, False, 7.43, 'pink')

    print(f'Fan 1:\t{fan1}')
    print(f'Fan 2:\t{fan2}')

    fan1.turn_on
    fan2.turn_on

    fan1.set_speed(Fan.MEDIUM)
    fan2.set_speed(Fan.SLOW)

    fan1.set_color('aquamarine')

    print()
    print(f'Fan 1:\t{fan1}')
    print(f'Fan 2:\t{fan2}')



if __name__ == '__main__':
    main()