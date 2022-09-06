import random

while True:
    a= input("Rock paper or scissors? R P C: ")
    b = ["R", "P", "C"]
    x=b[random.randint(0, 2)]
    if a == x:
        print(x)
        print("Try Again")
    if x == "R" and a == "P":
        print(x)
        print("You Win")
        break
    elif x == "C" and a == "R":
        print(x)
        print("You Win")
        break
    elif x == "P" and a == "C":
        print(x)
        print("You Win")
        break
    else:
        print(x)
        print("You Lose!")
        break


