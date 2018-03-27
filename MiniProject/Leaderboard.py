import tkinter as tk

#class to hold leaderboard data
class Leaderboard(tk.Toplevel):
    def __init__(self,master,list):
        tk.Toplevel.__init__(self,master)
        self.master = master #set master

        self.leaderboardnamevar = tk.StringVar(value=[row[0] for row in list])
        self.leaderboardagevar = tk.StringVar(value=[row[1] for row in list])
        self.leaderboardscorevar = tk.StringVar(value=[row[2] for row in list])

        self.leaderboardnamelist = tk.Listbox(self,listvariable=self.leaderboardnamevar)#Create list box
        self.leaderboardagelist = tk.Listbox(self,listvariable=self.leaderboardagevar)#Create list box
        self.leaderboardscorelist = tk.Listbox(self,listvariable=self.leaderboardscorevar)#Create list box

        self.leaderboardnamelist.pack(side='left')
        self.leaderboardagelist.pack(side='left')
        self.leaderboardscorelist.pack(side='left')

