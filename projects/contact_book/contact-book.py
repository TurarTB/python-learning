#!/usr/bin/env python3

import json

class Contact:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email

contact_list = []

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
    contact = Contact(add_name, add_number, add_email)
    contact_list.append(contact)
    save_contacts()

def show_contacts():
    for contact in contact_list:
        print(f"{contact.name} | {contact.number} | {contact.email}")

def search_contact():
    search_contact = input("Enter contact Name: ")
    found = False
    found_list = []
    i = 1
    for contact in contact_list:
        if search_contact in contact.name:
            print(f"{i}. {contact.name} | {contact.number} | {contact.email}")
            found = True
            found_list.append(contact)
            i += 1
    if found == False:   
        print("Contact not found.")
    return found_list

def delete_contact():
    found_list = search_contact()
    if len(found_list) == 1:
        for contact in contact_list:
            if contact == found_list[0]:
                contact_list.remove(contact)
                print("Contact deleted.")
    elif len(found_list) == 0:
        print("Contact not found.")
    else:
        while True:
            try:
                delete_option = int(input("Enter contact for deletion: "))
                if 0 < delete_option <= len(found_list):
                    for contact in contact_list:
                        if contact == found_list[delete_option-1]:
                            contact_list.remove(contact)
                            print(f"Contact deleted.")
                    break
                else:
                    print("Chose the correct option")
                    continue
            except ValueError:
                print("The value has wrong format.")
                continue
    save_contacts()

def save_contacts():
    contacts = []
    for contact in contact_list:
        contacts_dict = dict(name=contact.name, number=contact.number, email=contact.email)
        contacts.append(contacts_dict)
    with open("contacts.json", "w") as f:
        json.dump(contacts, f)

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            data = json.load(file)
        for contact in data:
            name = contact["name"]
            number = contact["number"]
            email = contact["email"]
            loaded_contact = Contact(name, number, email)
            contact_list.append(loaded_contact)
    except FileNotFoundError:
        pass

load_contacts()

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

