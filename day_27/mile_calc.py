from tkinter import *

windows = Tk()

windows.title("Mile to KM Converter")
windows.config(padx= 30, pady= 30)



def converter():
    value = round(float(entry.get()) * 1.60934, 2)

    result_label.config(text = value)

entry = Entry(width= 10)
entry.grid(column= 1, row= 0)





#Create Labels
miles = Label(text= "Miles", font = ("Arial", 11, "normal"))
miles.config(padx=10, pady= 10)
miles.grid(column = 2, row = 0)

equal_to = Label(text= "is equal to", font = ("Arial", 11, "normal"))
equal_to.config(padx=10, pady= 10)
equal_to.grid(column = 0, row = 1)

result_label = Label(text= 0, font = ("Arial", 11, "normal"))
result_label.grid(column = 1, row = 1)

kilometer = Label(text= "Km", font = ("Arial", 11, "normal"))
kilometer.grid(column = 2, row = 1)

calc_button = Button(text="Calculate", command= converter)
calc_button.grid(column = 1, row = 3)


windows.mainloop()