from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=50)

entry = Entry(width=20)
entry.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)
label2 = Label(text="is equal to")
label2.grid(column=0, row=1)
label3 = Label(text=0)
label3.grid(column=1, row=1)
label4 = Label(text="Km")
label4.grid(column=2, row=1)


def miles_to_km():
    miles = float(entry.get())
    km = miles * 1.609
    label3["text"] = km


button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)




# Keep the window on screen
window.mainloop()

