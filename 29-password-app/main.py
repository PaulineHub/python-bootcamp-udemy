from tkinter import *
from tkinter import messagebox # not a class, need to import it separately
from random import shuffle, choice, randint 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = randint(8, 10)
nr_symbols = randint(2, 4)
nr_numbers = randint(2, 4)


def generate_password():
    password_entry.delete(0, 'end')

    #for char in range(nr_letters):
        #password_list.append(random.choice(letters))
    #for char in range(nr_symbols):
        #password_list += random.choice(symbols)
    #for char in range(nr_numbers):
        #password_list += random.choice(numbers)
    password_list = [choice(letters) for char in range(nr_letters)]
    password_list += [choice(symbols) for char in range(nr_symbols)]
    password_list += [choice(numbers) for char in range(nr_numbers)]

    shuffle(password_list)

    #password = ""
    #for char in password_list:
        #password += char
    password = "".join(password_list)
    password_entry.insert(0, password)


    

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    # Add datas to data.txt file
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if (len(website) == 0 or len(email) == 0 or len(password) == 0):
        warning = messagebox.showerror(title="Error", message="You can't leave a field empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            # Create a file if it doesn't exist and append content
            with open("29-password-app/data.txt", "a") as f:
                f.write(f"{website} | {email} | {password} \n")
            # Clear entries
            website_entry.delete(0, 'end')
            email_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


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

generate_button = Button(text="Generate Password", width=33, command=generate_password)
generate_button.grid(column=1, row=4, columnspan=2)
add_button = Button(text="Add", width=33, command=save_password)
add_button.grid(column=1, row=5, columnspan=2)


# Keep the window on screen
window.mainloop()
