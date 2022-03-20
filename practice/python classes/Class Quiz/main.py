from question_model import Question
from data import question_data

question_bank = []
for items in question_data:
    question_text = items["text"]
    question_answer = items["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

print(question_bank)