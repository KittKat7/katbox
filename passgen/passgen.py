import string
import random

def generate_password(length: int):
    #characters = string.ascii_letters + string.digits + string.punctuation
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!+-_*?%.{}~'
    password = ''.join(random.choice(characters) for i in range(length))
    return password


def main(args: list[str]):
    length = 0
    try:
        length = int(args[0])
    except:
        length = 16


    print(generate_password(length))
