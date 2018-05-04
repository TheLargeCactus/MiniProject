import tkinter as tk
#import sys


class QuestionDisplayer(tk.Frame):
    def __init__(self, parent, prompt, qNum, p0, p1, p2, p3):
        tk.Frame.__init__(self, parent)

        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.parent = parent
        self.adder = 0;
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.prompt = tk.Label(self, text="Question " + (str (qNum)) + "/10:\n\n" + prompt, font = 15)
        self.submit0 = tk.Button(self, text=p0, command = self.click0, height = 2, width = 50)
        self.submit1 = tk.Button(self, text=p1, command=self.click1, height = 2, width = 50)
        self.submit2 = tk.Button(self, text=p2, command=self.click2, height = 2, width = 50)
        self.submit3 = tk.Button(self, text=p3, command=self.click3, height = 2, width = 50)

        self.title = tk.Label(self, text="Space Adventure", font = 30)

        # lay the widgets out on the screen.
        self.title.pack(side="top", pady = 10)
        self.prompt.pack(side="top", pady = 10)
        self.submit0.pack(side="top", pady=10)
        self.submit1.pack(side="top", pady=10)
        self.submit2.pack(side="top", pady=10)
        self.submit3.pack(side="top", pady=10)

    def click0(self):
        self.adder = 1
        #sys.exit()
        self.parent.destroy()
    def click1(self):
        self.adder = 2
        #sys.exit()
        self.parent.destroy()
    def click2(self):
        self.adder = 3
        #sys.exit()
        self.parent.destroy()
    def click3(self):
        self.adder = 4
        #sys.exit()
        self.parent.destroy()
    def whichAnswer(self):
        return self.adder
