#file imports
import tkinter as tk
import time


#Class to implement a timer with tkinter
class Timer:
    def __init__(self,master=None,root=None,cnf={},**kw):
        self.master = master #set master
        self.root = root #set root for update binding
        self._timeVar = tk.StringVar()#variable to hold string representation of itme
        self._timeVar.set("00m:00s")
        self._clockContinue = True

        self._start = time.time() #set clock start time

        self.timeLabel = tk.Label(master,cnf,textvariable=self._timeVar,**kw)#Create label to hold timer


    #function starts clock updating itself
    def updateClock(self):
        self._timeVar.set(time.strftime("%Mm:%Ss",time.gmtime(time.time()-self._start)))

        #Clock only continues ticking while self.clockContinue is true
        if self._clockContinue:
            self.root.after(500,self.updateClock)

    #Start clock from 0
    def startClock(self):
        self._start = time.time()
        self._clockContinue = True
        self.updateClock()#start clock cycle
        

    #Stop clock
    def stopClock(self):
        self._clockContinue = False

    #Reset Clock to 0
    def resetClock(self):
        self._start = time.time()
        self._timeVar.set(time.strftime("%Mm:%Ss",time.gmtime(time.time()-self._start)))
     
    #Restart clock without resetting
    def restartClock(self):
        self._clockContinue = True
        self.updateClock()#start clock cycle




