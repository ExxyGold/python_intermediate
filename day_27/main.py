from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width = 500, height= 300)
window.config(padx= 100, pady= 200)
# Label

my_label = Label(text = "I am a Label", font = ("Arial", 24, "bold"))
my_label["text"] = "New TEXT"
my_label.grid(column = 0, row=0)
my_label.config(padx= 50, pady= 50)




#Button

def button_clicked():
    my_label.config(text = entry.get())
button = Button(text = "Click Me", command = button_clicked)
button.grid(column=1, row=1)

button2 = Button(text = "Dont Click", command= button_clicked)
button2.grid(column =2, row = 0)
#Entry
entry= Entry(width = 30)
# entry.insert(END, string= "Something to begin with")
print(entry.get())
entry.grid(column= 3, row=2)






#text
# text = Text(width= 30, height = 5)

# text.focus()
# text.pack()
# text.insert(END, "Example of Multi-line text entry\nI am a boy")
# print(text.get("2.0", END ))

# #Spinbox
# def spinbox_used():
#     print(spinbox.get())

# spinbox = Spinbox(from_= 0, to= 10, width = 5, command = spinbox_used)
# spinbox.pack()

# #Scale
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to= 100, command= scale_used)
# scale.pack()

# #Checkbox

# def checkbutton_used():
#     print(checked_state.get())

# checked_state = IntVar()
# checkbutton = Checkbutton(text = "Is on", variable= checked_state, command = checkbutton_used)
# checkbutton.pack()

# def radio_used():
#     print(radio_state.get())
# radio_state = IntVar()

# radio1 = Radiobutton(text= "Option1", value = 1, variable= radio_state, command= radio_used)
# radio2 = Radiobutton(text= "Option2", value = 2, variable = radio_state, command=radio_used)

# radio1.pack()
# radio2.pack()


# #List Box
# def listbox_used(event):
#     print(listbox.get(listbox.curselection()))

# listbox = Listbox(height= 4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]

# for items in fruits:
#     listbox.insert(fruits.index(items), items)

# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()



window.mainloop()



