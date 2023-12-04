import tkinter as tk
from tkinter import messagebox

class Phonebook:
    def __init__(self, root):
        self.root = root
        self.root.title("Phonebook")
        self.root.geometry("400x300")

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.phone_label = tk.Label(root, text="Phone Number:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=10)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)

        self.address_label = tk.Label(root, text="Address:")
        self.address_label.grid(row=2, column=0, padx=10, pady=10)
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=2, column=1, padx=10, pady=10)

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=3, column=0, padx=10, pady=10)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=3, column=1, padx=10, pady=10)

        self.save_button = tk.Button(root, text="Save", command=self.save_entry)
        self.save_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.load_button = tk.Button(root, text="Load", command=self.load_entries)
        self.load_button.grid(row=5, column=0, columnspan=2, pady=10)

    def save_entry(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        email = self.email_entry.get()

        entry = f"Name: {name}, Phone: {phone}, Address: {address}, Email: {email}\n"

        with open("phonebook.txt", "a") as file:
            file.write(entry)

        messagebox.showinfo("Phonebook", "Entry saved successfully!")

    def load_entries(self):
        try:
            with open("phonebook.txt", "r") as file:
                entries = file.readlines()

            if not entries:
                messagebox.showwarning("Phonebook", "No entries found!")
            else:
                entry_text = "\n".join(entries)
                self.display_entries(entry_text)
                messagebox.showinfo("Phonebook", "Entries loaded successfully!")
        except FileNotFoundError:
            messagebox.showwarning("Phonebook", "No entries found!")

    def display_entries(self, entry_text):
        popup = tk.Toplevel(self.root)
        popup.title("Phonebook Entries")
        popup.geometry("400x300")

        entries_label = tk.Label(popup, text=entry_text)
        entries_label.pack(padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    phonebook = Phonebook(root)
    root.mainloop()
