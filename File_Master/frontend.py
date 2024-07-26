import tkinter as tk

#function to create the frontend window
def create_window():

    #global variables
    global root, frame, name_entry, email_entry, phone_entry, branch_vars, file_format_var, submit_button, download_button, clear_button

    #User Interface Description
    root = tk.Tk()
    root.title("User Data Form")
    root.configure(background="#aba8a7")

    label = tk.Label(root, text="User Data Form", font=("Arial", 35), bg="#aba8a7", fg="#333333")
    label.pack(pady=20)   #heading 

    frame = tk.Frame(root, bg="#F5F5F5")
    frame.pack(padx=50, pady=50)

    #creating Name , Email ID , Phone Number with necessary styling

    name_label = tk.Label(frame, text="Name", font=("Arial", 20), bg="#F5F5F5", fg="#333333")
    name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    name_entry = tk.Entry(frame, font=("Helvetica", 15), bg="#FFFFFF", fg="#333333")
    name_entry.grid(row=0, column=1, padx=10, pady=10)    

    email_label = tk.Label(frame, text="Email ID", font=("Arial", 20), bg="#F5F5F5", fg="#333333")
    email_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
    email_entry = tk.Entry(frame, font=("Helvetica", 15), bg="#FFFFFF", fg="#333333")
    email_entry.grid(row=1, column=1, padx=10, pady=10)

    phone_label = tk.Label(frame, text="Phone Number", font=("Arial", 20), bg="#F5F5F5", fg="#333333")
    phone_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    phone_entry = tk.Entry(frame, font=("Helvetica", 15), bg="#FFFFFF", fg="#333333")
    phone_entry.grid(row=2, column=1, padx=10, pady=10)

    # BooleanVar objects are created to track branch selections
    branch_vars = {
        "Engineering": tk.BooleanVar(),
        "Medical": tk.BooleanVar(),
        "Degree": tk.BooleanVar()
    }

    # Branch creation
    branch_frame = tk.Frame(frame, bg="#F5F5F5")
    branch_label = tk.Label(branch_frame, text="Branch", font=("Arial", 20), bg="#F5F5F5", fg="#333333")
    branch_label.pack(side=tk.LEFT)

    #Checkbox creation
    engineering_checkbox = tk.Checkbutton(branch_frame, text="Engineering", variable=branch_vars["Engineering"], font=("Helvetica", 15), bg="#F5F5F5", fg="#333333")
    engineering_checkbox.pack(side=tk.LEFT, padx=5)   #engineering checkbox

    medical_checkbox = tk.Checkbutton(branch_frame, text="Medical", variable=branch_vars["Medical"], font=("Helvetica", 15), bg="#F5F5F5", fg="#333333")
    medical_checkbox.pack(side=tk.LEFT, padx=5)      #medical checkbox

    degree_checkbox = tk.Checkbutton(branch_frame, text="Degree", variable=branch_vars["Degree"], font=("Helvetica", 15), bg="#F5F5F5", fg="#333333")
    degree_checkbox.pack(side=tk.LEFT, padx=5)      #degree checkbox
    branch_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


    file_format_var = tk.StringVar(value='json')
    file_format_label = tk.Label(frame, text="File Format", font=("Arial", 20), bg="#F5F5F5", fg="#333333")
    file_format_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

    #drop down menu for file formats
    file_format_menu = tk.OptionMenu(frame, file_format_var, 'json', 'txt', 'xml', 'xlsx')
    file_format_menu.config(font=("Helvetica", 15), bg="#FFFFFF", fg="#333333")
    file_format_menu.grid(row=4, column=1, padx=10, pady=10)

    #Submit Button
    submit_button = tk.Button(frame, text="Submit", font=("Arial", 20), bg="#4CAF50", fg="white")
    submit_button.grid(row=5, column=0, padx=10, pady=10, sticky=tk.EW)   #button styling
    
    #Download Button
    download_button = tk.Button(frame, text="Download", font=("Arial", 20), bg="#2196F3", fg="white")
    download_button.grid(row=5, column=1, padx=10, pady=10, sticky=tk.EW)     #button styling
     
    #Clear Button
    clear_button = tk.Button(frame, text="Clear", font=("Arial", 20), bg="#FF9800", fg="white")
    clear_button.grid(row=5, column=2, padx=10, pady=10, sticky=tk.EW)         #button styling

    # Return values which are to be used in the main.py 
    return root, name_entry, email_entry, phone_entry, branch_vars, file_format_var, submit_button, download_button, clear_button

