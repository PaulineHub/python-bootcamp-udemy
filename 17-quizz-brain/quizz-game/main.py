from data import question_data
from question_cls import Question
from quiz_brain_cls import Quiz_brain

question_bank = []

for question in question_data:
  question_item = Question(question["text"], question["answer"])
  question_bank.append(question_item)

quiz = Quiz_brain(question_bank)

while quiz.still_has_questions():
  quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was {quiz.score}/{quiz.question_number}.")
