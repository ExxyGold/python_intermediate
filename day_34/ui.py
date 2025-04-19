from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg= THEME_COLOR)


        self.score_label = Label(text= f"Score: {0}", bg= THEME_COLOR, fg= "white", font = ("Ariel", 15 ))
        self.score_label.grid(column= 1, row= 0) 


        self.canvas = Canvas(width=300, height=250, bg= "white")
        self.question_text = self.canvas.create_text(
            150,
            125, 
            width= 280,
            text = "Type in here", fill = THEME_COLOR, 
            font = ("Arial", 20, "italic"))
        
        self.canvas.grid(column= 0, row= 1, columnspan= 2, pady= 50)
        

        true = PhotoImage(file="./day_34/images/true.png")
        false = PhotoImage(file="./day_34/images/false.png")

        self.true_button = Button(image= true, highlightthickness= 0, command= self.pick_true)
        self.true_button.grid(column = 0, row = 2)

        self.false_button = Button(image= false, highlightthickness= 0, command = self.pick_false)
        self.false_button.grid(column = 1, row = 2)

        self.get_next_question()

        self.window.mainloop()
        
    def pick_true(self):
        is_right = self.quiz.check_answer("true")
        self.score_label.config(text= f"Score: {self.quiz.score}")
        self.give_feedback(is_right)

        if self.quiz.still_has_questions() == False:
            self.true_button.config(command= self.game_over)
            self.false_button.config(command= self.game_over)

    def pick_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)
    
        self.score_label.config(text= f"Score: {self.quiz.score}")


    def game_over(self):
        messagebox.showinfo(title= "Trivia Completed", message= f"Your total score is {self.quiz.score}/10")
        


    def get_next_question(self):
        self.canvas.config(bg = "white")
        if self.quiz.still_has_questions(): 
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text )
        else:
            self.canvas.itemconfig(self.question_text, text = "You have come to the End of the Quiz")
            self.true_button.config(command= self.game_over)
            self.false_button.config(command= self.game_over)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg= "green")
        else:
            self.canvas.config(bg = "red")
        
        self.show_color = self.window.after(1000, self.get_next_question)
    
        
    