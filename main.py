from passwordencrypter import encrypt_password
from passwordgenerator import generate_password


print("Do you want a computer generated password?")
print('Enter "Yes" or "No" ')
choice = input()

if choice == "Yes" or choice == "yes":
    generate_password()

elif choice == "No" or choice == "no":
    print("Enter the Password: ")
    password = input()
    encrypt_password(password)

else:
    print("Invalid Input")