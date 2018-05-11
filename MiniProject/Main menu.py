from tkinter import *

window = Tk()

window.title("Kid game")

window.geometry('350x500')

lbl = Label(window, text="Select a Game")

lbl.grid(column=0, row=0)


def clicked():
    lbl.configure(text="Button was clicked !!")


if btn = Button(window, text="Space trivia", command=clicked)
    else btn = Button(window, text= "math", command=clicked)

btn.grid(column=3, row=4)

window.mainloop()