import tkinter as tk
from tkinter import messagebox, simpledialog
import re

class Contact:
    """Represents a contact with basic details."""
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactManager:
    """Manages a collection of contacts."""
    def __init__(self):
        self.contacts = {}
        self.valid_domains = {"gmail.com", "yahoo.com", "rediffmail.com"}

    def is_valid_phone(self, phone):
        """Validates the phone number to ensure it is exactly 10 digits."""
        return phone.isdigit() and len(phone) == 10

    def is_valid_email(self, email):
        """Validates the email to ensure it has a valid domain and structure."""
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(pattern, email):
            return False

        domain = email.split('@')[-1]
        return domain in self.valid_domains

    def is_valid_name(self, name):
        """Validates the name to ensure it is less than 50 characters."""
        return len(name) > 0 and len(name) < 50

    def add_contact(self, name, phone, email, address):
        if not self.is_valid_name(name):
            return "Invalid name. It must be less than 50 characters."
        if not self.is_valid_phone(phone):
            return "Invalid phone number. It must be exactly 10 digits long."
        if not self.is_valid_email(email):
            return "Invalid email. It must be a real email domain like gmail.com, yahoo.com, etc."
        if not address:
            return "Invalid address. Address cannot be empty."
        
        if phone in self.contacts:
            return "Contact with this phone number already exists."
        else:
            self.contacts[phone] = Contact(name, phone, email, address)
            return "Contact added successfully."

    def view_contacts(self):
        return [str(contact) for contact in self.contacts.values()]

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts.values():
            if search_term.lower() in contact.name.lower() or search_term == contact.phone:
                found_contacts.append(str(contact))
        return found_contacts or ["Contact not found."]

    def update_contact(self, phone, name=None, email=None, address=None):
        contact = self.contacts.get(phone)
        if contact:
            if name:
                if not self.is_valid_name(name):
                    return "Invalid name. It must be less than 50 characters."
                contact.name = name
            if email:
                if not self.is_valid_email(email):
                    return "Invalid email. It must be a real email domain like gmail.com, yahoo.com, etc."
                    return
                contact.email = email
            if address:
                contact.address = address
            return "Contact updated successfully."
        else:
            return "Contact not found."

    def delete_contact(self, phone):
        if phone in self.contacts:
            del self.contacts[phone]
            return "Contact deleted successfully."
        else:
            return "Contact not found."

class ContactManagerGUI:
    def __init__(self, root):
        self.manager = ContactManager()
        self.root = root
        self.root.title("Contact Management System")

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.contact_listbox = tk.Listbox(self.frame, width=50, height=15)
        self.contact_listbox.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(self.root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack(pady=5)

        self.search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        self.search_button.pack(pady=5)

        self.update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5)

        self.quit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.quit_button.pack(pady=5)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter Name:")
        phone = simpledialog.askstring("Input", "Enter Phone Number:")
        email = simpledialog.askstring("Input", "Enter Email:")
        address = simpledialog.askstring("Input", "Enter Address:")
        
        result = self.manager.add_contact(name, phone, email, address)
        messagebox.showinfo("Add Contact", result)
        self.view_contacts()

    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        contacts = self.manager.view_contacts()
        if not contacts:
            self.contact_listbox.insert(tk.END, "No contacts found.")
        else:
            for contact in contacts:
                self.contact_listbox.insert(tk.END, contact)

    def search_contact(self):
        search_term = simpledialog.askstring("Input", "Enter Name or Phone Number to Search:")
        results = self.manager.search_contact(search_term)
        self.contact_listbox.delete(0, tk.END)
        for result in results:
            self.contact_listbox.insert(tk.END, result)

    def update_contact(self):
        phone = simpledialog.askstring("Input", "Enter Phone Number of the Contact to Update:")
        if phone in self.manager.contacts:
            name = simpledialog.askstring("Input", "Enter new Name (leave blank to keep unchanged):")
            email = simpledialog.askstring("Input", "Enter new Email (leave blank to keep unchanged):")
            address = simpledialog.askstring("Input", "Enter new Address (leave blank to keep unchanged):")
            
            result = self.manager.update_contact(phone, name, email, address)
            messagebox.showinfo("Update Contact", result)
            self.view_contacts()
        else:
            messagebox.showerror("Error", "Contact not found.")

    def delete_contact(self):
        phone = simpledialog.askstring("Input", "Enter Phone Number of the Contact to Delete:")
        result = self.manager.delete_contact(phone)
        messagebox.showinfo("Delete Contact", result)
        self.view_contacts()

if __name__ == "__main__":
    root = tk.Tk()
    gui = ContactManagerGUI(root)
    root.mainloop()
