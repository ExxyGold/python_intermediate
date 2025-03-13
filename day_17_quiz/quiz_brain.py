class QuizBrain:
    def __init__(self, list ):
       self.question_number = 0
       self.question_list = list
       self.score = 0


    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print(f" your final score is {self.score}/{self.question_number}")   
            return False


    def next_question(self):

        current_question = self.question_list[self.question_number]
        self.question_number += 1
        
        user_answer = input(f"Q: {self.question_number} {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)
        

    def check_answer(self, user_answer, correct_answer):
        self.correct = correct_answer
        self.user_answer = user_answer

        if self.correct == self.user_answer:
            self.score += 1
            print("You got it Right")
        else:
            print(f"You got it wrong")
        print(f"The correct answer is {correct_answer}\n")
