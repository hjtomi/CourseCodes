from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions = []
for question in question_data:
    new_question = (Question(question["text"], question["answer"]))
    questions.append(new_question)

quiz = QuizBrain(questions)
quiz.next_question()
