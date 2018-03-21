#import graphics library
import tkinter as tk 
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Toplevel
from tkinter import font
from fractions import gcd

#import other python libraries
import math
import sqlite3
import os
import random
import time

#import other class files
from Timer import *
from ProfileSelectPopup import *
from CreateProfilePopup import *
from Questions import *

#python version should be Python 3

class Application:
    def __init__(self):
        self.root = tk.Tk()#object used to create window
        
        #Profile variables
        self.profileName = ""
        self.profileNameVar = tk.StringVar()
        self.profileNameVar.set("Profile: "+self.profileName) #profile Name
        self.profileAge = 0   #Age of profile user
        self.profileScore = 0 #Profile Score
        self.db = sqlite3.connect("./Profiles/profiles.db") #database object, stored relative to currentdirectory/Profiles/profile.db
        self.cursor = self.db.cursor()
        self.profileLoaded = False

        self.profileAgeVar = tk.StringVar()#variables to hold profileAge and profileScore
        self.profileScoreVar = tk.StringVar()
        self.profileAgeVar.set("Age: ")
        self.profileScoreVar.set("Score: ")

        #question container variable
        self.question = None


        self.createGUI()#function defined in this class to create GUI elements

        self.root.protocol('WM_DELETE_WINDOW', self.end)#Add protocol to call closing function on exit

        #Must be last statement in __init__
        self.root.mainloop()#starts the main loop of the GUI

    def createGUI(self):

        #set window options
        self.root.title("MentalMath | Jose Gonzalez | Stephen Wratten") #set window title
        self.root.minsize(width=500,height=500) #set minimum window size

        #create menubar section
        self.menuBar = tk.Menu(self.root,bg='#355C7D')#create menu bar object

        self.fileMenu = tk.Menu(self.menuBar,tearoff=0) #create submenu by using menuBar as master
        self.fileMenu.add_command(label="Create New Profile", command=self.createProfile) #add create profile command to submenu
        self.fileMenu.add_command(label="Delete Profile",command=self.deleteProfile) #Add delete profile command to submenu
        self.fileMenu.add_separator() #Add command Separator
        self.fileMenu.add_command(label="Save Profile", command=self.saveProfile) #add save profile command to submenu
        self.fileMenu.add_command(label="Load Profile", command=self.loadProfile)#Add load profile command to menu
        self.fileMenu.add_separator() #add seperator line in submenu
        self.fileMenu.add_command(label="Quit", command=self.root.quit) #add quit command to submenu
        self.menuBar.add_cascade(label="File", menu=self.fileMenu) #place submenu with title File on menubar


        self.root.config(menu=self.menuBar) #update menu on root window

        #create sidebar section
        self.sidebar = tk.Frame(self.root, bg='#6C5B7B', height=500)
        self.sidebar.pack(expand=False,fill='both', side='left', anchor='w')

        #Add Profile name to sidebar
        self.sidebarProfileLabel = tk.Label(self.sidebar,textvariable=self.profileNameVar,bg=self.sidebar['bg'])
        self.sidebarProfileLabel.pack(side="top",fill='both',anchor='w')

        #Add profile age to sidebar
        self.sidebarAgeLabel = tk.Label(self.sidebar,textvariable=self.profileAgeVar,bg=self.sidebar['bg'])
        self.sidebarAgeLabel.pack(side="top",anchor='w')

        #create main area for question section
        self.mainarea = tk.Frame(self.root, width=350, bg='#F8B195', height=470)
        self.mainarea.pack(expand=True, fill='both', side='top',anchor='e')

        #create bottom bar section
        self.bottombar = tk.Frame(self.root, width=500, bg='#C06C84', height=50)
        self.bottombar.pack(expand=False, fill='both', side='bottom',anchor='w')

        #create subframe to hold some visual elements
        self.bottombarsubframe = tk.Frame(self.bottombar,bg=self.bottombar['bg'])
        self.bottombarsubframe.pack(side='left')

        #Add profile score to bottom bar
        self.sidebarScoreLabel = tk.Label(self.bottombarsubframe,textvariable=self.profileScoreVar,bg=self.bottombar['bg'],font=(tk.font.nametofont("TkDefaultFont"), 16))
        self.sidebarScoreLabel.pack(side="bottom",anchor='sw')

        #Create Timer
        self.timer = Timer(self.bottombarsubframe, self.root,bg=self.bottombarsubframe['bg'],font=(tk.font.nametofont("TkDefaultFont"), 16))
        self.timer.timeLabel.pack(side='top',anchor='nw')

        #Create Next Question Button
        self.nextquestionbutton = tk.Button(self.bottombar,text='Next Question',command=self.nextQuestion,state='disabled')
        self.nextquestionbutton.pack(side="right",anchor='w')

        #Create Submit Question Button
        self.submitquestionbutton = tk.Button(self.bottombar,text='Submit Question',command=self.submitQuestion,state='disabled')
        self.submitquestionbutton.pack(side="right")

        #turn off resizing for certain frames
        self.bottombar.pack_propagate(0)

        return

    #function prompts a user to create a profile, giving an error if the profile exists
    def createProfile(self):
        popup = CreateProfilePopup(master=self)#prompt user to enter input
        self.root.wait_window(popup.top) #wait for input to be entered
        
        profName = popup.nameVar.get()#get values from popup instance
        profAge = popup.ageVar.get()

        if profName == "":
            tk.messagebox.showerror("Entry Error","Invalid Entry Given")
            return

        #check if name exists in database
        self.cursor.execute("Select * from Profile where profileName = '"+profName+"'")

        entries = self.cursor.fetchall()

        #if entries has a size > 0 we know that a tuple existed in the database, and therefore the name is taken
        if len(entries) > 0:
            tk.messagebox.showerror("Profile Error","Profile already exists")
        else:
            self.cursor.execute("Insert Into Profile values ('"+profName+"', '"+profAge+"','0')") #insert new tuple into table
            self.db.commit()#save data to database file

            self.loadProfile(profName)#after creating profile, load it
        return 

    #function for loading profiles
    def loadProfile(self, name=None):
        #if no name passed to function, prompt user for name
        if name==None:
            self.cursor.execute("SELECT profileName from Profile")#retrieve data from database

            entries=self.cursor.fetchall()#parse profilenames as seperate entries

            #check is entries has a size > 0, if not display an error and return
            if len(entries) == 0:
                tk.messagebox.showerror("Load Error", "Cannot load Profile! No profiles exist!")
                return

            #create subwindow to hold listview
            pickwindow = ProfileSelectPopup(self.root, entries)

            #wait for user to pick an item
            self.root.wait_window(pickwindow.toplevel)

            #check if pickwindow choice has a length
            if pickwindow.choice is None:
                tk.messagebox.showerror("Choice Error","No Choice Given")
                return

            #get value from prompt object
            name = pickwindow.choice[0]

        #get database data and assign it to variables
        self.cursor.execute("SELECT profileName, profileAge, profileScore from Profile Where profileName = '"+name+"'")

        temp = self.cursor.fetchone() #add results to a temp variable

        #if profile is already loaded, then save profile before loading new values
        if self.profileLoaded:
            self.saveProfile()

        self.profileName = temp[0]
        self.profileNameVar.set("Profile: "+ self.profileName) #set variables
        self.profileAge = int(temp[1])
        self.profileScore = int(temp[2])
        self.profileLoaded = True
        self.profileAgeVar.set("Age: "+str(self.profileAge))
        self.profileScoreVar.set("Score: "+str(self.profileScore))

        self.nextquestionbutton['state'] = 'normal'#Allow pressing of next question button

        return

    #function to save currently loaded profile
    def saveProfile(self):
        if not self.profileLoaded:#if no profile is loaded, do nothing 
            return

        #save score to database table
        self.cursor.execute("UPDATE Profile SET profileScore = "+str(self.profileScore)+" Where profileName = '"+self.profileName+"'")

        self.db.commit()#commit data to database
        self.nextquestionbutton['state'] = 'disabled'#Disable next question button when no profile is loaded

        return

    #function to delete profile
    def deleteProfile(self):

        self.cursor.execute("SELECT profileName from Profile")#retrieve data from database

        entries=self.cursor.fetchall()#parse profilenames as seperate entries

        #create subwindow to hold listview
        pickwindow = ProfileSelectPopup(self.root, entries)

        #wait for user to pick an item
        self.root.wait_window(pickwindow.toplevel)

        #check if pickwindow choice has a length
        if pickwindow.choice is None:
            tk.messagebox.showerror("Choice Error","No Choice Given")
            return

        #check if pickwindow choice has a length
        if len(pickwindow.choice) < 1:
            tk.messagebox.showerror("Choice Error","No Choice Given")

        #get value from pickwindow
        name = pickwindow.choice[0]

        #Check if profile exists
        self.cursor.execute("Select profileName from Profile Where profileName='"+name+"'")

        #check if results are found, if they dont, give an error
        if len(self.cursor.fetchall()) < 1:
            tk.messagebox.showerror("Profile Error","Profile does not exist")
            return

        #if profile selected for delete is loaded, display an error
        if self.profileName == name:
            tk.messagebox.showerror("Selection Error","Cannot delete the currently open profile. Close the profile before deleting.")
            return

        #if it exists, delete it
        self.cursor.execute("Delete From Profile Where profileName ='"+name+"'")

    #function updates GUI with next question data
    
    #######################
    #### Next Question ####
    #######################

    def nextQuestion(self):
        #disable question button so question is not-skipable
        self.nextquestionbutton['state'] = 'disabled'

        #enable submit button
        self.submitquestionbutton['state'] = 'normal'

        self.question = random.choice([GCDivisorQuestion(self.mainarea),
                                       divisionQuestion(self.mainarea),
                                       AdditionQuestion(self.mainarea),
                                       subtractQuestion(self.mainarea),
                                       multiplicationQuestion(self.mainarea),
                                       SolveXQuestion(self.mainarea)])#set question to random choice from question Category list

        self.question.createQuestion()#Place Question on screen

        self.timer.resetClock()#start clock
        self.timer.restartClock()
        return

    #function called after question is submitted
    def submitQuestion(self):
        #Stop the timer
        self.timer.stopClock()
        
        #if question is answered correctly, add point value to score, else sub incorrect value from score
        if self.question.getAnswer():
            self.profileScore += self.question.correctvalue
        else:
            self.profileScore += self.question.wrongvalue # add 5 for trying 

        #enable next question button
        self.nextquestionbutton['state'] = 'normal'
        
        #disable submit button
        self.submitquestionbutton['state'] = 'disabled'

        #destroy question
        self.question.questionFrame.destroy()

        #update profile score variable
        self.profileScoreVar.set("Score: " +str(self.profileScore))
        return

    #End Application
    def end(self):
        self.saveProfile()
        self.root.destroy()

app = Application() #start application



