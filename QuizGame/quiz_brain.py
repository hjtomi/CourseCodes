class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        question = self.question_list[self.question_number]
        decision = input(f"Q.{self.question_number+1}: {question.text} (True/False)? ")
        self.check_answer(decision, question)

    def check_answer(self, decision, question):
        if decision.title() == question.answer:
            print("gud")
            self.question_number += 1
            if self.question_number < len(self.question_list):
                self.next_question()
        else:
            print("too bad!")
