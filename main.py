from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.title("Contact Management System")
# window.geometry("600x400")

frame = Frame(window)
frame.pack()

# Saving user info
user_info_frame = LabelFrame(frame, text="User Information")
user_info_frame.grid(row= 0, column= 0, padx= 20, pady=20)

# label
first_name_label = Label(user_info_frame, text= "First Name")
first_name_label.grid(row= 0, column= 0)

last_name_label = Label(user_info_frame, text= "Last Name")
last_name_label.grid(row= 0, column= 1)

company_name_label = Label(user_info_frame, text= "Company")
company_name_label.grid(row= 0, column= 2)

# taking entry on first and last name
first_name_entry = Entry(user_info_frame)
last_name_entry = Entry(user_info_frame)

first_name_entry.grid(row= 1, column= 0)
last_name_entry.grid(row= 1, column= 1)

company_name_entry = Entry(user_info_frame)
company_name_entry.grid(row=1, column=2)

# creating label of mr mrs ..
title_label = Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["Mr.", "Ms.",  "Mrs.", "Other"])
title_combobox.current(0)

title_label.grid(row= 2, column= 0)
title_combobox.grid(row= 3, column= 0)

# age_label = Label(user_info_frame, text= "Age")
# age_spinbox = Spinbox(user_info_frame, from_= 0, to= 100)

# age_label.grid(row= 2, column= 1)
# age_spinbox.grid(row= 3, column= 1)

# creating space between the widget
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx = 10, pady= 5)

# creating next widget
contact_info_frame = LabelFrame(frame, text="Contact Information")
contact_info_frame.grid(row= 1, column= 0,padx= 10, pady=10)

phone_number_label = Label(contact_info_frame, text="Phone Number")
phone_number_code_combobox = ttk.Combobox(contact_info_frame, values= ["+91","+977", "+61"], width= 10)

phone_number_label.grid(row= 1, column= 0)
phone_number_code_combobox.grid(row= 2, column= 0)
phone_number_code_combobox.current(0)

phone_number_entry = Entry(contact_info_frame)
phone_number_entry.grid(row= 2, column= 1)

# storage
temp_username = StringVar()

email_label = Label(contact_info_frame, text= "Email")
email_entry = Entry(contact_info_frame, textvariable= temp_username)

email_label.grid(row=1, column =2)
email_entry.grid(row=2, column= 2)
# creating space for contact info
for widget in contact_info_frame.winfo_children():
    widget.grid_configure(padx=5,pady= 5)

# taking data

import re
def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def validate_phone(phone):
    cleaned_number = re.sub(r'\D', '', phone)

    pattern = r'\d{10}$'

    return re.match(pattern, cleaned_number) is not None

def save():
    firstname = first_name_entry.get()
    
    if firstname != "" :
        lastname = last_name_entry.get()
        company = company_name_entry.get()
        title = title_combobox.get()
        phonenumber = phone_number_entry.get()
        email = email_entry.get()
        val_num = validate_phone(phonenumber)
        validate = validate_email(email)
        phonenumbercode = phone_number_code_combobox.get()

        if phonenumber.strip() or email.strip():
            if phonenumber.strip():
                if email.strip():
                    if (val_num == True and validate == True):
                        print(f"Name: {title} {firstname} {lastname}\ncompany: {company}\nphone Number: {phonenumbercode} {phonenumber}\nemail: {email}")
                        print("\n-------------------------------------------------------------------\n")
                    else:
                        messagebox.showerror('Error','Invalid Phone Number/Email')
                else:
                    if (val_num == True):
                        print(f"Name: {title} {firstname} {lastname}\ncompany: {company}\nphone Number: {phonenumbercode} {phonenumber}\nemail: {email}")
                        print("\n-------------------------------------------------------------------\n")
                    else:
                        messagebox.showerror('Error','Invalid Phone Number')
                
            elif email.strip():
                if validate == True:
                    print(f"Name: {title} {firstname} {lastname}\ncompany: {company}\nphone Number: {phonenumbercode} {phonenumber}\nemail: {email}")
                    print("\n-------------------------------------------------------------------\n")
                else:
                    messagebox.showerror('Error','Invalid Email')
        
        else:
            messagebox.showerror("Error!", "Please enter phone number or email")
    else:
        messagebox.showerror("Error!", "Please enter your First Name.")


def clear():
    print("suces")



def delete():
    print("ok")


def update():
    print("ok")

# Button widget frame
button_frame = Label(frame, text="Submit Field")
button_frame.grid(row=2,column=0)

clear_button = Button(button_frame, text= "Clear", command= clear)
save_button = Button(button_frame, text="Save", command= save)
delete_button = Button(button_frame, text= "Delete", command= delete)
update_button = Button(button_frame, text= "Update", command= update)

clear_button.grid(row= 1, column= 0)
save_button.grid(row= 1, column= 1)
delete_button.grid(row= 1, column= 2)
update_button.grid(row= 1, column= 3)






window.mainloop()