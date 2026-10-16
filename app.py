import sqlite3

con = sqlite3.connect('customer.db')

c = con.cursor()



# fn = input("Enter first name: ")
# ln = input("Enter last name: ")
# no = input("Enter phone no: ")
# email = input("Enter email: ")

# c.execute(""" CREATE TABLE buyers(
#     first_name text,
#     last_name text,
#     phone_no text,
#     email text

# )""")

# c.execute(" INSERT INTO buyers VALUES(?,?,?,?)",(fn,ln,no,email))

data = c.execute("SELECT * FROM buyers WHERE rowid = 1")

for item in data:
    print(c.fetchone())

con.commit()

con.close()