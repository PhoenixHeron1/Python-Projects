import sqlite3
import os
import time

conn = sqlite3.connect("Contacts.db")

c = conn.cursor()
banned = "1234567890"


def add():
    small()
    print("\nAlright! Adding Contacts")

    c.execute("SELECT * from Contacts")
    testing = c.fetchall()

    name = input("Enter name: ").capitalize()

    while any(word in name for word in banned):
        print("Please enter proper name")
        name = input("Enter name: ").capitalize()
    for rows in testing:
        if name in rows:
            print("That name is already in the database")
            add()

    number = int(input("Enter phone number: "))

    c.execute(
        f"""INSERT INTO Contacts VALUES (
    "{name}", "{number}"
)
"""
    )
    conn.commit()
    print(f"Added {name} with {number} in the database ")
    time.sleep(1)
    os.system("clear")
    view()


def delete():
    
    small()
    print("\nAlright! Deleting Contacts")
    name = input("Enter name: ")
    while any(word in name for word in banned):
        print("Please enter proper name")
        name = input("Enter name: ")

    c.execute(
        f"""DELETE from Contacts WHERE Name = "{name}";
"""
    )
    conn.commit()
    print(f"Deleted {name}")
    time.sleep(1)
    os.system("clear")
    view()


def view():
    c.execute("SELECT * from Contacts")
    output = c.fetchall()
    small()
    print("\n      Data in Contact Book (Database)\n")

    for index, (row, columns) in enumerate(output, start=1):
        print(f"|{index}|. {row} : {columns} ")
    small()
    conn.commit()

    print()
    print("Add or Delete Contacts")
    ask = input("Enter your choice: ")
    if ask == "Add":
        add()
    elif ask == "Delete":
        delete()
    else:
        print("Invalid Input")
        view()

def welcome(name):
    for char in name:
        print(char, end="")
        time.sleep(0.03)
        
def small():
    print("_________________________________________")
        
os.system("clear")
welcome("""
        Welcome to Contact Book
        Created by : Phoenix
    Made using Python and SQliTE3 Database
""")
view()
