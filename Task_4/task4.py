import random
import time
import simple_colors

title = ["Rock", "Paper", "Scissors"]
print(simple_colors.cyan('Rock-Paper-Scissors', 'bold'))
user = input("Enter your choice: ")
rps = ["Paper", "Rock", "Scissors"]
if user not in rps:
    print("Invalid Choice !")
    user = input("Enter your choice: ")
comp = random.choice(rps)
for i in title:
    print(simple_colors.magenta("\r" + i, "bold"), end=" ")
    time.sleep(0.75)
print(simple_colors.magenta("\rGo !", "bold"))

print("Computer's choice :", simple_colors.yellow(comp, "bold"))
if user < comp:
    if ord(user[0]) + 3 == ord(comp[0]):     # paper rock scissors
        print(simple_colors.red("Computer won !", "bold"))
    else:
        print(simple_colors.green("You won !", "bold"))
elif user[0] == comp[0]:
    print(simple_colors.blue("Draw", "bold"))
else:
    print(simple_colors.red("Computer won !", "bold"))
