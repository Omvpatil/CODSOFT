import random
import time
from simple_colors import *
title = ["Rock", "Paper", "Scissors"]
print(cyan('Rock-Paper-Scissors', 'bold'))
user = input("Enter your choice: ")
rps = ["Paper", "Rock", "Scissors"]
if user not in rps:
    print("Invalid Choice !")
    user = input("Enter your choice: ")
comp = random.choice(rps)

for i in title:

    print(magenta("\r" + i, "bold"), end=" ")
    time.sleep(0.75)
print(magenta("\rGo !", "bold"))

print("Computer's choice :", yellow(comp, "bold"))
if user[0] < comp[0] and comp == "Scissors":
    print(green("You won !", "bold"))
elif user[0] == comp[0]:
    print(blue("Draw", "bold"))
else:
    print(red("Computer won !", "bold"))
