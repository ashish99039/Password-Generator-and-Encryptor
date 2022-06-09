from passwordencrypter import encrypt_password


def user_generated_password():
    print("Enter the Password: ")
    password = input()
    encrypt_password(password)
