from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
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
                                text="This is a question test", 
                                font=("Arial", 20, "italic"), 
                                fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons
        button_true_img = PhotoImage(file="34-trivia-api/images/true.png")
        self.button_true = Button(image=button_true_img, highlightthickness=0)
        self.button_true.grid(column=0, row=2)
        button_false_img = PhotoImage(file="34-trivia-api/images/false.png")
        self.button_false = Button(image=button_false_img, highlightthickness=0)
        self.button_false.grid(column=1, row=2)

        # Keep window open
        self.window.mainloop()
