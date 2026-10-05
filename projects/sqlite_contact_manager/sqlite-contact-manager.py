#!/usr/bin/evn python3

# import the sqlite3 module
import sqlite3


def add_contact():
    add_name = input("Name: ")
    if not add_name.strip():
        print("You must enter the name")
        return
    try:
        add_number = int(input("Number: "))
    except ValueError:
        print("The value has wrong format")
        return
    add_email = input("Email: ")

    # Define connection and cursor
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()

    #create table
    try:
        create_table = '''CREATE TABLE CONTACT(
        Contact_ID INTEGER PRIMARY KEY, Name VARCHAR(100) NOT NULL, 
        Number int NOT NULL, Email VARCHAR(100))'''
        cursor.execute(create_table)
    except sqlite3.OperationalError:
        pass

    cursor.execute("INSERT INTO CONTACT (Name, Number, Email) \
                   VALUES (?, ?, ?)", (add_name, add_number, add_email))

    # Commit the changes in database and Close the connection
    connection.commit()
    connection.close()

def show_contacts():
    # Connecting to sqlite databse
    connection = sqlite3.connect('contacts.db')

    # cursor object
    cursor = connection.cursor()

    # to select all column we will use
    statement = '''SELECT * FROM CONTACT'''

    cursor.execute(statement)

    output = cursor.fetchall()
    for row in output:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

    # Close the connection
    connection.close()

def search_contact():
    search_contact = input("Enter contact Name: ")
    connection = sqlite3.connect('contacts.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM CONTACT WHERE Name = ?", (search_contact,))
    output = cursor.fetchall()
    for row in output:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
    if not output:   
        print("Contact not found.")
    connection.close()
    return output

def delete_contact():
    search_contact = input("Enter contact Name: ")
    connection = sqlite3.connect('contacts.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM CONTACT WHERE Name = ?", (search_contact,))
    output = cursor.fetchall()
    if len(output) == 1:
        cursor.execute("DELETE FROM CONTACT WHERE Name = ?", (search_contact,))
        print("Contact deleted.")
    elif len(output) == 0:
        print("Contact not found.")
    else:
        while True:
            try:
                for row in output:
                    print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
                delete_option = int(input("Enter Contact_id for deletion: "))
                if any(delete_option == row[0] for row in output):
                    cursor.execute("DELETE FROM CONTACT WHERE Contact_id = ?", (delete_option,))
                    print("Contact deleted.")
                    break
                else:
                    print("Chose the correct option")
                    continue
            except ValueError:
                print("The value has wrong format.")
                continue
    connection.commit()
    connection.close()


while True:   
    user_input = input("1. Add contact" \
    "\n2. Show contacts" \
    "\n3. Search contact" \
    "\n4. Delete contact" \
    "\n5. Exit" \
    "\nChoose an option: ")
    if user_input == "1":
        add_contact()
    elif user_input == "2":
        show_contacts()
    elif user_input == "3":
        search_contact()
    elif user_input =="4":
        delete_contact()
    elif user_input =="5":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please a valid option.")
        continue