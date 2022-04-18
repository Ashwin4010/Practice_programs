from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0,column=1)

website = Label(text="Website: ")
website.grid(row=1,column=0)


email = Label(text="Email/Username: ")
email.grid(row=2,column=0)

password = Label(text="Password: ")
password.grid(row=3,column=0)

# entries

website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"example@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

#buttons

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3,column=2)
add_button = Button(text="Add", width= 36)
add_button.grid(row=4,column=1,columnspan=2)




window.mainloop()