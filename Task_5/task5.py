import tkinter as tk
from tkinter import messagebox, simpledialog
import json

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Information Manager")

        self.contacts = []
        self.file_path = "contacts.json"
        self.load_contacts_from_file()

        self.name_label = tk.Label(root, text="Name:")
        self.name_entry = tk.Entry(root)

        self.phone_label = tk.Label(root, text="Phone Number:")
        self.phone_entry = tk.Entry(root)

        self.email_label = tk.Label(root, text="Email:")
        self.email_entry = tk.Entry(root)

        self.address_label = tk.Label(root, text="Address:")
        self.address_entry = tk.Entry(root)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)

        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=10)
        self.update_button.grid(row=7, column=0, columnspan=2, pady=10)
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
            self.save_contacts_to_file()
        else:
            messagebox.showerror("Error", "Name and Phone Number are required fields.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("No Contacts", "No contacts found.")
            return

        contact_list = "Contact List:\n"
        for idx, contact in enumerate(self.contacts, start=1):
            contact_list += f"{idx}. {contact['Name']} - {contact['Phone']}\n"

        messagebox.showinfo("Contacts", contact_list)

    def search_contact(self):
        search_query = simpledialog.askstring("Search", "Enter name or phone number:")
        if not search_query:
            return

        results = []
        for contact in self.contacts:
            if search_query.lower() in contact['Name'].lower() or search_query in contact['Phone']:
                results.append(contact)

        if not results:
            messagebox.showinfo("No Results", "No matching contacts found.")
        else:
            result_str = "Search Results:\n"
            for idx, result in enumerate(results, start=1):
                result_str += f"{idx}. {result['Name']} - {result['Phone']}\n"
            messagebox.showinfo("Search Results", result_str)

    def update_contact(self):
        search_query = simpledialog.askstring("Update", "Enter name or phone number:")
        if not search_query:
            return

        for contact in self.contacts:
            if search_query.lower() in contact['Name'].lower() or search_query in contact['Phone']:
                new_name = simpledialog.askstring("Update", "Enter new name (press enter to keep the same):", initialvalue=contact['Name'])
                new_phone = simpledialog.askstring("Update", "Enter new phone number (press enter to keep the same):", initialvalue=contact['Phone'])
                new_email = simpledialog.askstring("Update", "Enter new email (press enter to keep the same):", initialvalue=contact['Email'])
                new_address = simpledialog.askstring("Update", "Enter new address (press enter to keep the same):", initialvalue=contact['Address'])

                contact['Name'] = new_name if new_name else contact['Name']
                contact['Phone'] = new_phone if new_phone else contact['Phone']
                contact['Email'] = new_email if new_email else contact['Email']
                contact['Address'] = new_address if new_address else contact['Address']

                messagebox.showinfo("Success", "Contact updated successfully!")
                self.save_contacts_to_file()
                return

        messagebox.showinfo("No Results", "No matching contacts found.")

    def delete_contact(self):
        search_query = simpledialog.askstring("Delete", "Enter name or phone number:")
        if not search_query:
            return

        for contact in self.contacts:
            if search_query.lower() in contact['Name'].lower() or search_query in contact['Phone']:
                self.contacts.remove(contact)
                messagebox.showinfo("Success", "Contact deleted successfully!")
                self.save_contacts_to_file()
                return

        messagebox.showinfo("No Results", "No matching contacts found.")

    def load_contacts_from_file(self):
        try:
            with open(self.file_path, 'r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = []
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Error decoding contacts file.")

    def save_contacts_to_file(self):
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.contacts, file, indent=2)
        except Exception as e:
            messagebox.showerror("Error", f"Error saving contacts to file: {str(e)}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
