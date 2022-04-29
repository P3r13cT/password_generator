from random import choice
from time import sleep


def generate_password(amount, length, chars):
    password = ''
    for _ in range(amount):
        for _ in range(length):
            password += choice(chars)
        print(password)
        password = ''
        sleep(0.001)


digits, lowercase = list('0123456789'), list('abcdefghijklmnopqrstuvwxyz')
uppercase, symbols = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), list('!#$%&*+-=?@^_')
chars = []
entering = True
while entering:  # A lot of fool-proofing
    amount = input('Enter amount of passwords generated: ')
    if amount.isdigit() is True and int(amount) > 0:
        amount = int(amount)
        entering = False
entering = True
while entering:
    length = input('Enter length of password(s): ')
    if length.isdigit() is True and int(length) > 0:
        length = int(length)
        entering = False
response = input('Include digits? (y/n)')
if not response.lower() == 'n':
    chars += digits
response = input('Include uppercase letters? (y/n)')
if not response.lower() == 'n':
    chars += uppercase
response = input('Include lowercase letters? (y/n)')
if not response.lower() == 'n':
    chars += lowercase
response = input('Include symbols? (y/n)')
if not response.lower() == 'n':
    chars += symbols
print('Your password(s):')
generate_password(amount, length, chars)
