import tkinter as tk
from tkinter import messagebox
from frontend import create_window
from backend import create_excel_file, save_data_to_excel, download_data

def main():
    # Create the initial Excel file if it doesn't exist
    create_excel_file()

    # Create the main window and get references to UI elements
    root, name_entry, email_entry, phone_entry, branch_vars, file_format_var, submit_button, download_button, clear_button = create_window()

    # This will store the data that has been submitted
    submitted_data = []

    def submit_data():
        """
        Collects data from the user input fields, validates them, and saves the data
        to an Excel file. Updates the `submitted_data` list with the collected data.
        """
        name = name_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        branches = [branch for branch, var in branch_vars.items() if var.get()]

        # Validate that all required fields are filled and at least one branch is selected
        if name and email and phone and branches:
            branch_str = ', '.join(branches)
            # Save the collected data to the Excel file
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
            # Show an error message if any field is missing
            messagebox.showerror("Error", "All fields are required!")

    def download_file():
        """
        Handles the downloading of the submitted data in the selected file format.
        Shows an error message if no data has been submitted yet.
        """
        if submitted_data:
            file_format = file_format_var.get()
            download_data(file_format, submitted_data)
        else:
            # Show an error message if no data is available for download
            messagebox.showerror("Error", "Enter the Data First.")

    def clear_input():
        """
        Clears all input fields and resets the branch checkboxes.
        """
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        for var in branch_vars.values():
            var.set(False)

    # Configure buttons with their corresponding functions
    submit_button.config(command=submit_data)
    download_button.config(command=download_file)
    clear_button.config(command=clear_input)

    # Start the Tkinter event loop
    root.mainloop()

# Ensure that the main function is called when the script is executed
if __name__ == "__main__":
    main()