#!/usr/bin/env python3

import json

class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

expense_list = []

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
                data = json.load(file)
        for expense in data:
            amount = expense["amount"]
            category = expense["category"]
            description = expense["description"]
            loaded_expense = Expense(amount, category, description)
            expense_list.append(loaded_expense)
    except FileNotFoundError:
        pass

def save_expenses():
    expenses_list = []
    for expense in expense_list:
        expenses_dict = dict(amount=expense.amount, category=expense.category, description=expense.description)
        expenses_list.append(expenses_dict)
    with open("expenses.json", "w") as f:
        json.dump(expenses_list, f)

def add_expense():
    try:
        a1 = float(input("Amount: "))
        if a1 <= 0:
            print("The value must be greater than zero")
            return
    except ValueError:
        print("The value has wrong format")
        return
    c1 = input("Category: ")
    if not c1.strip():
        print("You must enter the category")
        return
    d1 = input("Description: ")
    e1 = Expense(a1, c1, d1)
    expense_list.append(e1)

def show_expenses():
    for expense in expense_list:
        print(f"{expense.amount} | {expense.category} | {expense.description}")

def calculate_total():
    total = 0
    for money in expense_list:
        total += money.amount
    return total
load_expenses()



while True:
    user_input = input("1. Add Expense" \
"\n2. Show Expenses" \
"\n3. Show Total" \
"\n4. Exit\nChoose an option: ")
    if user_input == "1":
        add_expense()
        
    elif user_input == "2":
        show_expenses()
    elif user_input == "3":
        print("Total = ", calculate_total())
    elif user_input == "4":
        print("Exiting the program.")
        save_expenses()
        break
    else:
        print("Invalid option. Please choose a valid option.")



    
        
