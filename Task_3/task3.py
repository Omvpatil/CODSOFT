import random

Capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Small = "abcdefghijklmnopqrstuvwxyz"
Special = "~`@!#$%^&*()_+{}:;/?"
num = "1234567890"
password = ""
char = [Capital, Special, Small, num]
length = int(input("Enter length of password :"))
for i in range(length):
    for j in random.choices(char,):
        password += random.choice(j)
        break

print("Password :", password)
