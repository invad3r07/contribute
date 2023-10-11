#importing module for random number generation
import random

min_val = 1
max_val = 6

def roll_dice():
    while True:
        roll_again = input("Do we roll the dice again (YES/y or NO/n): ").lower()
        if roll_again == "yes" or roll_again == "y":
            print("Rolling The Dice...")
            val_1 = random.randint(min_val, max_val)
            val_2 = random.randint(min_val, max_val)
            print(f"The Values are: {val_1}, {val_2}")
        elif roll_again == "quit" or roll_again == "q":
            break
        else: print("Please input valid values")

if __name__ == "__main":
    roll_dice()

