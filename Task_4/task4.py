import random
import time

print("Rock-Paper-Scissors")
user = input("Enter your choice: ")
rps = ["Rock", "Paper", "Scissors"]
comp = random.choice(rps)

# Display countdown
for i in rps:
    print("\r" + i, end="")
    time.sleep(1)
print("\r ")

# Display computer's choice
print("My choice :", comp)
if i[0]>comp[0] and comp is not "Rock":
    print("You won !")
else:
    print("I won !")
