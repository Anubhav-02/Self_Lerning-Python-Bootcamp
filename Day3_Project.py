print("Welcome to the Treasure Hunt Game!")
print("Your mission is to find the treasure.")

print('''You're at a crossroad. Where do you want to go?
Type "left" or "right": ''')

direction = input().lower()

if direction == "left":
    print("You fell into a hole. Game Over.")
elif direction == "right":
    print('''You've come to a lake. There is an island in the middle of the lake.
Type "wait" to wait for a boat or "swim" to swim across: ''')
    action = input().lower()

    if action == "wait":
        print('''You arrive at the island unharmed.
There is a house with 3 doors: one red, one yellow, and one blue. 
Which color do you choose?''')
        door = input().lower()

        if door == "red":
            print("You fell into lava. Game Over.")
        elif door == "yellow":
            print("Congratulations! You found the treasure. You win!")
        elif door == "blue":
            print("You were shot by an assassin. Game Over.")
        else:
            print("Invalid door choice. Game Over.")
    elif action == "swim":
        print("You were eaten by crocodiles. Game Over.")
    else:
        print("Invalid action. Game Over.")
else:
    print("Invalid direction. Game Over.")
