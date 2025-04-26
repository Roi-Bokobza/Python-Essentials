import time
import sqlite3

db = sqlite3.connect("bank.db")
cursor = db.cursor()

cursor.execute("""
create table if not exists users (
    username text primary key,
    password text,
    balance integer
)
""")
db.commit()

cursor.executemany("insert or ignore into users values (?, ?, ?)", [
    ("admin", "admin", 0),
    ("roi bokobza", "totallysecure", 4568978),
    ("shmuel", "ya manyak", 6546),
    ("shalom", "shalom olam", 87123),
    ("shaulov", "1234", 65432)
])
db.commit()

log_out_flag = True

while log_out_flag:
    username = ""
    passwd = ""

    while True:
        username = input("Enter your Username: ").strip().lower()
        query = f"SELECT * FROM users WHERE username = '{username}'"
        cursor.execute(query)
        user = cursor.fetchone()

        if not user:
            print(f"'{username}' is a wrong username, try again.")
        else:
            print(f"Hello {username.title()}")
            break

    while True:
        passwd = input("\nEnter your password: ").strip()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{passwd}'"
        cursor.execute(query)
        user = cursor.fetchone()

        if user:
            print(f"Welcome {username.title()}, you have been authorized")
            break
        else:
            print("Wrong password!")

    if username == "admin":
        while True:
            time.sleep(1)
            action = input("You are logged in as Admin!\n(v)iew accounts\n(r)eset password\n(l)og out\n").lower()

            if action == "v":
                cursor.execute("select username, password from users")
                print("\nUser Accounts:", cursor.fetchall())

            elif action == "r":
                new_passwd = input("Enter a new password: ").strip()
                query = f"UPDATE users SET password = '{new_passwd}' WHERE username = '{username}'"
                cursor.execute(query)
                db.commit()
                print("Password successfully reset!")
                time.sleep(1)

            elif action == "l":
                print(f"Goodbye {username.title()}!")
                break

            elif action == "e":
                log_out_flag = False
                break

            else:
                print("Invalid action, please choose again.")

    else:
        while True:
            time.sleep(1)
            action = input(f"You are logged in as {username.title()}!\n(v)iew your banking account\n(r)eset password\n(l)og out\n").lower()

            if action == "v":
                query = f"SELECT balance FROM users WHERE username = '{username}'"
                cursor.execute(query)
                print(f"\nYour banking account balance: ${cursor.fetchone()[0]:,}")

            elif action == "r":
                new_passwd = input("Enter a new password: ").strip()
                query = f"UPDATE users SET password = '{new_passwd}' WHERE username = '{username}'"
                cursor.execute(query)
                db.commit()
                print("Password successfully reset!")
                time.sleep(1)

            elif action == "l":
                print(f"Goodbye {username.title()}!")
                break

            elif action == "e":
                log_out_flag = False
                break

            else:
                print("Invalid action, please choose again.")