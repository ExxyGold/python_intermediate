
import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    word_doc =pandas.read_csv("./day_31/to_learn/to_learn.csv")

except:
    word_doc =pandas.read_csv("./day_31/data/french_words.csv")


word_dict = {row.French: row.English for (index, row) in word_doc.iterrows()}

alt_dict = word_doc.to_dict(orient = "records")

# print(alt_dict)

french_list = []

for keys in word_dict:
    single_dict = {"French": keys, "English": word_dict[keys]}
    french_list.append(single_dict)

chosen_dict = {}


def gen_word():
    global flip_time
    window.after_cancel(flip_time)
    global chosen_dict
    chosen_dict = random.choice(french_list)
    canvas.itemconfig(cover, image = frontground )
    flip_time= window.after(3000, change_background)

    for key in chosen_dict:
        if key == "French":
            canvas.itemconfig(word, text = chosen_dict[key], fill = "black")
            canvas.itemconfig(language, text = key, fill = "black")
    
    


def change_background():
    canvas.itemconfig(cover, image = background)
    for key in chosen_dict:
        if key == "English":
            canvas.itemconfig(word, text = chosen_dict[key], fill = "white")
            canvas.itemconfig(language, text = key, fill = "white")
    

def checker():
    
    gen_word()
    french_list.remove(chosen_dict)

    new_file = pandas.DataFrame(french_list)

    new_file.to_csv("./day_31/to_learn.csv", index = False)
    




window = Tk()

window.title("Flashy")
window.config(padx= 30, pady = 30, bg= BACKGROUND_COLOR)

flip_time= window.after(3000, change_background)



background = PhotoImage(file = "./day_31/images/card_back.png")
frontground = PhotoImage(file = "./day_31/images/card_front.png")
wrong = PhotoImage(file = "./day_31/images/wrong.png")
right = PhotoImage(file = "./day_31/images/right.png")


canvas = Canvas(height= 526, width = 810, highlightthickness= 0, bg = BACKGROUND_COLOR)


cover = canvas.create_image(400, 263, image = frontground  )
language = canvas.create_text(400,150, text= "Title", font= ("Ariel", 40, "italic"))
word = canvas.create_text(400,263, text= "Word", font= ("Ariel", 60, "bold"))
canvas.grid(column= 0, row = 0, columnspan= 2)


right_button = Button(image = right, highlightthickness=0, command= checker)
right_button.grid(column= 0, row = 1)

wrong_button = Button(image = wrong, highlightthickness=0, command= gen_word)
wrong_button.grid(column = 1, row = 1)

gen_word()

window.mainloop()