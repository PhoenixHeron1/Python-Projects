class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_tricks(self, tricks):
        self.tricks.append(tricks)

d = Dog("Fido")
e = Dog("Buddy")

d.add_tricks("bhow bhow")
e.add_tricks("jump")

print(d.tricks, e.tricks)

# In the above code every dog has separate tricks.
