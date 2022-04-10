username = input("Enter your username: ")
while len(username) < 5:
	username = input("Enter your username: ")
password = input("Enter your password: ")

print("-"*(len(username) + len(password)))
print(f"Username : {username} \npassword : {password}")

 