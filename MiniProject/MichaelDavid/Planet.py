import tkinter as tk
import random
import sys

from QuestionDisplayer import QuestionDisplayer
from CorrectDisplay import CorrectDisplay
from WrongDisplay import WrongDisplay
from EndLevelScreen import EndLevelScreen
from Question import Question

class Planet:
    def __init__(self, q0, q1, q2, q3, q4, q5, q6, q7, q8, q9):
        self.questions = (q0, q1, q2, q3, q4, q5, q6, q7, q8, q9)
        self.correct = 0
    def displayAllQuestions(self, cPlanet, nPlanet):
        x = 0
        while x <= 9:
            self.displayQuestion(x)
            x += 1
            if x == 10:
                root = tk.Tk()
                root.geometry("2000x800")
                eDisplay = EndLevelScreen(root, cPlanet, nPlanet, self.correct)
                eDisplay.pack(fill="both", expand=True)
                root.mainloop()
                y = eDisplay.whichAnswer()
                print(y)
                if y == 0:
                    x = 0
                elif y == -1:
                    sys.exit()

    def displayQuestion(self, indexVal):
        # Will display the prompt of the question of the selected index
        root = tk.Tk()
        root.geometry("2000x800")
        a = [self.questions[indexVal].getInc0(), self.questions[indexVal].getInc1(), self.questions[indexVal].getInc2(), self.questions[indexVal].getAnswer()]
        y = [self.questions[indexVal].getInc0(), self.questions[indexVal].getInc1(), self.questions[indexVal].getInc2(), self.questions[indexVal].getAnswer()]
        correct = 0
        random.shuffle(a)
        if a[0] == y[3]:
            correct = 0
        if a[1] == y[3]:
            correct = 1
        if a[2] == y[3]:
            correct = 2
            print("C is 2")
        if a[3] == y[3]:
            correct = 3
        qDisplay = QuestionDisplayer(root, self.questions[indexVal].getPrompt(), (indexVal + 1), a[0], a[1], a[2], a[3])
        qDisplay.pack(fill="both", expand=True)
        root.mainloop()
        if qDisplay.whichAnswer() == 0:
            sys.exit()
        if (qDisplay.whichAnswer() - 1) == correct:
            self.correct += 1
            if(indexVal < 9):
                root = tk.Tk()
                root.geometry("2000x800")
                cDisplay = CorrectDisplay(root, self.questions[indexVal].getPrompt(), self.questions[indexVal].getAnswer())
                cDisplay.pack(fill="both", expand=True)
                root.mainloop()
        else:
            if(indexVal < 9):
                root = tk.Tk()
                root.geometry("2000x800")
                wDisplay = WrongDisplay(root, self.questions[indexVal].getPrompt(), self.questions[indexVal].getAnswer())
                wDisplay.pack(fill="both", expand=True)
                root.mainloop()
        #print(val)
        # Will randomize the order of the correct answer and incorrect answer (Will have a variable that holds the slot index the right answer is put in)
        # Will display buttons and wait
        # Checks if correct button was pressed
