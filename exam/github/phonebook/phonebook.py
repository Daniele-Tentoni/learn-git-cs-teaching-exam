"""
Main module of PyPhonebook utility.

Process command line inputs and execute requested operations.
"""

import os
import sys

def list_contacts():
  """
  List all contacts in the console.

  The format of contacts is:

      Nickname
          Name
          Surname
          Email
  """
  pass

def add_contact():
  """Add a contact to the phonebook."""
  pass

def remove_contact():
  """Remove a contact from the phonebook."""
  pass

def update_contact():
  """Update a contact in the phonebook."""
  pass

def cli(args: list[str]):
  """Process the command line arguments of the program."""
  if "ls" in args:
    list_contacts()
  elif "add" in args:
    add_contact()
  elif "rm" in args:
    remove_contact()
  elif "up" in args:
    update_contact()

  sys.exit(os.EX_OK)

if __name__ == "__main__":
  cli(sys.argv[1:])
