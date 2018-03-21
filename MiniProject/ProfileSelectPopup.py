import tkinter as tk

class ProfileSelectPopup:
    def __init__(self,master,list):
        self.toplevel = tk.Toplevel(master)#create window
        self.choice = None #variable to hold choice

        #set window title
        self.toplevel.title("Choose a Profile")

        #convert list to StringVar list
        self.stringVars = tk.StringVar(value=list)

        #add label to window
        self.promptlabel = tk.Label(self.toplevel,text="Choose a Profile")
        self.promptlabel.pack()
        
        #create listbox and add to window
        self.listbox = tk.Listbox(self.toplevel, listvariable=self.stringVars,selectmode="single")
        self.listbox.pack()

        #create confirm button and add to window
        self.confirm = tk.Button(self.toplevel, text="Select",command=self.toplevel.destroy)
        self.confirm.pack()

        #add event binding to trigger callback
        self.listbox.bind("<<ListboxSelect>>",self.getSelection)

    #function called by bound event
    def getSelection(self, event):
        widget = event.widget
        selection = widget.curselection()#get index of current selection
        self.choice = widget.get(selection[0])#get value of index selected