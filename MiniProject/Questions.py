
#file imports
import tkinter as tk

from fractions import gcd
import math
import random

#Abstract Class for question box
class QuestionBox:
    def __init__(self,master):
        self.correctvalue = 0 #change these values in specializations
        self.wrongvalue = 0


        self.master = master#save master frame
        self.questionFrame = tk.Frame(self.master,bg=self.master['bg'])

    def destroy(self):
        self.questionFrame.destroy()
        

    #Create Visual Elements related to question
    def createQuestion(self):
        #overload this in a specialization to create question types
        SystemExit()
        return

    def getAnswer(self):
        #overload in derived class for logic related to checking answer validity
        SystemExit()
        return

#derived class from question box for specific question category

#######################
####  Questions    ####
#######################
class GCDivisorQuestion(QuestionBox):
    def __init__(self,master):
        QuestionBox.__init__(self,master)
        self.correctvalue = 50#set values for base class variables
        self.wrongvalue = 5

    def createQuestion(self):#overload of base class create question method
        self.questionFrame.pack(expand="True")

        self.x = random.randint(1,100)
        self.y = random.randint(1,100)

        self.answer = gcd(self.x,self.y)

        #create stringVar to hold question
        self.questionString = tk.StringVar()
        self.questionString.set("Question: What is the Greatest common divisor of "+str(self.x)+" and "+str(self.y)+"?")
        

        #Create Question Label
        self.questionLabel = tk.Label(self.questionFrame,textvariable=self.questionString,bg=self.master['bg'])
        self.questionLabel.pack(side="top")

        #create variable to hold answer entry
        self.answerEntryVar = tk.StringVar()

        #create answer entry
        self.answerentry = tk.Entry(self.questionFrame,textvariable=self.answerEntryVar)
        self.answerentry.pack(side="bottom",anchor='s')

    def getAnswer(self):
        if int(self.answerEntryVar.get()) == self.answer:
            return True
        else:
            return False

class divisionQuestion(QuestionBox):
    def __init__(self,master):
        QuestionBox.__init__(self,master)
        self.correctvalue = 10#set values for base class variables
        self.wrongvalue = 5

    def createQuestion(self):#overload of base class create question method
        self.questionFrame.pack(expand="True")

        self.x = random.randint(2,100)# number 1 is boring 
        self.y = random.randint(2,100)
        
        while ( self.x % self.y != 0): # makes sure picked numbers do perfect integer division
             self.x = random.randint(2,100)# number one is borring 
             self.y = random.randint(2,100) 

        self.answer = self.x / self.y #calculate answer
        #create stringVar to hold question
        self.questionString = tk.StringVar()
        self.questionString.set("Question: What is "+str(self.x)+" ÷ "+str(self.y)+ "?")
        

        #Create Question Label
        self.questionLabel = tk.Label(self.questionFrame,textvariable=self.questionString,bg=self.master['bg'])
        self.questionLabel.pack(side="top")

        #create variable to hold answer entry
        self.answerEntryVar = tk.StringVar()

        #create answer entry
        self.answerentry = tk.Entry(self.questionFrame,textvariable=self.answerEntryVar)
        self.answerentry.pack(side="bottom",anchor='s')

    def getAnswer(self):
        if int(self.answerEntryVar.get()) == self.answer:
            return True
        else:
            return False

class subtractQuestion(QuestionBox):
    def __init__(self,master):
        QuestionBox.__init__(self,master)
        self.correctvalue = 10#set values for base class variables
        self.wrongvalue = 5

    def createQuestion(self):#overload of base class create question method
        self.questionFrame.pack(expand="True")

        self.x = random.randint(1,1000)#create question numbers
        self.y = random.randint(1,1000)

        self.answer = self.x - self.y #calculate answer

        #create stringVar to hold question
        self.questionString = tk.StringVar()
        self.questionString.set("Question: What is "+str(self.x)+" - "+str(self.y)+ "?")
        
        #Create Question Label
        self.questionLabel = tk.Label(self.questionFrame,textvariable=self.questionString,bg=self.master['bg'])
        self.questionLabel.pack(side="top")

        #create variable to hold answer entry
        self.answerEntryVar = tk.StringVar()

        #create answer entry
        self.answerentry = tk.Entry(self.questionFrame,textvariable=self.answerEntryVar)
        self.answerentry.pack(side="bottom",anchor='s')

    def getAnswer(self):
        if int(self.answerEntryVar.get()) == self.answer:
            return True
        else:
            return False

class multiplicationQuestion(QuestionBox):
    def __init__(self,master):
        QuestionBox.__init__(self,master)
        self.correctvalue = 10#set values for base class variables
        self.wrongvalue = 5
    def createQuestion(self):#overload of base class create question method
        self.questionFrame.pack(expand="True")

        self.x = random.randint(2,20)# Most people learn up to the 12 times tables
        self.y = random.randint(2,20)

        self.answer = self.x * self.y #calculate answer

        #create stringVar to hold question
        self.questionString = tk.StringVar()
        self.questionString.set("Question: What is "+str(self.x)+" * "+str(self.y)+ "?")
        

        #Create Question Label
        self.questionLabel = tk.Label(self.questionFrame,textvariable=self.questionString,bg=self.master['bg'])
        self.questionLabel.pack(side="top")

        #create variable to hold answer entry
        self.answerEntryVar = tk.StringVar()

        #create answer entry
        self.answerentry = tk.Entry(self.questionFrame,textvariable=self.answerEntryVar)
        self.answerentry.pack(side="bottom",anchor='s')

    def getAnswer(self):
        if int(self.answerEntryVar.get()) == self.answer:
            return True
        else:
            return False

class AdditionQuestion(QuestionBox):
    def __init__(self,master):
        QuestionBox.__init__(self,master)#initialize base class

        self.correctvalue = 10#set values for base class variables
        self.wrongvalue = 5

    def createQuestion(self):#overload of base class create question method
       self.questionFrame.pack(expand="True")

       self.x = random.randint(1,1000)#create question numbers
       self.y = random.randint(1,1000)

       self.answer = self.x + self.y #calculate answer

       #create stringVar to hold question
       self.questionString = tk.StringVar()
       self.questionString.set("Question: What is "+str(self.x)+" + "+str(self.y)+ "?")

       #Create Question Label
       self.questionLabel = tk.Label(self.questionFrame,textvariable=self.questionString,bg=self.master['bg'])
       self.questionLabel.pack(side="top")

       #create variable to hold answer entry
       self.answerEntryVar = tk.StringVar()

       #create answer entry
       self.answerentry = tk.Entry(self.questionFrame,textvariable=self.answerEntryVar)
       self.answerentry.pack(side="bottom",anchor='s')

    #Question to verify answer
    def getAnswer(self):
        if int(self.answerEntryVar.get()) == self.answer:
            return True
        else:
            return False

class SolveXQuestion(QuestionBox):
    def __init__(self,master):
        QuestionBox.__init__(self,master)#initialize base class

        self.correctvalue = 50#set values for base class variables
        self.wrongvalue = 5

    def createQuestion(self):#overload of base class create question method
       self.questionFrame.pack(expand="True")

       self.x = random.randint(-10,10)#Value of x
       self.a = random.randint(-10,10)#Value of a
       self.b = random.randint(-10,10)#Value of b
       
       #calculate final variable
       self.y = self.a * self.x + self.b

       #create stringVar to hold question
       self.questionString = tk.StringVar()
       self.questionString.set("Question: Solve for x: \n"+str(self.a)+"x"+self.displaySign(self.b)+"="+str(self.y))

       #Create Question Label
       self.questionLabel = tk.Label(self.questionFrame,textvariable=self.questionString,bg=self.master['bg'])
       self.questionLabel.pack(side="top")

       #create variable to hold answer entry
       self.answerEntryVar = tk.StringVar()

       #create answer entry
       self.answerentry = tk.Entry(self.questionFrame,textvariable=self.answerEntryVar)
       self.answerentry.pack(side="bottom",anchor='s')

    #Question to verify answer
    def getAnswer(self):
        if int(self.answerEntryVar.get()) == self.x:
            return True
        else:
            return False

    #function to convert positive or negative number to show its sign
    def displaySign(self,num):
        if num > -1:
            return "+"+str(num)
        else:
            return str(num)