from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = question_bank.append(Question(question_text,question_answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions(): #if quiz still has question remaining
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

