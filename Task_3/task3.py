import random
import simple_colors

Capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Small = "abcdefghijklmnopqrstuvwxyz"
Special = "~`@!#$%^&*()_+{}:;/?"
num = "1234567890"
password = ""
char = [Capital, Special, Small, num]
length = int(input(simple_colors.yellow("Enter length of password :")))
for i in range(length):
    for j in random.choices(char,):
        password += random.choice(j)
        break

print(simple_colors.green("Password :"), simple_colors.red(password))
