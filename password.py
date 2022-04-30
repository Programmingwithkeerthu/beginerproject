import random
import string


def generate_random_value():
    print('Start generating a random value........')
    alpha = list(string.ascii_letters)
    digits = list(string.digits)
    print(digits)
    special_char = '!@#$%^&*()'
    
    var = [alpha, digits, special_char]
    
    password = ''

    for i in range(6):
        password += random.choice(random.choice(var))
    
    print(password)

if __name__ == '__main__':
    generate_random_value()
   