# Calling methods inside class

class Classroom:

    def __init__(self):
        self.data = []

    def add_name(self, name):
        self.data.append(name)
        self.add_twice(name) # calling

    def add_twice(self, name):
        self.data.append(name)
        self.data.append(name)

c = Classroom()
c.add_name("Sumit")


for items in c.data:
    print(items)
