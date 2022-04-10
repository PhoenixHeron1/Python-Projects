# contact book
import sqlite3

# connecting to database
conn = sqlite3.connect("Contacts.db")

# creating a database
c = conn.cursor()

# creating a table
# c.execute("""CREATE TABLE Contacts (
#     Name text,
#     Phone integer
# )""")

# inserting data
c.execute("""INSERT INTO Contacts VALUES (
    "John", "859455"
)
""")

# There are only 5 datatypes in sqlite3:
# 1. NULL 2. INTEGER 3. REAL 4. TEXT 5. BLOB 

# commiting to database
conn.commit()

# closing our connection
conn.close()
