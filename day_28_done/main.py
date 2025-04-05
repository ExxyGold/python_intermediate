from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text = "Timer", fg = GREEN)
    canvas.itemconfig(timer_text, text = "00:00")
    global reps
    reps = 0
    mark_label.config(text = "")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = 5
    break_sec = 5
    long_break_sec = 20
    
    
    if reps % 8 ==0:
        timer_label.config(text = "Long Break", fg = RED)
        countdown(long_break_sec)

    elif reps % 2 !=0:
        timer_label.config(text = "Work", fg = GREEN)
        countdown(work_sec)
    else:
        timer_label.config(text = "Break", fg = PINK)
        countdown(break_sec)
        
    
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60    
    if len(str(count_sec)) == 1:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, countdown, count-1 )
    else:
        start_timer()
        mark = ""
        session = math.floor(reps/2)
        for _ in range(session):
            mark+= "✔"
            
        mark_label.config(text = mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady = 50, bg= YELLOW)




canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness= 0)

tomato_photo = PhotoImage(file = "./day_28/tomato.png")

canvas.create_image(100, 112, image = tomato_photo)
timer_text = canvas.create_text(100, 120, text = "00:00", font = (FONT_NAME, 40, "bold",), fill = "white")
canvas.grid(column = 1, row= 1 )


timer_label = Label(text = "Timer", font = (FONT_NAME, 50), fg = GREEN, bg= YELLOW)
timer_label.config(padx = 5, pady = 5)
timer_label.grid(column = 1, row= 0)

start_button = Button(text="Start", command = start_timer)
start_button.grid(column = 0, row= 2)

mark_label = Label( bg = YELLOW, fg = GREEN, font = (FONT_NAME, 15, "bold"))
mark_label.config(padx= 5, pady= 10)
mark_label.grid(column=1, row = 2)

reset_button = Button(text="Reset", command = reset_timer)
reset_button.grid(column = 2, row= 2)

window.mainloop()