import re

phone_numbers = []
regex1 = r'^\([0-9]{3}\)[0-9]{3}-[0-9]{4}$' # matches (xxx)xxx-xxxx
regex2 = r'^[0-9]{3}[0-9]{3}[0-9]{4}$'      # matches xxxxxxxxx
regex3 = r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$'    # matches xxx-xxx-xxxx

with open('week09_regular_expressions/regex/phone_numbers.txt', 'r') as phone_file:
    phone_numbers = [number.strip() for number in phone_file.readlines()]

print('Valid / Invalid Phone Numbers')
for number in phone_numbers:
    is_match = re.fullmatch(regex1, number) or \
               re.fullmatch(regex2, number) or \
               re.fullmatch(regex3, number)
    print(f'{number}\t=\t{(is_match != None)}')