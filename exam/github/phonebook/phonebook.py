#!/usr/bin/env python3
"""
Main module of PyPhonebook utility.

Process command line inputs and execute requested operations.
"""

def list_contacts():
  """
  List all contacts in the console.

  The format of contacts is:

      Nickname
          Name
          Surname
          Email
  """
  print("No contacts")
  pass

def add_contact():
  """Add a contact to the phonebook."""
  print("Added")
  pass

def remove_contact():
  """Remove a contact from the phonebook."""
  pass

def update_contact():
  """Update a contact in the phonebook."""
  pass

def cli():
  """Process the command line arguments of the program."""
  running = True

  while running:
    choice = input("PyPhonebook: digit a command and enter (help for more info): ")
    if choice == "ls":
      list_contacts()
    elif choice == "new":
      add_contact()
    elif choice == "rm":
      remove_contact()
    elif choice == "up":
      update_contact()
    elif choice == "exit":
      running = False

if __name__ == "__main__":
  cli()
