#!/usr/bin/env python3
"""
Main module of PyPhonebook utility.

Process command line inputs and execute requested operations.
"""

import os
import smtplib
import sys

from email.message import EmailMessage

class Contact:
  def __init__(self, nickname: str, name: str, surname: str, email: str) -> None:
    self.nickname = nickname
    self.name = name
    self.surname = surname
    self.email = email

phonebook: dict[str, Contact] = {}
groups: dict[str, list[str]] = {}

phonebook_separator = "#"
group_separator = "#"
components_separator = ";"

def list_contacts():
  """
  List all contacts in the console.

  The format of contacts is:

      Nickname
          Name
          Surname
          Email
  """
  for c in phonebook.values():
    print(f"{c.nickname}")
    indent = "\t"
    print(f"{indent}{c.name}")
    print(f"{indent}{c.surname}")
    print(f"{indent}{c.email}")
    print("")

def _insert_contact(nickname, name, surname, email):
  """Insert a contact in the phonebook."""
  contact = Contact(nickname, name, surname, email)
  phonebook[nickname] = contact

def create_contact():
  """Create a contact and insert it into the phonebook."""
  nickname = input("Input the nickname of the contact: ")
  if nickname in phonebook:
    print(f"User {nickname} already registered")
    pass

  name = input("Input the name of the contact: ")
  surname = input("Input the surname of the contact: ")
  email = input("Input the e-mail of the contact: ")
  _insert_contact(nickname, name, surname, email)

def remove_contact():
  """Remove a contact from the phonebook."""
  nickname = input("Insert nickname: ")
  if nickname in phonebook:
    sure = input("Are you sure? [y/N] ")
    if sure.lower() == "y":
      del phonebook[nickname]
    else:
      print("Operation aborted")
  else:
    print(f"Unknown contact {nickname}")

def update_contact():
  """Update a contact in the phonebook."""
  pass

def load_contacts():
  """Load contacts from file system."""
  try:
    with open("phonebook.txt", "r", encoding="utf-8") as r:
      raw_phonebook = r.readlines()

    raw_contacts = [c.split(phonebook_separator) for c in raw_phonebook]
    for rc in raw_contacts:
      _insert_contact(rc[0], rc[1], rc[2], rc[3])
  except FileNotFoundError:
    print("Saved phonebook not found")
  except Exception as ex:
    print(f"Thrown exception {ex}")

  try:
    with open("groups.txt", "r", encoding="utf-8") as group_reader:
      raw_groups = group_reader.readlines()

    raw_lists = [c.split("#") for c in raw_groups]
    for rg in raw_lists:
      name = rg[0]
      groups[name] = []
      nicks = rg[1].split(";")
      groups[name].extend(nicks)
  except FileNotFoundError:
    print("Saved phonebook not found")
  except Exception as ex:
    print(f"Thrown exception {ex}")

def save_contacts():
  """Save contacts in the filesystem."""
  raw_contacts = [f"{c.nickname}{phonebook_separator}{c.name}{phonebook_separator}{c.surname}{phonebook_separator}{c.email}" for c in contacts.values()]
  try:
    with open("phonebook.txt", "w", encoding="utf-8") as phonebook_writer:
      [phonebook_writer.write(f"{r}") for r in raw_contacts]
  except Exception as ex:
    print(f"Thrown exception {ex}")

  try:
    with open("groups.txt", "w", encoding="utf-8") as group_writer:
      for k, v in groups:
        contacts = components_separator.join(v)
        group_writer.write(f"{k}{group_separator}{contacts}")
  except Exception as ex:
    print(f"Exception thrown {ex}")

def send_email():
  """Send email."""
  nick = input("Select a contact: ")
  if nick in phonebook:
    contact = phonebook[nick]
    txt = input("Input your message: ")
    _send_email_to(contact, txt)
  else:
    print(f"Unknown contact {nick}")

def _send_email_to(contact: Contact, text: str):
  """Send a mail to a contact."""
  msg = EmailMessage()
  msg.set_content(text)
  msg['Subject'] = "Message from PyPhonebook"
  msg['From'] = "PyPhonebook <pyphonebook@example.com"
  msg['To'] = contact.email

  with smtplib.SMTP('localhost') as s:
    s.send_message(msg)

def list_groups():
  """List all groups with all components"""
  for k, v in groups.items():
    print(k)
    for c in v:
      print(f"\t{c}")

def create_group():
  """Create a new group."""
  name = input("Input name of new group")
  if name in groups.keys():
    print(f"Group {name} already exists")
  else:
    groups[name] = []

def delete_group():
  """Delete an existing group."""
  name = input("Input name of group to delete")
  if name in groups.keys():
    del groups[name]
  else:
    print(f"Unknown group {name}")

def add_component():
  """Add a component to a given group."""
  nick = input("Input nick of user to add to a group")
  if nick not in phonebook.keys():
    print("Unknown contact to add")
  else:
    name = input("Input name of group to use")
    if name not in groups.keys():
      print(f"Unknown group {name}")
    else:
      groups[name].append(nick)

def remove_component():
  """Remove a component from a given group."""
  name = input("Input name of group to use")
  if name not in groups.keys():
    print(f"Unknown group {name}")
  else:
    nick = input("Input nick of user to remove from group")
    if nick not in groups[name]:
      print(f"{nick} is not in group {name}")
    else:
      groups[name].remove(nick)

def send_email_group():
  """Send an email to a group."""
  name = input("Select a group: ")
  if name in groups:
    txt = input("Input your message")
    for nick in groups[name]:
      contact = phonebook[nick]
      _send_email_to(contact, txt)
  else:
    print(f"Unknown group {name}")

def group_menu():
  """Present to the user the group action menu."""
  cmd = input("PyPhonebook groups: digit a command for groups in the following list\nls: list groups\ncreate: create a new group\ndel: delete a group\nadd: add a contact to a group\nrm: remove a contact from a group\nsend: send emails to all components of a group\n: ")
  match cmd:
    case "ls":
      list_groups()
    case "create":
      create_group()
    case "del":
      delete_group()
    case "add":
      add_component()
    case "rm":
      remove_component()
    case "send":
      send_email_group()
    case _:
      print("Unknown command")

def cli():
  """Present to the user the main action menu."""
  """Ask to user the next operation to do."""
  load_contacts()
  while True:
    cmd = input("PyPhonebook: digit a command in the list\nls: list contacts\nnew: create new contact\nrm: remove a contact\nup: update a contact\nsave: save the current list of contacts\nexit: exit the program\n: ")
    match cmd:
      case "ls":
        list_contacts()
      case "new":
        create_contact()
      case "rm":
        remove_contact()
      case "up":
        update_contact()
      case "save":
        save_contacts()
      case "send":
        send_email()
      case "group":
        group_menu()
      case "exit":
        sys.exit(os.EX_OK)
      case _:
        print("Unknown command")

if __name__ == "__main__":
  cli()
