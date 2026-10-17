import sqlite3

con = sqlite3.connect('customer.db')

c = con.cursor()




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

def delete():
    show()
    while True:
        key = int(input("Enter the ID you want to delete: "))

        c.execute("SELECT 1 FROM buyers WHERE rowid = ?",(key,))

        if c.fetchone is None:
            print(" !!! INVALID ID! TRY AGAIN !!!")
            continue

        c.execute("SELECT rowid, * FROM buyers WHERE rowid = ?",(key,))
        print("The data to be deleted: \n")
        print(f"\t{'ID':5}{'First Name':15} {'Last Name':17} {'|':5}  {'Number':15} {'Email':20}")
        print("   ", "-" * 90)
        items = c.fetchone()
        print(f"\t{str(items[0]):5} {items[1]:15}  {items[2]:15} {'|':5} {items[3]:15} {items[4]:20}")
        print()
        sure = input("Are You Sure? [y/N]").lower()
        match sure:
            case 'y':
                c.execute("DELETE FROM buyers WHERE rowid = ?", (key,))
                print("\n Data has been deleted!")
                con.commit()
            case 'n':
                print("\n Data not deleted.")
                break
            case _:
                print(" \n !!! INVALID! TRY AGAIN !!!")
                continue
        again = input("\n Delete Another Data?[Y,n]: ").lower()
        if again == 'y':
            continue
        elif again == 'n':
            break
        else:
            print("\n Invalid! Try Again from start. ")

def order():
    while True: 
        print("What do you want to order by?")
        value = int(input("1. Row ID \n 2. First Name \n 3. Last Name \n -> "))
        way = int(input("\nOrder:\n 1. Ascending \n 2. Descending"))
        if (value < 1 and value > 3) or (way < 1 or way > 2):
            print("INVALID! Try Again!")
            continue
        print()
        match value:
            case 1:
                match way:
                    case 1: 
                        c.execute("SELECT rowid,* FROM Buyers ORDER BY rowid ASC")
                    case 2:
                        c.execute("SELECT rowid,* FROM Buyers ORDER BY rowid DESC")

            case 2:
                match way:
                    case 1: 
                        c.execute("SELECT rowid,* FROM Buyers ORDER BY first_name ASC")
                    case 2:
                        c.execute("SELECT rowid,* FROM Buyers ORDER BY first_name DESC")

            case 3:
                match way:
                    case 1: 
                        c.execute("SELECT rowid,* FROM Buyers ORDER BY last_name ASC")
                    case 2:
                        c.execute("SELECT rowid,* FROM Buyers ORDER BY last_name DESC")


        data = c.fetchall()
        print(f"\t{'ID':5}{'First Name':15} {'Last Name':17} {'|':5}  {'Number':15} {'Email':20}")
        print("   ", "-" * 90)
        for item in data:
            print(f"\t{str(item[0]):5} {item[1]:15}  {item[2]:15} {'|':5} {item[3]:15} {item[4]:20}")
        print()
        break




while True:
    value = int(input("\n 1. Input Data \n 2. Show Data \n 3. Update Existing Data \n 4. Delete Data \n 5. View Data in Order \n 0. Cancle \n -> "))
    match value:
        case 1:
            add_data()
        case 2:
            show()
        case 3:
            update()
        case 4:
            delete()
        case 5:
            order()
        case 0:
            break

        case _:
            print("Invalid! Try Again")
            continue

    print()
    ans = input(" -> Do You Want To Continue? [Y,n]: ")
    while ans != 'y' and ans != 'Y' and ans != 'n' and ans != 'N':
        print("\t ERROR: Invalid Character. Try again!")
        ans = input(" -> Do You Want To Continue? [Y,n]: ")

    if ans == 'N' or ans == 'n':
        break
    


con.commit()
con.close()