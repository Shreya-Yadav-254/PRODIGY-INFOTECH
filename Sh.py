import os

CONTACTS_FILE = "contacts.txt"

def load_contacts():
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                contacts.append({"name": name, "phone": phone, "email": email})
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def edit_contact(contacts):
    view_contacts(contacts)
    try:
        idx = int(input("Enter the contact number to edit: ")) - 1
        if 0 <= idx < len(contacts):
            contacts[idx]['name'] = input("Enter new name: ")
            contacts[idx]['phone'] = input("Enter new phone number: ")
            contacts[idx]['email'] = input("Enter new email: ")
            save_contacts(contacts)
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input.")

def delete_contact(contacts):
    view_contacts(contacts)
    try:
        idx = int(input("Enter the contact number to delete: ")) - 1
        if 0 <= idx < len(contacts):
            contacts.pop(idx)
            save_contacts(contacts)
            print("Contact deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input.")

def main():
    contacts = load_contacts()
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
