from tkinter import *
from tkinter import messagebox # not a class, need to import it separately
from random import shuffle, choice, randint 
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = randint(8, 10)
nr_symbols = randint(2, 4)
nr_numbers = randint(2, 4)


def generate_password():
    # Clear the entry
    password_entry.delete(0, 'end')
    # Choose randomly several characters in each array (letters, numbers, symbols)
    password_list = [choice(letters) for char in range(nr_letters)]
    password_list += [choice(symbols) for char in range(nr_symbols)]
    password_list += [choice(numbers) for char in range(nr_numbers)]
    #Shuffle the order of the characters in the list created
    shuffle(password_list)
    # Concatenate the characters of the password_list in a string
    password = "".join(password_list)
    # Insert the password in the entry
    password_entry.insert(0, password)


    

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    # Get data of the entries
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    # Entry verification
    if (len(website) == 0 or len(email) == 0 or len(password) == 0):
        warning = messagebox.showerror(title="Error", message="You can't leave a field empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        # Save data in JSON in an other file
        if is_ok:
            try:
                # UPDATE with JSON
                # Note: to load the content out of the json file (change arg of open() to 'r' for read):
                with open("29-password-app/data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                # WRITE with JSON
                with open("29-password-app/data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                with open("29-password-app/data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                # Clear entries
                website_entry.delete(0, 'end')
                email_entry.delete(0, 'end')
                password_entry.delete(0, 'end')

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password():
    website = website_entry.get()
    try:
        with open("29-password-app/data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        warning = messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            website_password = messagebox.showinfo(title=website, message=f"These are the infos: \nEmail: {email} \nPassword: {password}")
        else:
            no_details_message = messagebox.showinfo(title=website, message="No details for the website exists.")
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=240, height=240)
window.config(padx=20, pady=20, bg="white")


# Lock image (canvas)
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="29-password-app/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Password Form
website_label = Label(text="Website", bg="white")
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username", bg="white")
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password", bg="white")
password_label.grid(column=0, row=3)
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

search_button = Button(text="Search Password", width=33, command=search_password)
search_button.grid(column=1, row=4, columnspan=2)
generate_button = Button(text="Generate Password", width=33, command=generate_password)
generate_button.grid(column=1, row=5, columnspan=2)
add_button = Button(text="Add", width=33, command=save_password)
add_button.grid(column=1, row=6, columnspan=2)


# Keep the window on screen
window.mainloop()
