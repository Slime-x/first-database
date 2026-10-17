import sqlite3

con = sqlite3.connect('customer.db')

c = con.cursor()


def data_in():
    fn = input("Enter first name: ")
    ln = input("Enter last name: ")
    no = input("Enter phone no: ")
    email = input("Enter email: ")

    c.execute(""" CREATE TABLE IF NOT EXISTS buyers(
        first_name text,
        last_name text,
        phone_no text,
        email text
    )""")

    c.execute(" INSERT INTO buyers VALUES(?,?,?,?)",(fn,ln,no,email))

def show():
    c.execute("SELECT * FROM buyers ")
    data = c.fetchall()
    print(f"{'First Name':15} {'Last Name':15} {'Number':15} {'Email':15}")
    print("-" * 70)
    for item in data:
        print(f"{item[0]:15} {item[1]:15} {item[2]:15} {item[3]:15}")




while True:
    value = int(input(" 1. Input Data \n 2. Show Data \n -> "))
    if value == 1:
        data_in()
    elif value == 2:
        show()
    else:
        print("Ran wrong!!")

    ans = input("Do You Want To Continue? [Y,n]")
    while ans != 'y' and ans != 'Y' and ans != 'n' and ans != 'N':
        print("ERROR: Invalid Character. Try again!")
        ans = input("Do You Want To Continue? [Y,n]")

    if ans == 'N' or ans == 'n':
        break

















con.commit()
con.close()