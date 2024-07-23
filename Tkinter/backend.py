import os
import json
import openpyxl
from openpyxl import Workbook
import xml.etree.ElementTree as ET
from tkinter import filedialog, messagebox

# Excel File Path where the data will append from the user.
excel_file = r"C:\Users\T.Venkateshwar Reddy\OneDrive\Desktop\data.xlsx"

def create_excel_file():
    if not os.path.exists(excel_file):
        wb = Workbook()  # Create a new workbook
        ws = wb.active  
        ws.title = "UserData"  
        ws.append(["Name", "Email ID", "Phone Number", "Branch"])
        wb.save(excel_file)  # Save the workbook to the file

def save_data_to_excel(name, email, phone, branch_str):   #here the user data will be added to the excel file

    wb = openpyxl.load_workbook(excel_file) 
    ws = wb.active  
    ws.append([name, email, phone, branch_str])
    wb.save(excel_file)  # Save the workbook

def save_as_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f)  #  JSON file format.

def save_as_txt(data, file_path):
    with open(file_path, 'w') as f:
        for entry in data:
            f.write(f"{entry}\n")  # TXT file format.

def save_as_xml(data, file_path):
    root = ET.Element("Users")  # Create the root XML element
    for entry in data:
        user = ET.SubElement(root, "User")  # Create a 'User' element for each entry
        for key, value in entry.items():
            ET.SubElement(user, key).text = value  # Add sub-elements 
    tree = ET.ElementTree(root) 
    tree.write(file_path)  # XML File format.

def download_data(file_format, data):
    # Prompt the user for file path.
    file_path = filedialog.asksaveasfilename(defaultextension=f".{file_format}", 
                                             filetypes=[(file_format.upper(), f"*.{file_format}")])
    if not file_path:
        return 
    
    # Save data in the selected format
    if file_format == 'json':
        save_as_json(data, file_path)
    elif file_format == 'txt':
        save_as_txt(data, file_path)
    elif file_format == 'xml':
        save_as_xml(data, file_path)
    elif file_format == 'xlsx':
        wb = Workbook()  
        ws = wb.active  
        ws.title = "UserData"  
        ws.append(["Name", "Email ID", "Phone Number", "Branch"])  
        for entry in data:
            ws.append([entry['Name'], entry['Email'], entry['Phone'], entry['Branch']])  # Append each entry into the file
        wb.save(file_path)  # Save the workbook to the file
    
    # Inform the user that the file has been downloaded
    messagebox.showinfo("Download", f"Downloaded as {file_format}")