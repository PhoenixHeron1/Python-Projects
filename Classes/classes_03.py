# Random Remarks

# If the same attribute name occurs in both an instance and
# in a class, then attribute lookup prioritizes the instance:
class Warehouse:

    purpose = "storage"
    region = "west"

w1 = Warehouse()
print(w1.purpose, w1.region)

w1.purpose, w1.region = "trunk", "east"
print(w1.purpose, w1.region)

# We can manipulate the variables inside a class
