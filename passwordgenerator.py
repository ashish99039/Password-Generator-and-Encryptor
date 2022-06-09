import random

from passwordencrypter import encrypt_password


def generate_password():
    passlen = int(input("Enter the length of the password: "))
    charpool = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    generated_password = "".join(random.sample(charpool, passlen))
    print("Generated Password: ", generated_password)
    encrypt_password(generated_password)
