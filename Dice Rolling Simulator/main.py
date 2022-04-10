# Dice Rolling Simulator
import random
import os
import time

def main():
    limit = input("\nHow many times you wanna roll the dice: ")
    while limit.isalpha():
        limit = input("Enter how many times you wanna roll the dice: ")
    print(f"\nYou chosed {limit}!!")

    arg1 = """
    Rolling the Dice    
"""
    for char in arg1:
        print(char, end="")
        time.sleep(0.04)

    random_list = []
    for _i in range(int(limit)):
        rr = random.randint(1, 6)
        random_list.append(rr)

    print("\nRolled number are: ")
    for index, items in enumerate(random_list, start=1):
        print(f"{index}. {items}")
        time.sleep(0.02)

os.system("clear")
main()



        