# Function defined outside the class definition

def f1(self, x, y):
    return min(x, x+y)

class F:

    f = f1

    def g(self):
        return "Hello, world!"

    h = g

# This only server the purpose of confusing the reader
