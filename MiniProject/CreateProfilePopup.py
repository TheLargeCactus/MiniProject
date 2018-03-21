#file imports
import tkinter as tk

class CreateProfilePopup:
    def __init__(self,master):
        
        self.top = tk.Toplevel(master.root)#create sub-window

        self.nameVar = tk.StringVar()
        self.ageVar = tk.StringVar()

        #Create name label and add it to box
        nameboxlabel = tk.Label(self.top,text="Enter a new profile name:")
        nameboxlabel.pack(side="top")

        #Create name text box
        nameboxtextbox = tk.Entry(self.top,textvariable=self.nameVar)
        nameboxtextbox.pack(side="top")

        #create age label
        ageboxlabel = tk.Label(self.top,text="Enter a new profile age:")
        ageboxlabel.pack(side="top")

        #create age text box
        ageboxtextbox = tk.Entry(self.top,textvariable=self.ageVar)
        ageboxtextbox.pack(side="top")

        #create a submit button
        nameboxcreatebutton = tk.Button(self.top,text="Create",command=self.top.destroy)
        nameboxcreatebutton.pack(side="top")