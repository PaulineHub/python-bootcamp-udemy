from tkinter import *
import pandas 
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'Arial'
LANGAGE_1 = "espagnol"
LANGAGE_2 = "francais"
rand_word_dict = ""

# DATAS
try:
    dataframe = pandas.read_csv("30-flash-card-app/data/words_es_to_learn.csv")
except FileNotFoundError:
    dataframe = pandas.read_csv("30-flash-card-app/data/traductions_es_fr.csv")

data_list = dataframe.to_dict(orient="records")

    

# ---------------------------- REMOVE WORD FROM THE LIST ------------------------------- #


def create_dataframe_words_to_learn():
    data_list.remove(rand_word_dict)
    new_dataframe = pandas.DataFrame(data_list)
    new_dataframe.to_csv("30-flash-card-app/data/words_es_to_learn.csv", index=False)

def update_list_words_to_learn():
    create_dataframe_words_to_learn()
    generate_rand_word()

# ---------------------------- FLIP CARD ------------------------------- #

def flip_card():
    # Pick the word translated
    word_translated = rand_word_dict[LANGAGE_2]
    # Change the UI setup
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(canvas_text_langage, text=LANGAGE_2, fill="white")
    canvas.itemconfig(canvas_text_word, text=word_translated, fill="white")
    window.after_cancel(1000)

# ---------------------------- GENERATE RANDOM WORD ------------------------------- #


def generate_rand_word():
    global rand_word_dict
    # Pick random word
    rand_word_dict = choice(data_list)
    rand_es_word = rand_word_dict[LANGAGE_1]
    # Change the UI setup
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(canvas_text_langage, text=LANGAGE_1, fill="black")
    canvas.itemconfig(canvas_text_word, text=rand_es_word, fill="black")
    # Wait 3sec to reveal the translation
    window.after(3000, flip_card)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Cards ES FR")
window.minsize(width=900, height=570)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flash cards
canvas = Canvas(width=800, height=600,bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="30-flash-card-app/images/card_front.png")
card_back_img = PhotoImage(file="30-flash-card-app/images/card_back.png")
canvas_image = canvas.create_image(400, 290, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

# Canva text
canvas_text_langage = canvas.create_text(400, 190, text=LANGAGE_1, font=(FONT_NAME, 40, "italic"), fill="black")
canvas_text_word = canvas.create_text(400, 303, text="", font=(FONT_NAME, 60, "bold"), fill="black")
# Generate a first random word
generate_rand_word()

# Buttons
button_right_img = PhotoImage(file="30-flash-card-app/images/right.png")
button_right = Button(image=button_right_img, highlightthickness=0, command=update_list_words_to_learn)
button_right.grid(column=1, row=1)
button_wrong_img = PhotoImage(file="30-flash-card-app/images/wrong.png")
button_wrong = Button(image=button_wrong_img, highlightthickness=0, command=generate_rand_word)
button_wrong.grid(column=0, row=1)

# Keep the window on screen
window.mainloop()
