# Password Generator
import random
import string
from time import sleep


def generate_password(min_length, has_numbers=True, has_specials=True):
    letters = string.ascii_letters
    numbers = string.digits
    specials = string.punctuation

    random_password = ""

    while len(random_password) <= min_length:
        random_password += random.choice(letters)
        if has_numbers:
            random_password += random.choice(numbers)
        if has_specials:
            random_password += random.choice(specials)

    shuffled_password = list(random_password)

    password = "".join(shuffled_password)

    return password


while True:
    try:
        len_pwd = int(input("Enter length of password you want: "))
        contain_numbers = input("Want numbers in your password?(y/n): ").lower() == "y"
        contain_specials = input("Want special chars in your password?(y/n): ").lower() == "y"

        if len_pwd < 5:
            print("Password length should be greater than 5")
        elif len_pwd > 30:
            print("Password length is too long!")
        else:
            pwd = generate_password(len_pwd, contain_numbers, contain_specials)
            print(f"Generated Password is: {pwd}")
            sleep(5)
    except Exception:
        pass
