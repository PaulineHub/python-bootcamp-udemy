from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain): # indicate the type of parameter expected
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Trivia Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(text="score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        # Text
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
                                150, 125, 
                                width=280,
                                text="This is a question test", 
                                font=("Arial", 20, "italic"), 
                                fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons
        button_true_img = PhotoImage(file="34-trivia-api/images/true.png")
        self.button_true = Button(
            image=button_true_img, highlightthickness=0, command=self.true_pressed)
        self.button_true.grid(column=0, row=2)
        button_false_img = PhotoImage(file="34-trivia-api/images/false.png")
        self.button_false = Button(
            image=button_false_img, highlightthickness=0, command=self.false_pressed)
        self.button_false.grid(column=1, row=2)

        self.get_next_question()

        # Keep window open
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_txt = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_txt)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        
    