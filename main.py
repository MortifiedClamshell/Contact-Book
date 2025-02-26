import csv

# Creates a contact book if contact book doesn't exist
try:
    f = open("Contact_Book.csv", "x")
    f.close()
except FileExistsError:
    print("File already exists")

# Gives the user options to view, edit, append, delete, or exit the contact book
option = ""
while option != "5":
    print("select an option:\n1. View Contacts\n2. Add Contact\n3. Edit Contact\n4. Delete Contact\n5. Exit")
    option = input(">> ") 

    # View contacts
    if option == "1":
        with open("Contact_Book.csv", "r") as f:
            print(f.read())

    # Add a new contact
    elif option == "2":
        with open("Contact_Book.csv", "a") as f:
            f.write(input("Name \n>> "))
            f.write(", ")
            f.write(input("Number \n>> "))
            f.write("\n")

    # Edit an existing contact
    elif option == "3":
        with open("Contact_Book.csv", "r") as f:
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
            with open("Contact_Book.csv", "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerows(reader)
        else:
            print("Invalid index")

    # Delete an existing contact
    elif option == "4":
        with open("Contact_Book.csv", "r") as f:
            reader = list(csv.reader(f))
            for i, row in enumerate(reader):
                print(f"{i}: {row[0]}, {row[1]}")
        index = int(input("Enter the number of the contact you want to delete: "))
        if 0 <= index < len(reader):
            del reader[index]
            with open("Contact_Book.csv", "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerows(reader)
        else:
            print("Invalid index")

    # Exit the program
    elif option == "5":
        print("Goodbye")

    # Handle invalid options
    else:
        print("Invalid option")