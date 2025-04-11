from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))    ]
    password_numbers = [choice(numbers) for num in range(randint(2, 4)) ]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():
    website= website_entry.get()
    try:
        with open("./day_29/data.json", mode = "r") as up_file:
            data_finder = json.load(up_file)
    except:
        messagebox.showerror(title= "Error", message = 'No data File found')
    else:
        try:
            messagebox.showinfo(title= website, message = f"Email: {data_finder[website]["email"]}\nPassword: {data_finder[website]["password"]}")
        except: 
            messagebox.showerror(title= "Error", message = 'No details for the website exists')

def save():
    email = email_entry.get()
    website = website_entry.get()
    password = password_entry.get()
    new_data = { 
         website: {
              "email": email, 
              "password": password
                           }
         
    }



    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title= "Oops", message= "Please dont leave any of the field empty")
    else:
            try:
                with open("./day_29/data.json", mode = "r") as file:
                 
                    data = json.load(file)
            except:
                with open("./day_29/data.json", mode = "w") as file:
                    json.dump(new_data, file, indent = 4)
                
            else:
                data.update(new_data)
                
                with open("./day_29/data.json", mode = "w") as up_file:
                    json.dump(data, up_file, indent = 4)
                    
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

canvas = Canvas(width= 200, height= 200)
logo = PhotoImage(file= "./day_29/logo.png")
canvas.create_image(100,100, image = logo)
canvas.grid(column = 1, row = 0, columnspan= 2)


website_label = Label(text = "Website:")
website_label.grid(column = 0, row = 1)

email_label = Label(text= "Email/Username:")
email_label.grid(column = 0, row = 2)

password_label = Label(text = "Password:")
password_label.grid(column = 0, row = 3)

website_entry = Entry(width=21)
website_entry.grid(column = 1, row = 1)
website_entry.focus()

email_entry = Entry(width = 41)
email_entry.insert(0, "mokonoghoexalt@gmail.com")
email_entry.grid(column = 1, row = 2, columnspan= 2)

password_entry = Entry(width= 21)
password_entry.grid(column = 1, row = 3)


gen_button = Button(text="Generate Password", command= generate_password)
gen_button.grid(column = 2, row = 3)

add_button = Button(text = "Add", width= 36, command = save)
add_button.grid(column = 1, row = 4, columnspan= 2)

search_button = Button(text = "Search", width = 15, command= find_password)
search_button.grid(column = 2, row = 1)


window.mainloop()