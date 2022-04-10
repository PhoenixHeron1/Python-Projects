# Number Guessing Game
import random
import os
import time

def main():
    random_number = random.randint(1, 20)
    print("\nComputer has choosen it's random number")
    user_input = int(input("Enter number: "))


    if user_input == random_number:
        print(f"You guessed the number {user_input} right!!")

    while user_input != random_number:
        if user_input < random_number:
            print("Guess is a very low\n")
        elif user_input > random_number:
            print("Guess is too high\n")
        user_input = int(input("Enter number: "))
        
    if user_input == random_number:
        print(f"You guessed the number {user_input} right!!")
        
    
        

def welcome():
    args = """
    Welcome to the number guessing game
        Made by : Phoenix
    Made using Python and Randomw
"""
    for char in args:
        print(char, end="")
        time.sleep(0.03)
    main()
os.system("clear")
welcome()