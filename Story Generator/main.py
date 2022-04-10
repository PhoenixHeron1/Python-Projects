import random
import os
os.system("clear")

name = input("Enter your name: ").capitalize()
gender = input("Boy or girl: ").lower()
age = int(input("Enter age: "))
pronoun = input("He/She: ").capitalize()

story1 = f"""
There was a {gender} named {name} whose age was {age}. {pronoun} loved to eat ice-cream. He loved to play with his friends
"""
story2 = f"""
{name} was a {gender} who's age was {age}. {pronoun} was a intelligent child. {pronoun} used to always top in exams.
"""

list1 = [story1, story2]

print(random.choice(list1))