# PyPhonebook

Organize contacts using this CLI tool!

Add contacts to your phonebook using this simple cli utility. Some info you can store are:
1. Nickname
2. Name and Surname
3. E-mail Address

Some features available:

1. List all your contacts:

    Show all your saved contacts. You will obtain an output like this::

        Tento
            Name: Daniele
            Surname: Tentoni
            E-mail: daniele.tentoni2@studio.unibo.it

2. Add a new contact:

    Run this tool using `python3 phonebook.py add` to start the New Contact Adding Procedure. It will prompt you::

        Input the nickname of the contact: _

    You have to fill that field and press Enter. It will than prompt you::

        Input the name of the contact: _
        Input the surname of the contact: _
        Input the e-mail of the contact: _

    Fill all fields to create the new contact.

3. Remove an existing contact:

    Select the menu voice number relative to *Delete a contact* and input the nickname of the contact to delete::

        Input the nickname of the contact: _

    It will remove the contact from the phonebook.

4. Update a contact:

    Select the menu voice number relative to *Update a contact* and input the nickname of the contact to update::

        Input the nickname of the contact: _

    You have to fill that field and press Enter. It will than prompt you::

        Input the nickname of the contact: _
        Input the name of the contact: _
        Input the surname of the contact: _
        Input the e-mail of the contact: _

    You can confirm the field content or modify it.

## Advanced features

Features that will be available:
1. Send a simple text mail to an existing contact
2. Create contact groups (new groups are empty from contact)
    a. Add an existing contact to an existing group
    b. Remove a contact from a group
    c. Send emails to all contacts in a group
3. Save phonebook data in the local file system (think at the best way to do that)

## Exercise

Collaborate with your teammates to develop base features of this phonebook:

1. Create an issue for each feature to develop, discuss in the issue comments about best methods and implementations of that feature and assign that issue to the teammates who is account for it
2. When all work is divided among all mates, fork the main the repo in your account and start to work
3. Submit a pull request when you are ready and discuss with your teammates about the correctness of your implementation

Your evaluation will count both programming and collaborating skills.
