# Calculator
def add(a, b):
    return a + b


def sub(a, b):
    return a-b


def mult(a, b):
    return a*b


def qdiv(a, b):
    return a/b


def rdiv(a, b):
    return a%b


print("Enter operation and number: eg.\n| 5    | \n|  x   |\n| 2    |")
A = int(input(" "))
C = input(" ")
B = int(input(" "))

if C == "+":
    print("__________________\n", add(A, B))
elif C == "-":
    print("__________________\n", sub(A, B))
elif C == "/":
    print("__________________\nQuotient = ", qdiv(A, B), " Remainder = ", rdiv(A, B))
elif C == "*" or "x" or "X":
    print("__________________\n", mult(A, B))
else:
    print("Invalid Input")