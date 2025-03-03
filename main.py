import csv
import os

# Asks if the user wants to open an existing contact book or create a new one
contact_option = ""
book = ""
while contact_option != "1" and contact_option != "2" and contact_option != "3" and contact_option != "4":
    print("Welcome to Your Contact Books \n1. Open existing contact book \n2. Create new contact book \n3. View all contact books \n4. Delete contact book")
    contact_option = input(">> ")
    
    # Open existing contact book
    if contact_option == "1":
        try:
            book = input("Enter the name of the contact book >> ")
            f = open(book + ".csv", "r")
            f.close()   
        except FileNotFoundError:
            print("File doesn't exist")
            contact_option = ""
    
    # Create new contact book
    elif contact_option == "2":
        try:
            book = input("Enter the name of the contact book >> ")
            f = open(book + ".csv", "x")
            f.write("Name, Number\n")
            f.close()
        except FileExistsError:
            print("File already exists")
            contact_option = ""
    
    # View all contact books
    elif contact_option == "3":
        for file in os.listdir():
            if file.endswith(".csv"):
                print(file)
        contact_option = ""
    
    # Delete contact book
    elif contact_option == "4":
        book = input("Enter the name of the contact book >> ")
        os.remove(book + ".csv")
        contact_option = ""

    # Handle invalid options
    else:
        print("Invalid option")

# Gives the user options to view, edit, append, delete, override, switch, or exit the contact book
option = ""
while option != "7":
    print("select an option:\n1. View Contacts\n2. Add Contact\n3. Edit Contact\n4. Delete Contact\n5. Override Contact Book\n6. Switch Contact Book\n7. Exit")
    option = input(">> ") 

    # View contacts
    if option == "1":
        with open(book + ".csv", "r") as f:
            print(f.read())

    # Add a new contact
    elif option == "2":
        with open(book + ".csv", "a") as f:
            f.write(input("Name \n>> "))
            f.write(", ")
            f.write(input("Number \n>> "))
            f.write("\n")

    # Edit an existing contact
    elif option == "3":
        with open(book + ".csv", "r") as f:
            reader = list(csv.reader(f))
            for i, row in enumerate(reader):
                print(f"{i}: {row[0]}, {row[1]}")
        index = int(input("Enter the number of the contact you want to edit: "))
        if 0 <= index < len(reader):
            name = input("Enter new name (leave blank to keep current): ")
            number = input("Enter new number (leave blank to keep current): ")
            if name:
                reader[index][0] = name
            if number:
                reader[index][1] = number
            with open(book + ".csv", "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerows(reader)
        else:
            print("Invalid index")

    # Delete an existing contact
    elif option == "4":
        with open(book + ".csv", "r") as f:
            reader = list(csv.reader(f))
            for i, row in enumerate(reader):
                print(f"{i}: {row[0]}, {row[1]}")
        index = int(input("Enter the number of the contact you want to delete: "))
        if 0 <= index < len(reader):
            del reader[index]
            with open(book + ".csv", "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerows(reader)
        else:
            print("Invalid index")

    # Override the contact book
    elif option == "5":
        with open(book + ".csv", "w") as f:
            f.write("Name, Number\n")
            print("Contact book has been overridden")

    # Switch contact book
    elif option == "6":
        contact_option = ""
        while contact_option != "1" and contact_option != "2":
            print("1. Open existing contact book \n2. Create new contact book")
            contact_option = input(">> ")
            if contact_option == "1":
                try:
                    book = input("Enter the name of the contact book >> ")
                    f = open(book + ".csv", "r")
                    f.close()   
                except FileNotFoundError:
                    print("File doesn't exist")
                    contact_option = ""
            elif contact_option == "2":
                try:
                    book = input("Enter the name of the contact book >> ")
                    f = open(book + ".csv", "x")
                    f.write("Name, Number\n")
                    f.close()
                except FileExistsError:
                    print("File already exists")
                    contact_option = ""
            else:
                print("Invalid option")

    # Exit the program
    elif option == "7":
        print("Goodbye")

    # Handle invalid options
    else:
        print("Invalid option")