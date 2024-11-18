from random import choice, randint, shuffle
import pyperclip
from tkinter import messagebox
from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    input_pass.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
   website = input_website.get()
   email = input_email.get()
   password = input_pass.get()
  
   if len(website) ==0 or len(password)==0:
      messagebox.showinfo(title="Error", message="Make sure no fields are empty.")
   else:
    is_okay = messagebox.askokcancel(title=website, message=f" Email: {email}\n Password: {password}\n Proceed?")

    if is_okay:
        with open("./day 29 python/data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            input_website.delete(0,END)
            input_pass.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="./day 29 python/logo.png")
canvas.create_image(100, 100,image = logo)
canvas.grid(column=0, row=0,columnspan=3)

label_website = Label(text="Website: ", font=("Arial", 10, "bold"))
label_website.grid(column=0, row=1)

input_website = Entry(width = 45)
input_website.grid(column=1,row=1, columnspan=2, sticky="w")
input_website.focus()

label_email = Label(text="Email/Username: ", font=("Arial", 10, "bold"))
label_email.grid(column=0, row=2)
input_email = Entry(width = 45)
input_email.grid(column=1,row=2, columnspan=2, sticky="w")
input_email.insert(0,"anymail@gmail.com")

label_pass = Label(text="Password: ", font=("Arial", 10, "bold"))
label_pass.grid(column=0, row=3)
input_pass = Entry(width = 21)
input_pass.grid(column=1,row=3, columnspan=1, sticky="w")
button_pass = Button(text="Generate Password", width=18, command=generate_password)
button_pass.grid(column=2, row=3, columnspan=1, sticky="w")

button_add = Button(text="Add", width=37, command=save)
button_add.grid(column=1, row=4, columnspan=2, sticky="w")


window.mainloop()