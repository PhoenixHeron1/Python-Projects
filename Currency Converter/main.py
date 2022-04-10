import os

available_currency = ["INR", "EUR", "USD"]

def main():
	currency_1 = input("What currency you have: ")

	if currency_1 not in available_currency:
		return

	amount = float(input(f"How much {currency_1} you have: "))
	currency_2 = input("Which currency you want to convert it to: ").upper()

	if currency_1 == "INR":

		if currency_2 == "USD":
			print(f"{amount} INR in USD is {amount*0.013} $")
		elif currency_2 == "EUR":
			print(f"{amount} INR in EUR is {amount*0.012} $")
		else:
			print("That currency is not available with us")
	
	elif currency_1 == "USD":
		
		if currency_2 == "INR":
			print(f"{amount} USD in USD is {amount*75} INR")
		elif currency_2 == "EUR":
			print(f"{amount} USD in EUR is {amount*0.92} Euro")
		else:
			print("That currency is not available with us")

	elif currency_1 == "EURO":
	
		if currency_2 == "USD":
			print(f"{amount} US$ in Euro is {amount*1.09} Euro")
		elif currency_2 == "INR":
			print(f"{amount} INR in Euro is {amount*82.53} Euro")
		else:
			print("That currency is not available with us")

	else:
		print("That currency is not recognized")

os.system("clear")
main()
			