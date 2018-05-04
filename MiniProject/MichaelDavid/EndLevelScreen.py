import tkinter as tk


class EndLevelScreen(tk.Frame):
    def __init__(self, parent, b0, b1, score):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.b0 = b0
        self.b1 = b1
        self.advance = -1
        self.prompt = tk.Label(self, text="You answered " + (str (score)) + " out of 10 questions correctly" + "\n\n\nWhould you like to advance to the next planet?", font = 15)
        self.submit0 = tk.Button(self, text= "Repeat planet " + b0, command = self.turnOff, height=2, width=50)
        self.submit1 = tk.Button(self, text= "Advance to planet " + b1, command=self.turnOn, height=2, width=50)
        self.submit2 = tk.Button(self, text= "Quit game", command = self.endGame, height=2, width=50)

        self.title = tk.Label(self, text="Space Adventure", font = 30)

        # lay the widgets out on the screen.
        self.title.pack(side="top", fill="x", pady = 10)
        self.prompt.pack(side="top", fill="x", pady = 20)
        self.submit0.pack(side="top", pady=10)
        self.submit1.pack(side="top", pady=10)
        self.submit2.pack(side="top", pady=10)

    def turnOn(self):
        self.advance = 1
        self.parent.destroy()
    def turnOff(self):
        self.advance = 0
        self.parent.destroy()
    def endGame(self):
        self.advance = -1
        self.parent.destroy()
    def whichAnswer(self):
        return self.advance


# if this is run as a program (versus being imported),
# create a root window and an instance of our example,
# then start the event loop
