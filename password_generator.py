import string
from random import choice


def password_generator():
    strength = int(input("How strong would you like your password? "))
    password = ''
    for item in range(1, strength + 1):
        alphanum = string.ascii_letters + string.digits
        rand_alphanum = choice(alphanum)
        password += rand_alphanum
    return password

print(password_generator())


##########

import random
import string

s = string.ascii_letters + string.digits
passlen = int(input("How strong of a password? "))
p = ''.join(random.sample(s, passlen))
print(p)