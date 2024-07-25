import tkinter as tk

def create_window():
    global root, frame, name_entry, email_entry, phone_entry, branch_vars, file_format_var, submit_button, download_button, clear_button

    # To create the user interface 
    root = tk.Tk()
    root.title("Form")
    root.configure(background="#a8a232")  

   
    label = tk.Label(root, text="User Data Form", font=("Roboto", 35))
    label.pack()

    # pack the main frame
    frame = tk.Frame(root, bg="#a8a232")
    frame.pack(padx=100, pady=100)


    name_label = tk.Label(frame, text="Name", font=("Arial", 20))
    name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    name_entry = tk.Entry(frame, font=("Helvetica", 15))
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    email_label = tk.Label(frame, text="Email ID", font=("Arial", 20), bg="#f0f0f0")
    email_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
    email_entry = tk.Entry(frame, font=("Helvetica", 15), bg="#ffffff")
    email_entry.grid(row=1, column=1, padx=10, pady=10)

  
    phone_label = tk.Label(frame, text="Phone Number", font=("Arial", 20), bg="#f0f0f0")
    phone_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    phone_entry = tk.Entry(frame, font=("Helvetica", 15), bg="#ffffff")
    phone_entry.grid(row=2, column=1, padx=10, pady=10)

    # BooleanVar objects are created to track branch selections
    branch_vars = {
        "Engineering": tk.BooleanVar(),
        "Medical": tk.BooleanVar(),
        "Degree": tk.BooleanVar()
    }

    #branch creation
    branch_frame = tk.Frame(frame, bg="#f0f0f0")
    branch_label = tk.Label(branch_frame, text="Branch", font=("Arial", 20), bg="#f0f0f0")
    branch_label.pack(side=tk.LEFT)
    engineering_checkbox = tk.Checkbutton(branch_frame, text="Engineering", variable=branch_vars["Engineering"], font=("Helvetica", 15), bg="#f0f0f0")
    engineering_checkbox.pack(side=tk.LEFT)
    medical_checkbox = tk.Checkbutton(branch_frame, text="Medical", variable=branch_vars["Medical"], font=("Helvetica", 15), bg="#f0f0f0")
    medical_checkbox.pack(side=tk.LEFT)
    degree_checkbox = tk.Checkbutton(branch_frame, text="Degree", variable=branch_vars["Degree"], font=("Helvetica", 15), bg="#f0f0f0")
    degree_checkbox.pack(side=tk.LEFT)
    branch_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    file_format_var = tk.StringVar(value='json')
    file_format_label = tk.Label(frame, text="File Format", font=("Arial", 20), bg="#f0f0f0")
    file_format_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
    file_format_menu = tk.OptionMenu(frame, file_format_var, 'json', 'txt', 'xml', 'xlsx')
    file_format_menu.grid(row=4, column=1, padx=10, pady=10)

    #buttons
    submit_button = tk.Button(frame, text="Submit", font=("Arial", 20), bg="#4CAF50", fg="white")
    submit_button.grid(row=7, column=0, padx=10, pady=10)

    download_button = tk.Button(frame, text="Download", font=("Arial", 20), bg="#2196F3", fg="white")
    download_button.grid(row=7, column=1, padx=10, pady=10)

    clear_button = tk.Button(frame, text="Clear", font=("Arial", 20), bg="#FF9800")
    clear_button.grid(row=7, column=2, columnspan=2, padx=10, pady=10)

    # Return to be used in the main application
    return root, name_entry, email_entry, phone_entry, branch_vars, file_format_var, submit_button, download_button, clear_button