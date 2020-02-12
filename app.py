import random


def password_size():
    size = 0
    while True:
        try:
            size = int(input("Enter password size: "))
            if size < 6:
                print("Password size must be 6 chars min")
            else:
                return size
        except:
            print("Please enter a number")


chars = "@#$%123456abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
password = ""
pass_size = password_size()

for char in range(0, pass_size):
    char = chars[random.randrange(0, len(chars))]
    password += char

print(password)
