# SQLite Contact Manager

A simple command-line contact manager written in Python using SQLite.

## Features

- Add contacts
- Show all contacts
- Search contacts by name
- Delete contacts
- Automatically generate unique contact IDs
- Store contacts in an SQLite database
- Contacts persist after restarting the program

## Requirements

- Python 3
- SQLite3 (included with Python)

## How to Run

Run the program from the terminal:

```bash
python sqlite-contact-manager.py
```

## Menu

```text
1. Add contact
2. Show contacts
3. Search contact
4. Delete contact
5. Exit
```

## Database

The program automatically creates the SQLite database and the `CONTACT` table if they do not already exist.

Contacts are stored in:

```text
contacts.db
```