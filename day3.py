print("Welcome to Treasure Island.Your mission is to find the treasure.")
a = input("Left or Right /LR")

if a == "L":
    b = input("Swim or Wait /SW")
    if b == "W":
        c = input("Which Door? Red Blue or Yellow?")
        if b == "Red":
            print("Burned by fire! Game over")
        elif b == "Blue":
            print("Eaten by beasts!. Game Over")
        elif b == "Yellow":
            print("You Win!")
        else:
            print("Game Over")
    else:
        print("Attacked by trout! Game Over")
else:
    print("Fall into a hole. Game over")

