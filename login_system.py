import sqlite3
import hashlib

# -------------------- SETUP --------------------
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT
)
""")
conn.commit()


# -------------------- SECURITY --------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# -------------------- FUNCTIONS --------------------

# To Register 
def register():
    print("\n--- REGISTER ---")
    username = input("Enter username: ")

    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    if cursor.fetchone():
        print("Username already exists!\n")
        return

    password = hash_password(input("Enter password: "))
    cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    conn.commit()

    print(" Registration successful!\n")

#To Login
def login():
    print("\n--- LOGIN ---")
    username = input("Enter username: ")
    password = hash_password(input("Enter password: "))

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    
    if cursor.fetchone():
        print(" Login successful!\n")
    else:
        print("Invalid credentials!\n")

#To Delete User
def delete_user():
    print("\n--- DELETE USER ---")
    username = input("Enter username: ")
    password = hash_password(input("Enter password: "))

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    
    if cursor.fetchone():
        cursor.execute("DELETE FROM users WHERE username=?", (username,))
        conn.commit()
        print("User deleted successfully!\n")
    else:
        print("Invalid username or password!\n")

#Menu
def show_menu():
    print("=" * 35)
    print("        LOGIN SYSTEM MENU")
    print("=" * 35)
    print("1. Register")
    print("2. Login")
    print("3. Delete User")
    print("4. Exit")
    print("=" * 35)


# -------------------- MAIN LOOP --------------------
while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        delete_user()
    elif choice == "4":
        print("\nExiting program. Goodbye!")
        break
    else:
        print(" Invalid choice! Try again.\n")

conn.close()