import sqlite3

con = sqlite3.connect('customer.db')

c = con.cursor()



variable = input("Enter first name: ")

c.execute(""" CREATE TABLE buyers(
    first_name text,
    last_name text,
    phone_no text,
    email text

)""")


con.commit()

con.close()