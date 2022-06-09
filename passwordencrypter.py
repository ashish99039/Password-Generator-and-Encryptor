import rsa


def encrypt_password(password):
    publickey, privatekey = rsa.newkeys(1024)
    encpassword = rsa.encrypt(password.encode(), publickey)
    decpassword = rsa.decrypt(encpassword, privatekey).decode()

    print("Encrypted Password: ", encpassword)
    print("Decrypted Password: ", decpassword)
