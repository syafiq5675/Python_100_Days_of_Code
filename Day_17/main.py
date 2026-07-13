from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    new_q = Question(q["text"], q["answer"])
    question_bank.append(new_q)


Quiz = QuizBrain(question_bank)

while Quiz.still_had_questions():
    Quiz.next_question()

print("\n")
print("You've completed the quiz")
print(f"your final score was: {Quiz.score}/{Quiz.question_number}")