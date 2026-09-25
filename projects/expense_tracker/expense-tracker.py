#!/usr/bin/env python3

while True:
    user_input = input("1. Add Expense" \
"\n2. Show Expenses" \
"\n3. Show Total" \
"\n4. Exit\nChoose an option: ")
    if user_input == "1":
        print("Add expense")
    elif user_input == "2":
        print("Show expenses")
    elif user_input == "3":
        print("Show Total")
    elif user_input == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please choose a valid option.")
        
