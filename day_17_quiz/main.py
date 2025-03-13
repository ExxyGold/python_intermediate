from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


updated_data = question_data["results"]
print("Welcome to Quiz")
question_bank = []

for dictionary in updated_data:
    question_number = dictionary["question"]
    answer = dictionary["correct_answer"]

    values = Question(question_number, answer)

    question_bank.append(values)







quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    



