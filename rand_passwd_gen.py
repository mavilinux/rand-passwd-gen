import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # For ComboBox
import secrets
import string
import os
from datetime import datetime
import pyperclip  # For clipboard functionality

def generate_password(length, complexity):
    """Generates a random password based on the selected length and complexity level."""
    if complexity == 'simple':
        characters = string.ascii_letters + string.digits  # Letters and digits
    elif complexity == 'complex':
        characters = string.ascii_letters + string.digits + string.punctuation  # Letters, digits, and punctuation
    else:
        raise ValueError("Complexity level not recognized.")

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def save_to_file(site_name, email_username, password):
    """Saves the generated password details to a text file with the date."""
    file_path = "passwords.txt"
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current date and time
    content = f"Site Name: {site_name}\nEmail/Username: {email_username}\nPassword: {password}\nDate: {current_date}\n{'-' * 40}\n"

    with open(file_path, "a") as file:
        file.write(content)

    messagebox.showinfo("Success", f"Password details saved to {file_path}")

def on_generate_password():
    """Handles the GUI actions for password generation and saving."""
    site_name = site_name_entry.get()
    email_username = email_username_entry.get()
    password_length = int(password_length_combobox.get())
    complexity = complexity_combobox.get()

    if not site_name or not email_username:
        messagebox.showwarning("Input Error", "Please fill in both Site Name and Email/Username.")
        return

    password = generate_password(password_length, complexity)
    password_label.config(text=f"Generated Password: {password}")  # Display password in GUI
    save_to_file(site_name, email_username, password)

def copy_to_clipboard():
    """Copies the generated password to clipboard."""
    password = password_label.cget("text").replace("Generated Password: ", "")
    if password != "None":
        pyperclip.copy(password)  # Copy password to clipboard
        messagebox.showinfo("Success", "Password copied to clipboard.")
    else:
        messagebox.showwarning("No Password", "Please generate a password first.")

def on_exit():
    """Exit the GUI application."""
    root.quit()

# Set up the Tkinter GUI
root = tk.Tk()
root.title("Random Password Generator")

# Set up the input fields and labels
tk.Label(root, text="Site Name:").grid(row=0, column=0, padx=10, pady=5)
site_name_entry = tk.Entry(root, width=30)
site_name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Email/Username:").grid(row=1, column=0, padx=10, pady=5)
email_username_entry = tk.Entry(root, width=30)
email_username_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Password Length:").grid(row=2, column=0, padx=10, pady=5)

# Replace OptionMenu with Combobox for password length selection
password_length_combobox = ttk.Combobox(root, values=["4", "8", "16"], state="readonly", width=27)
password_length_combobox.set("8")  # Default value
password_length_combobox.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Password Complexity:").grid(row=3, column=0, padx=10, pady=5)

# Replace OptionMenu with Combobox for complexity selection
complexity_combobox = ttk.Combobox(root, values=["simple", "complex"], state="readonly", width=27)
complexity_combobox.set("simple")  # Default value
complexity_combobox.grid(row=3, column=1, padx=10, pady=5)

# Display for generated password
password_label = tk.Label(root, text="Generated Password: None", fg="green")
password_label.grid(row=4, column=0, columnspan=2, pady=10)

# Set up the buttons
generate_button = tk.Button(root, text="Generate and Save Password", command=on_generate_password)
generate_button.grid(row=5, column=0, columnspan=2, pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=6, column=0, columnspan=2, pady=5)

exit_button = tk.Button(root, text="Exit", command=on_exit)
exit_button.grid(row=7, column=0, columnspan=2, pady=5)

# Run the GUI
root.mainloop()
