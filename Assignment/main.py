import tkinter as tk
from tkinter import messagebox
from frontend import create_window
from backend import save_data_to_excel, download_data

def main():
    root, name_entry, email_entry, phone_entry, branch_vars, file_format_var, submit_button, download_button, clear_button = create_window()

    # This will store the data that has been submitted
    submitted_data = []

    def submit_data():
        name = name_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        branches = [branch for branch, var in branch_vars.items() if var.get()]

        # Validate that all required fields are filled and at least one branch is selected
        if name and email and phone and branches:
            branch_str = ', '.join(branches)
            save_data_to_excel(name, email, phone, branch_str)
            messagebox.showinfo("Success", "Data saved successfully!")
            nonlocal submitted_data
            # Store the submitted data in a structured format
            submitted_data = [{
                "Name": name,
                "Email": email,
                "Phone": phone,
                "Branch": branch_str
            }]
        else:
            # error message will be displayed if there is any missing field.
            messagebox.showerror("Error", "All fields are required!")

    def download_file():
        file_format = file_format_var.get()
        download_data(file_format)

    def clear_input():
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        for var in branch_vars.values():
            var.set(False)

    # Configure buttons 
    submit_button.config(command=submit_data)
    download_button.config(command=download_file)
    clear_button.config(command=clear_input)

    root.mainloop()

# Ensure that the main function is called when the script is executed
if __name__ == "__main__":
    main()