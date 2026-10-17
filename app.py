import sqlite3

con = sqlite3.connect('customer.db')

c = con.cursor()


def remove():
    c.execute("SELECT rowid FROM buyers")
    key = input("Enter which data you want to delete: ")


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
    c.execute("SELECT  rowid,*  FROM buyers ")
    data = c.fetchall()
    print(f"\t{'ID':5}{'First Name':15} {'Last Name':17} {'|':5}  {'Number':15} {'Email':20}")
    print("\t--" + "-" * 70)
    for item in data:
        print(f"\t{str(item[0]):5} {item[1]:15}  {item[2]:15} {'|':5} {item[3]:15} {item[4]:20}")

def update():
    show()
    c.execute(" Select rowid FROM buyers")
    key = int(input("Enter ID of the user you want to update:"))
    print()
    what = input("What do you want to change? \n 1. First Name \n 2. Last Name \n 3. Phone No \n 4. Email \n -> ")

while True:
    value = int(input(" 1. Input Data \n 2. Show Data \n -> "))
    if value == 1:
        data_in()
    elif value == 2:
        show()
    else:
        print("Ran wrong!!")

    print()
    ans = input("\t -> Do You Want To Continue? [Y,n]: ")
    while ans != 'y' and ans != 'Y' and ans != 'n' and ans != 'N':
        print("\t ERROR: Invalid Character. Try again!")
        ans = input("\t -> Do You Want To Continue? [Y,n]: ")

    if ans == 'N' or ans == 'n':
        break

















con.commit()
con.close()