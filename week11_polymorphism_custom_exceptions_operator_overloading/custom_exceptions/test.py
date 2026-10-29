def main():
    dict1 = {"blue": 12, "green": 37}

    try:
        print(dict1['red'])
    except KeyError as ke:
        print(f'Key {ke} does not exist')


main()