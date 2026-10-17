import sqlite3

con = sqlite3.connect('customer.db')

c = con.cursor()


def remove():
    c.execute("SELECT rowid FROM buyers")
    key = input("Enter which data you want to delete: ")


def add_data():
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
    print("   ", "-" * 90)
    for item in data:
        print(f"\t{str(item[0]):5} {item[1]:15}  {item[2]:15} {'|':5} {item[3]:15} {item[4]:20}")
    print()

def update():
    show()
    c.execute(" Select rowid FROM buyers")
    while True:
        key = int(input("Enter ID of the user you want to update:"))
        c.execute("SELECT 1 FROM buyers WHERE rowid = ?", (key,))

        if c.fetchone() is None:
            print(" !!! Invalid Key! Try Again !!! \n")
            continue

        print()
        what = int(input("What do you want to change? \n 1. First Name \n 2. Last Name \n 3. Phone No \n 4. Email \n -> "))
        if what < 1 or what > 4:
            print(" !!! Invalid choice! Try Again !!!\n")
            continue

        match what:
            case 1:
                change_first_name = input("\n Enter New First Name: ")
                c.execute("""UPDATE buyers 
                            SET first_name = ?
                            WHERE rowid = ?
                        """, (change_first_name, key))
            case 2:
                change_last_name = input("\n Enter New Last Name: ")
                c.execute("UPDATE buyers SET last_name = ? WHERE rowid = ?", (change_last_name, key))
            case 3:
                change_phone = input("\n Enter New Phone NO: ")
                c.execute("UPDATE buyers SET phone_no = ? WHERE rowid = ?", (change_phone, key))
            case 4:
                change_email = input("\n Enter New Email: ")
                c.execute("UPDATE buyers SET email = ? WHERE rowid = ?", (change_email, key))
            case _:
                print("\n !!! Invalid! Try again !!!")
                print("-" * 90)
                continue
        con.commit()
        break

while True:
    value = int(input("\n 1. Input Data \n 2. Show Data \n 3. Update Existing Data \n -> "))
    match value:
        case 1:
            add_data()
        case 2:
            show()
        case 3:
            update()

        case _:
            Print("Invalid! Try Again")

    print()
    ans = input(" -> Do You Want To Continue? [Y,n]: ")
    while ans != 'y' and ans != 'Y' and ans != 'n' and ans != 'N':
        print("\t ERROR: Invalid Character. Try again!")
        ans = input(" -> Do You Want To Continue? [Y,n]: ")

    if ans == 'N' or ans == 'n':
        break
    

















con.commit()
con.close()