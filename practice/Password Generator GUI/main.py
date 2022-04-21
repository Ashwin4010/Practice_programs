from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pasword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    password_numbers = [choice(numbers) for number in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(*args):
    web = website_entry.get()
    ema = email_entry.get()
    pas = password_entry.get()
    new_data = {web:{
        "email":ema,
        "password":pas
    }}

    if len(web) == 0 or len(pas) == 0:
        messagebox.showerror(title="Field Empty", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", mode="r") as file:
                #Reading Old data
                data = json.load(file)
        except FileNotFoundError as filenotfound:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            #updateing new data
            data.update(new_data)
            with open("data.json",mode='w') as file:
                #saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="error",message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="error",message=f"No details for {website} found")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website = Label(text="Website: ")
website.grid(row=1, column=0)

email = Label(text="Email/Username: ")
email.grid(row=2, column=0)

password = Label(text="Password: ")
password.grid(row=3, column=0)

# entries

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)
password_entry = Entry(width=35)
password_entry.grid(row=3,column=1)

# buttons

generate_password_button = Button(text="Generate Password",command=generate_pasword)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search",width=10,command=find_password)
search_button.grid(row=1,column=2)

window.mainloop()
