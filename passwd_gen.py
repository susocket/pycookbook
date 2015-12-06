import string
from random import choice
from sys import argv

def make_passwd(length=12):
    if len(argv)==2 and argv[1].isdigit():
        length = int(argv[1])
    #chars = ''.join(set(string.punctuation)-set('\'\"\`|')) + \
    #        string.ascii_letters + string.digits
    chars = string.ascii_letters + string.digits + '!@#$%^&*?'
    return ''.join([choice(chars) for i in range(length)])

if __name__ == '__main__':
    password = make_passwd()
    print(password)