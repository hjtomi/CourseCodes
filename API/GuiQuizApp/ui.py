from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # setup
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.label_score = Label(text="Score: ", background=THEME_COLOR, foreground="white", font=("Arial", 12, "normal"))
        self.canvas = Canvas(width=300, height=250)
        self.text_question = self.canvas.create_text(150,
                                                     125,
                                                     text="Hello brian",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR,
                                                     width=280)

        self.img_true = PhotoImage(file="images/true.png")
        self.img_false = PhotoImage(file="images/false.png")

        self.button_true = Button(image=self.img_true, command=self.answer_true)
        self.button_false = Button(image=self.img_false, command=self.answer_false)

        # grid
        self.label_score.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.button_true.grid(row=2, column=0)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_question, text=q_text)
        else:
            self.canvas.itemconfig(self.text_question, text="You have reached the end.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def answer_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")

        self.window.after(1000, self.get_next_question)
