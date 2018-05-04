import tkinter as tk
#import sys


class CorrectDisplay(tk.Frame):
    def __init__(self, parent, prompt, answer):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.prompt = tk.Label(self, text="Well Done!!!\n\n" + answer + " is the correct answer", font = 15)
        self.submit0 = tk.Button(self, text="Next Question", command = self.destroyIt, height=2, width=50)

        self.title = tk.Label(self, text="Space Adventure", font = 30)

        # lay the widgets out on the screen.
        self.title.pack(side="top", fill="x", pady = 10)
        self.prompt.pack(side="top", fill="x", pady = 20)
        self.submit0.pack(side="top", pady=10)
    def destroyIt(self):
        self.parent.destroy()
