import sys
c = int(input("1.Add task\n2.View Tasks\n3.Delete Tasks\n4.Exit\n"))


def put():
    print("\rEnter choice :")
    a = int(input())
    return a


def add():
    f = open("tasks.txt", "a")
    a = "-"
    print("\rEnter task :")
    b = input()
    f.write(a + b + "\n")
    f.close()
    print("Task Added")


def clear():
    f = open("tasks.txt", "w")
    f.close()
    print("\rAll tasks are cleared")


def display():
    print("Tasks:----------------------")
    f = open("tasks.txt", "r")
    print(f.read())
    f.close()


while c < 4:
    if c == 1:
        add()
        c = put()
    if c == 2:
        display()
        c = put()
    if c == 3:
        clear()
        c = put()
    else:
        break
