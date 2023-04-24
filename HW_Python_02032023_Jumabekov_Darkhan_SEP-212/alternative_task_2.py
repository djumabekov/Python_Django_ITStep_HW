'''
Задание 2.
Напишем программу для создания надежного пароля.
'''

import random
import string

def create_reliable_password():

    # берем необходимые символы с констант модуля string
    s0 = string.ascii_lowercase
    s1 = string.ascii_uppercase
    s2 = string.digits
    s3 = string.punctuation
    s = s0 + s1 + s2 + s3

    password = ""

    for i in range(15):
        p = random.choice(s)
        password = password + p

    print(f"New password [{i}]: {password}")
