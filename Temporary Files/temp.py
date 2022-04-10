cost = 99
def main():
    global quantity
    quantity = int(input("How many quantity: "))
    d(quantity)

def d(q):
    if q <= 19:
        discount = 0.20

    elif q <= 46:
        discount = 0.30

    elif q <= 60:
        discount = 0.40

    elif q > 100:
        discount = 0.50
    price(discount)

def price(dis):
    beforeD = quantity * cost
    afterD = beforeD - dis*beforeD
    print(afterD)

main()
