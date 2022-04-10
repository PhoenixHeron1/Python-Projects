# Class Objects

# class Dog:
#
#     legs = 4
#     # Every dog has 4 legs
#
# d = Dog()
# print(d.legs)

class Complex:

    def __init__(self, real_part, imag_part):
        self.r = real_part
        self.i = imag_part

c = Complex(3.0, -4.0)
# print(c.r, c.i)

# Class and Instance Variables

class Instance:

    kind = "canine"
    def __init__(self, name):
        self.name = name


i = Instance("dog")
j = Instance("cat")
# print(i.name, j.name)
# print(i.kind, j.kind)

class Dog:

    tricks = [] # used by every dog

    def __init__(self, name):
        self.name = name

    def add_ticks(self, trick):
        self.tricks.append(trick)
d = Dog("Fido")
e = Dog("Buddy")

d.add_ticks("roll over")
e.add_ticks("jump")

print(d.tricks, e.tricks) # unexpectedly shared by all dogs
