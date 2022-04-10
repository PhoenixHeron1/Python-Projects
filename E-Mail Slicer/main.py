import os

def main():
    email = input("Enter you email: ")
    name = email.split("@")
    
    print(f"Name : {name[0]}\nDomain name : {name[1]} ")
os.system("clear")
main()