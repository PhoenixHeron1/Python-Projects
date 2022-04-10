import sqlite3
import os
import time
from turtle import color
from termcolor import colored

conn = sqlite3.connect("guest.db")
c = conn.cursor()


# Creating Table
# c.execute("""CREATE TABLE Guest (
#     Name text,
#     Age integer,
#     Phone integer,
#     Email text

# )""")


def name():
    print("\nChecking-In")
    print("Enter your name, age, phone number and email when asked!")
    global name1
    name1 = input("\nEnter your name: ")
    while name1.isdigit():
        name1 = input("Enter your name: ")
    age(name1)


def age(arg1):
    global age1
    try:
        age1 = int(input("Enter your age: "))
    except ValueError:
        age(arg1)
    phone(arg1)


def phone(arg2):
    global number
    try:
        number = int(input("Enter phone number: "))
    except ValueError:
        phone(arg2)
    email()


def email():
    global email1
    email1 = input("Enter your email id: ")
    display()


def display():

    c.execute("SELECT Phone FROM Guest")
    check = c.fetchall()
    for items in check:
        if number in items:
            print(f"\nLooks like {number} is already here!!")
            print("Registration Failed!")
            time.sleep(1)
            welcome()
    add()
    conn.commit()


def add():
    c.execute(
        f"""INSERT INTO Guest VALUES (
    "{name1}", "{age1}", "{number}", "{email1}"
)"""
    )
    conn.commit()
    print("\nChecked-In Successfully!")
    welcome()


def welcome():
    message = """
    Welcome to my Hotel Management Service!
              Made by : Phoenix\n  
"""
    for char in message:
        print(colored(char, color="yellow", attrs=["bold"]), end="")
        time.sleep(0.03)
    prompt = int(input(colored("1. Check-in \nor \n2. Check-out\nEnter here: ", color="magenta", attrs=["bold"])))
    if prompt not in (1, 2):
        print("Thats not a valid choice!")
        welcome()

    elif prompt == 1:
        name()
    elif prompt == 2:
        checkout()


def checkout():
    check = input("Enter your phone number: ")
    c.execute("SELECT Phone from Guest")
    test = c.fetchall()
    for items in test:
        if int(check) in items:
            c.execute(
                f"""
    DELETE from Guest WHERE Phone = "{check}";
"""
            )
            print("Checked Out!!")
            break
        print("That user has either checked out or was never here!")
    conn.commit()
    welcome()


os.system("clear")
welcome()
conn.commit()
