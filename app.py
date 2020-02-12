import random


chars = "@#$%123456abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
password = ""
pass_size = int(input("Enter password size: "))

for char in range(0, pass_size):
    char = chars[random.randrange(0, len(chars))]
    password += char

print(password)