class Square:
    
    def __init__(self, side): # initialzing with the variable you want to use in your class
        self.side = side

    def area(self): # creating an area function inside your class dont forget to pass self as a parameter to your functions
        return self.side ** 2

# Calling it
# To reduce the number of times we type a class's name. We can assign a variable to it
s = Square(4) # Dont forget to pass the values
# Now we can use s instead of typing Square() everytime we need to call it

# Now call the function within your class
print(s.area())