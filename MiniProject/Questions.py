
#file imports
import tkinter as tk
from fractions import Fraction
from fractions import gcd
import math
import random
from enum import Enum,auto

#Import Planet Trivia
from Trivia import *

#create type enumeration
class Type(Enum):
    Math = auto()
    Science = auto()
    Libs = auto()

#Abstract Class for question box
class QuestionBox:
    def __init__(self,master):
        self.correctvalue = 0 #change these values in specializations
        self.wrongvalue = 0
        self.master = master#save master frame
        self.questionFrame = tk.Frame(self.master,bg=self.master['bg'])

        self.correctLabel = tk.Label(self.questionFrame,bg=self.master['bg'],font=(tk.font.nametofont("TkDefaultFont"), 16),text='')
        self.correctLabel.pack(side='bottom')

    #function to cleanup question
    def destroy(self):
        self.questionFrame.destroy()

    #function to display correct or incorrect answer
    def displayCorrect(self):
        if self.getAnswer():
            self.correctLabel.configure(fg="Green",text='Correct! +'+str(self.correctvalue))
        else:
            self.correctLabel.configure(fg="Red",text='Incorrect! -'+str(self.wrongvalue))
        
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
class exponentQuestion(QuestionBox):
    def __init__(self,master):
        QuestionBox.__init__(self,master)
        self.correctvalue = 50 #set values for base class variables
        self.wrongvalue = 5

    def createQuestion(self):#overload of base class create question method
        self.questionFrame.pack(expand="True")

        self.x = random.randint(2,10)# 
        self.y = random.randint(2,10)# 

        self.answer = self.x ** self.y  #calculate answer

        #create stringVar to hold question
        self.questionString = tk.StringVar()

        if (self.y == 2):
            self.questionString.set("Question: What is "+str(self.x)+" squared? ")
        elif(self.y==3):
            self.questionString.set("Question: What is "+str(self.x)+" cubed? ")
        else:
             self.questionString.set("Question: What is "+str(self.x)+" to the "+str(self.y)+ "th power?")
        
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

class fractionDivision(QuestionBox):
    def __init__(self,master):
        QuestionBox.__init__(self,master)
        self.correctvalue = 40#set values for base class variables
        self.wrongvalue = 3

    def createQuestion(self):#overload of base class create question method
        self.questionFrame.pack(expand="True")

        self.n = random.randint(1,10)
        self.d = random.randint(1,20)

        self.n1= random.randint(1,10)
        self.d1= random.randint(1,20)

        temp = Fraction(self.n,self.d) / Fraction(self.n1,self.d1)

        self.answer = str(temp)# temp is converted to string and loaded to answer 

        #create stringVar to hold question
        self.questionString = tk.StringVar()

        self.questionString.set("Divide and reduce. What is "+str(self.n)+"/"+str(self.d) +" ÷ " + str(self.n1)+"/"+str(self.d1)+" ?")
        
        #Create Question Label
        self.questionLabel = tk.Label(self.questionFrame,textvariable=self.questionString,bg=self.master['bg'])
        self.questionLabel.pack(side="top")

        #create variable to hold answer entry
        self.answerEntryVar = tk.StringVar()

        #create answer entry
        self.answerentry = tk.Entry(self.questionFrame,textvariable=self.answerEntryVar)
        self.answerentry.pack(side="bottom",anchor='s')

    def getAnswer(self):
        if str(self.answerEntryVar.get()) == self.answer:
            return True
        else:
            return False

class fractionMultiplication(QuestionBox):
    def __init__(self,master):
        QuestionBox.__init__(self,master)
        self.correctvalue = 40#set values for base class variables
        self.wrongvalue = 3

    def createQuestion(self):#overload of base class create question method
        self.questionFrame.pack(expand="True")

        self.n = random.randint(1,10)
        self.d = random.randint(1,20)

        self.n1= random.randint(1,10)
        self.d1= random.randint(1,20)

        temp = Fraction(self.n,self.d) * Fraction(self.n1,self.d1)

        self.answer = str(temp)# temp is converted to string and loaded to answer 

        #create stringVar to hold question
        self.questionString = tk.StringVar()

        self.questionString.set("Multiply and reduce. What is "+str(self.n)+"/"+str(self.d) +" * " + str(self.n1)+"/"+str(self.d1)+" ?")
        
        #Create Question Label
        self.questionLabel = tk.Label(self.questionFrame,textvariable=self.questionString,bg=self.master['bg'])
        self.questionLabel.pack(side="top")

        #create variable to hold answer entry
        self.answerEntryVar = tk.StringVar()

        #create answer entry
        self.answerentry = tk.Entry(self.questionFrame,textvariable=self.answerEntryVar)
        self.answerentry.pack(side="bottom",anchor='s')

    def getAnswer(self):
        if str(self.answerEntryVar.get()) == self.answer:
            return True
        else:
            return False

class fractionSubtraction(QuestionBox):
    def __init__(self,master):
        QuestionBox.__init__(self,master)
        self.correctvalue = 40#set values for base class variables
        self.wrongvalue = 3

    def createQuestion(self):#overload of base class create question method
        self.questionFrame.pack(expand="True")

        self.n = random.randint(1,10)
        self.d = random.randint(1,20)

        self.n1= random.randint(1,10)
        self.d1= random.randint(1,20)

        temp = Fraction(self.n,self.d) - Fraction(self.n1,self.d1)

        self.answer = str(temp)# temp is converted to string and loaded to answer 

        #create stringVar to hold question
        self.questionString = tk.StringVar()

        self.questionString.set("Subtract and reduce. What is "+str(self.n)+"/"+str(self.d) +" - " + str(self.n1)+"/"+str(self.d1)+" ?")
        
        #Create Question Label
        self.questionLabel = tk.Label(self.questionFrame,textvariable=self.questionString,bg=self.master['bg'])
        self.questionLabel.pack(side="top")

        #create variable to hold answer entry
        self.answerEntryVar = tk.StringVar()

        #create answer entry
        self.answerentry = tk.Entry(self.questionFrame,textvariable=self.answerEntryVar)
        self.answerentry.pack(side="bottom",anchor='s')

    def getAnswer(self):
        if str(self.answerEntryVar.get()) == self.answer:
            return True
        else:
            return False

class fractionAddition(QuestionBox):
    def __init__(self,master):
        QuestionBox.__init__(self,master)
        self.correctvalue = 40#set values for base class variables
        self.wrongvalue = 3

    def createQuestion(self):#overload of base class create question method
        self.questionFrame.pack(expand="True")

        self.n = random.randint(1,10)
        self.d = random.randint(1,20)

        self.n1= random.randint(1,10)
        self.d1= random.randint(1,20)

        temp = Fraction(self.n,self.d) + Fraction(self.n1,self.d1)

        self.answer = str(temp)# temp is converted to string and loaded to answer 

        #create stringVar to hold question
        self.questionString = tk.StringVar()

        self.questionString.set("Add up and reduce. What is "+str(self.n)+"/"+str(self.d) +" + " + str(self.n1)+"/"+str(self.d1)+" ?")
        
        #Create Question Label
        self.questionLabel = tk.Label(self.questionFrame,textvariable=self.questionString,bg=self.master['bg'])
        self.questionLabel.pack(side="top")

        #create variable to hold answer entry
        self.answerEntryVar = tk.StringVar()

        #create answer entry
        self.answerentry = tk.Entry(self.questionFrame,textvariable=self.answerEntryVar)
        self.answerentry.pack(side="bottom",anchor='s')

    def getAnswer(self):
        if str(self.answerEntryVar.get()) == self.answer:
            return True
        else:
            return False

class fractionReduce(QuestionBox):
    def __init__(self,master):
        QuestionBox.__init__(self,master)
        self.correctvalue = 30#set values for base class variables
        self.wrongvalue = 3

    def createQuestion(self):#overload of base class create question method
        self.questionFrame.pack(expand="True")

        self.n = random.randint(1,100)# numerator variable
        self.d = random.randint(1,10)*random.randint(2,10)# denominator variable

        temp = Fraction(self.n,self.d) # temp holds the reduced fraction as a number variable

        self.answer = str(temp)# temp is converted to string and loaded to answer 

        #create stringVar to hold question
        self.questionString = tk.StringVar()

        self.questionString.set("Reduce the fraction "+str(self.n)+"/"+str(self.d))
        
        #Create Question Label
        self.questionLabel = tk.Label(self.questionFrame,textvariable=self.questionString,bg=self.master['bg'])
        self.questionLabel.pack(side="top")

        #create variable to hold answer entry
        self.answerEntryVar = tk.StringVar()

        #create answer entry
        self.answerentry = tk.Entry(self.questionFrame,textvariable=self.answerEntryVar)
        self.answerentry.pack(side="bottom",anchor='s')

    def getAnswer(self):
        if str(self.answerEntryVar.get()) == self.answer:
            return True
        else:
            return False

class rootQuestion(QuestionBox):
    def __init__(self,master):
        QuestionBox.__init__(self,master)
        self.correctvalue = 50 #set values for base class variables
        self.wrongvalue = 5

    def createQuestion(self):#overload of base class create question method
        self.questionFrame.pack(expand="True")

        self.x = random.randint(2,5)# random root, will do up to 5th roots
        self.y = random.randint(2,4)# up to 4, makes sure number is not too big

        self.y= self.y**self.x #creates answer -> makes sure the number has a whole root

        self.answer = self.y ** (1/self.x) #calculate answer

        #create stringVar to hold question
        self.questionString = tk.StringVar()

        if (self.x == 2):
            self.questionString.set("Question: What is the square root of "+str(self.y)+ "?")
        elif(self.x==3):
            self.questionString.set("Question: What is the cube root of "+str(self.y)+ "?")
        else:
             self.questionString.set("Question: What is the "+str(self.x)+"th root of "+str(self.y)+ "?")
        
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
        self.wrongvalue = 2

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
        self.wrongvalue = 2

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
        self.wrongvalue = 2
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
        self.wrongvalue = 2

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

       sign = [-1,1]

       self.x = random.randint(1,10) * random.choice(sign)#
       self.a = random.randint(1,10) * random.choice(sign)#Value of a
       self.b = random.randint(1,10) * random.choice(sign)#Value of b
       
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


class MercuryQuestion(QuestionBox):
    def __init__(self,master):
        QuestionBox.__init__(self,master)#initialize base class

        self.correctvalue = 20#set values for base class variables
        self.wrongvalue = 10 #wrong value needs to be greater than correctvalue * 1/4 as there are only 4 possible answers

    def createQuestion(self):#overload of base class create question method
       self.questionFrame.pack(expand="True")
       

       #Get Random Mercury Question
       self.planetQuestion = random.choice(mercury.questions)
       

       #answer is available in self.planetQuestion.answer

       #Prompt Question
       self.questionString = tk.StringVar()
       self.questionString.set(self.planetQuestion.prompt)
       self.questionLabel = tk.Label(self.questionFrame,textvariable=self.questionString,bg=self.master['bg'])
       self.questionLabel.pack(side="top")

       #create list of possible answers
       self.possibleAnswers = [self.planetQuestion.incorrect0,self.planetQuestion.incorrect1,self.planetQuestion.incorrect2,self.planetQuestion.answer] 

       #variable to hold currently selected radio button answer
       self.radioButtonAnswer = tk.StringVar()

       #mini frame to left justify 

       #create radio buttons with possible answers
       index = 0
       self.answerRadioButton = {}
       while len(self.possibleAnswers):
           #use temp variable to store one of random answers
           temp = random.choice(self.possibleAnswers)

           #create radio button for chosen answer
           self.answerRadioButton[index] = tk.Radiobutton(self.questionFrame,text=temp,value=temp,variable=self.radioButtonAnswer,bg=self.questionFrame['bg'],activebackground=self.questionFrame['bg'])
           self.answerRadioButton[index].pack(side="top",anchor='w')
           index += 1

           #remove value from list so it cant be randomly picked again
           self.possibleAnswers = [a for a in self.possibleAnswers if a != temp]

       #Set selected answer to first option
       self.radioButtonAnswer.set(self.answerRadioButton[0]['text'])

    #Question to verify answer
    def getAnswer(self):
        if self.radioButtonAnswer.get() == self.planetQuestion.answer:
            return True
        else:
            return False

class VenusQuestion(QuestionBox):
    def __init__(self,master):
        QuestionBox.__init__(self,master)#initialize base class

        self.correctvalue = 20#set values for base class variables
        self.wrongvalue = 10 #wrong value needs to be greater than correctvalue * 1/4 as there are only 4 possible answers

    def createQuestion(self):#overload of base class create question method
       self.questionFrame.pack(expand="True")
       

       #Get Random Venus Question
       self.planetQuestion = random.choice(venus.questions)
       

       #answer is available in self.planetQuestion.answer

       #Prompt Question
       self.questionString = tk.StringVar()
       self.questionString.set(self.planetQuestion.prompt)
       self.questionLabel = tk.Label(self.questionFrame,textvariable=self.questionString,bg=self.master['bg'])
       self.questionLabel.pack(side="top")

       #create list of possible answers
       self.possibleAnswers = [self.planetQuestion.incorrect0,self.planetQuestion.incorrect1,self.planetQuestion.incorrect2,self.planetQuestion.answer] 

       #variable to hold currently selected radio button answer
       self.radioButtonAnswer = tk.StringVar()

       #mini frame to left justify 

       #create radio buttons with possible answers
       index = 0
       self.answerRadioButton = {}
       while len(self.possibleAnswers):
           #use temp variable to store one of random answers
           temp = random.choice(self.possibleAnswers)

           #create radio button for chosen answer
           self.answerRadioButton[index] = tk.Radiobutton(self.questionFrame,text=temp,value=temp,variable=self.radioButtonAnswer,bg=self.questionFrame['bg'],activebackground=self.questionFrame['bg'])
           self.answerRadioButton[index].pack(side="top",anchor='w')
           index += 1

           #remove value from list so it cant be randomly picked again
           self.possibleAnswers = [a for a in self.possibleAnswers if a != temp]

       #Set selected answer to first option
       self.radioButtonAnswer.set(self.answerRadioButton[0]['text'])

    #Question to verify answer
    def getAnswer(self):
        if self.radioButtonAnswer.get() == self.planetQuestion.answer:
            return True
        else:
            return False

class EarthQuestion(QuestionBox):
    def __init__(self,master):
        QuestionBox.__init__(self,master)#initialize base class

        self.correctvalue = 20#set values for base class variables
        self.wrongvalue = 10 #wrong value needs to be greater than correctvalue * 1/4 as there are only 4 possible answers

    def createQuestion(self):#overload of base class create question method
       self.questionFrame.pack(expand="True")
       

       #Get Random Earth Question
       self.planetQuestion = random.choice(earth.questions)
       

       #answer is available in self.planetQuestion.answer

       #Prompt Question
       self.questionString = tk.StringVar()
       self.questionString.set(self.planetQuestion.prompt)
       self.questionLabel = tk.Label(self.questionFrame,textvariable=self.questionString,bg=self.master['bg'])
       self.questionLabel.pack(side="top")

       #create list of possible answers
       self.possibleAnswers = [self.planetQuestion.incorrect0,self.planetQuestion.incorrect1,self.planetQuestion.incorrect2,self.planetQuestion.answer] 

       #variable to hold currently selected radio button answer
       self.radioButtonAnswer = tk.StringVar()

       #mini frame to left justify 

       #create radio buttons with possible answers
       index = 0
       self.answerRadioButton = {}
       while len(self.possibleAnswers):
           #use temp variable to store one of random answers
           temp = random.choice(self.possibleAnswers)

           #create radio button for chosen answer
           self.answerRadioButton[index] = tk.Radiobutton(self.questionFrame,text=temp,value=temp,variable=self.radioButtonAnswer,bg=self.questionFrame['bg'],activebackground=self.questionFrame['bg'])
           self.answerRadioButton[index].pack(side="top",anchor='w')
           index += 1

           #remove value from list so it cant be randomly picked again
           self.possibleAnswers = [a for a in self.possibleAnswers if a != temp]

       #Set selected answer to first option
       self.radioButtonAnswer.set(self.answerRadioButton[0]['text'])

    #Question to verify answer
    def getAnswer(self):
        if self.radioButtonAnswer.get() == self.planetQuestion.answer:
            return True
        else:
            return False

class MarsQuestion(QuestionBox):
    def __init__(self,master):
        QuestionBox.__init__(self,master)#initialize base class

        self.correctvalue = 20#set values for base class variables
        self.wrongvalue = 10 #wrong value needs to be greater than correctvalue * 1/4 as there are only 4 possible answers

    def createQuestion(self):#overload of base class create question method
       self.questionFrame.pack(expand="True")
       

       #Get Random Mars Question
       self.planetQuestion = random.choice(mars.questions)
       

       #answer is available in self.planetQuestion.answer

       #Prompt Question
       self.questionString = tk.StringVar()
       self.questionString.set(self.planetQuestion.prompt)
       self.questionLabel = tk.Label(self.questionFrame,textvariable=self.questionString,bg=self.master['bg'])
       self.questionLabel.pack(side="top")

       #create list of possible answers
       self.possibleAnswers = [self.planetQuestion.incorrect0,self.planetQuestion.incorrect1,self.planetQuestion.incorrect2,self.planetQuestion.answer] 

       #variable to hold currently selected radio button answer
       self.radioButtonAnswer = tk.StringVar()

       #mini frame to left justify 

       #create radio buttons with possible answers
       index = 0
       self.answerRadioButton = {}
       while len(self.possibleAnswers):
           #use temp variable to store one of random answers
           temp = random.choice(self.possibleAnswers)

           #create radio button for chosen answer
           self.answerRadioButton[index] = tk.Radiobutton(self.questionFrame,text=temp,value=temp,variable=self.radioButtonAnswer,bg=self.questionFrame['bg'],activebackground=self.questionFrame['bg'])
           self.answerRadioButton[index].pack(side="top",anchor='w')
           index += 1

           #remove value from list so it cant be randomly picked again
           self.possibleAnswers = [a for a in self.possibleAnswers if a != temp]

       #Set selected answer to first option
       self.radioButtonAnswer.set(self.answerRadioButton[0]['text'])

    #Question to verify answer
    def getAnswer(self):
        if self.radioButtonAnswer.get() == self.planetQuestion.answer:
            return True
        else:
            return False