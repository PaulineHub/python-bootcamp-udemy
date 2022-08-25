from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    # reset title, timer and check marks
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # if it's the 1st/3rd/5th/7th rep:
    if reps % 2 != 0 :
        reps += 1
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec) 
    # if it's the 8th rep:
    elif reps == 8:
        reps += 1
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    # if it's the 2nd/4th/6th rep:
    elif reps < 7:
        reps += 1
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    # set the double 00
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    # start count down
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        # every 2 repetition, add another check mark
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
# fg foreground


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Tomato image (canvas)
canvas = Canvas(width=201, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="28-pomodoro-app/tomato.png")
canvas.create_image(101, 112, image=tomato_img)
timer_text = canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



# Label Timer
title_label = Label(text="Timer", fg=GREEN, font=(
    FONT_NAME, 40, "bold"), bg=YELLOW)
title_label.grid(column=1, row=0)

# Buttons start and reset
start_button = Button(text="Start", font=(FONT_NAME, 12, "bold"),
                bg="white", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 12, "bold"),
                bg="white", command=reset_timer)
reset_button.grid(column=2, row=2)

# Label Check
check_label = Label(text="", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
check_label.grid(column=1, row=3)

# Keep the window on screen
window.mainloop()
