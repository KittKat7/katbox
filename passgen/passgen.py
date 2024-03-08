import string
import random
import sys

length = 0
try:
    length = int(sys.argv[1])
except:
    length = 24

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!+-_*?%.{}~'

def generate_password(length):
    #characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print(generate_password(length))
