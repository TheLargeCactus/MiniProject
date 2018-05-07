  #THIS PROGRAM IS A MADLIB GAME
#AUTHORS: CRISTOBAL MITCHELL, BRANDON EASTON, KIRSTEN VILLA
#DATE MODIFIED: 05/05/2018
#VERSION: 0.1

#DEBUG FLAG
debug = False

#IMPORTS
import sys
import tkinter
import tkinter as tk
#from PIL import ImageTK
from tkinter import *
#from PIL import ImageTk, Image
import os from PyDictionary import PyDictionary
dictionary = PyDictionary()
go = ""
class MADLIBS():
    running = True
    catch = ""
    finishHit = ""
    go = ""
    def __init__(self):
        pass

    def start(self):
        print
        print  ("****     ****     **     *******         **       ** ******    ********")
		    print  ("/**/**   **/**    ****   /**////**       /**      /**/*////**  **////// ")
		    print  ("/**//** ** /**   **//**  /**    /**      /**      /**/*   /** /**       ")
		    print  ("/** //***  /**  **  //** /**    /**      /**      /**/******  /*********")
		    print  ("/**  //*   /** **********/**    /**      /**      /**/*//// **////////**")
		    print  ("/**   /    /**/**//////**/**    **       /**      /**/*    /**       /**")
        print  ("/**        /**/**     /**/*******        /********/**/*******  ******** ")
        print  ("//         // //      // ///////         //////// // ///////  ////////  ")
        print  
        print

        return self.player()     

    def player(self):
        name = raw_input("Player, what is your name? ")
        print 
        print ("Hello %s, lets get started...\n" % name)
        return self.game_select(name)
	
    def game_select(self, name):
        games = ["baseball", "weird day", "star wars"]
        print ("The libs that are available...\n")
        for game in games:
			print (game)
        print
        selected = raw_input("Which game would you like to play? ").lower()
        if selected in games:
            if selected == "baseball":
                go = "baseball"
                return self.my_game_baseball(name)
            elif selected == "star wars":
                go = "star wars"
                return self.m2_game_star(name)
            elif selected == "weird day":
                go = "weird day"
                return self.ml_weird_day(name)
        else:
            print ("I'm sorry that is not a valid selection")
            return self.game_select(name)

    def m2_game_star(self, name):        
        print ("\n")                                                                # Create a space 
        print ("Please provide me with each of the follow...\n")                    # Instructs the user to provide information

        adj = raw_input("Please enter an adjective. ")                              # Instructs the user to enter an adjective
		    adj = adjective(adj)

        #from PyDictionary import PyDictionary                                       # Imports a dictionary form the python libraries   
        #dictionary = PyDictionary()                                                 # Creates a variable containing the library
        #meaning = dictionary.meaning(adj)                                           # Creates a variable that holds the meaning of the user entered word        
        #stop = False                                                                # Variable that holds a false value for while loops
        #while stop == False:                                                        # While to make sure that the user enters the correct part of speech
            #if "Adjective" in meaning:
                #stop = True
            #else:
                #print ("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \nThe word you enter is not the correct part of speech. Here is the meaning of the word you entered. \n")
                #print (meaning, "\n")
                #adj = raw_input("Please try another word. ")
                #meaning = dictionary.meaning(adj)
                #print ("\n")                

        adj1 = raw_input("please enter another adjective. ")
		    adj1 = adjective(adj1)
        #meaning = dictionary.meaning(adj1)
        #stop = False
        #while stop == False:
			      #if "Adjective" in meaning:
				        #stop = True
            #else:
                #print ("\n \n The word you enter is not the correct part of speech. Here is the meaning of the word you entered. \n")
                #print (meaning, "\n")
                #adj1 = raw_input("Please try another word. ")
                #meaning = dictionary.meaning(adj1)
                #print ("\n")

        noun = raw_input("Please enter a noun ")
		    noun = checkNoun(noun)
        #meaning = dictionary.meaning(noun)
        #print (noun," ", meaning)
        #stop = False
        #while stop == False:
            #if 'Noun' in meaning:
                #stop = True
            #else:
                #print ("\n \n The word you enter is not the correct part of speech. Here is the meaning of the word you entered. \n")
                #print (meaning, "\n")
                #noun = raw_input("Please try another word. ")
                #meaning = dictionary.meaning(noun)
                #print ("\n")

        STORY = "\n \n %s went into a %s %s %s. \n \n"
        print 
        print (STORY % (name, adj, adj1, noun))

    def my_game_baseball(self, name):
        print ("\n")
        print ("Please provide me with each of the follow...\n")

        nouns = raw_input("Enter the Brewers score. This number is a noun. ")
        print ("\n")
        brewersScore = nouns
        score1 = int(nouns)

        nouns = raw_input("Enter the Yankees score. This number is a noun. ")
        print ("\n")
        yankeesScore = nouns
        score2 = int(nouns)

        adj1 = raw_input("Enter a inning number 1-9. This number is an adjective to the Inning. Inning is a noun. ")
        print ("\n")

        nounRunners = raw_input("How may runners on bases? This number is noun. ")
        print ("\n")
       
        while not nounRunners in ("No runners on base.", "Runner on first base.", "Runners on first and second base.", "Bases loaded."):
            if nounRunners == "0":
                runners = "No runners on base."
            elif nounRunners == "1":
                nounRunners = "Runner on first base."
            elif nounRunners == "2":
                nounRunners = "Runners on first and second base."
            elif nounRunners == "3":
                nounRunners = "Bases loaded."
            else:
                print ("Please enter a number between 0 to 3.")
                nounRunners = raw_input("How may runners on bases? This number is noun.")
        

        out = raw_input("Enter the number of out(s). ")
        print ("\n")

        while not out in ("no outs.", "one out.", "two outs."):
            if out == "0":
               out = "no outs."
            elif out == "1":
                out = "one out."
            elif out == "2":
                out = "two outs."
            else:
                print ("Please enter a number between 0 to 2.")
                out = raw_input("Enter the number of out(s).")

        ball = raw_input("Enter the number of ball(s). ")
        print ("\n")

        while not ball in ("0", "1", "2", "3"):
            if ball < "0" or ball > "3":
                print ("Please enter a number between 0 to 3.")
                out = raw_input("Enter the number of out(s).")

        strike = raw_input("Enter the number of strike(s). ")
        print ("\n")

        while not strike in ("0", "1", "2"):
            if strike < "0" or strike > "2":
                print ("Please enter a number between 0 to 2.")
                out = raw_input("Enter the number of strike(s).")

        play = raw_input("Enter 'catch' or 'homerun' ")
        print ("\n")
        
        while not play in ("catch", "homerun"):
            if play == "catch":
                catch = "makes the catch. Oh! my god, he made an exceptional catch against the wall robbing"
                #play =  "makes the catch. Oh! my god, he made an exceptional catch against the wall robbing"
                finishHit = "of game winning homerun. Yankees win the world series"
                #play = finishHit
            elif play == "homerun":
                catch = "the ball tips off his glove. It's a homerun."
                finishHit = "wins the world series!"
                brewersScore = "5"                  
            else:
                print ("Please enter 'catch' or 'homerun' only")
                play = raw_input("Enter 'catch' or 'homerun' ")           
              
        if play == "catch":
            catch =  "makes the catch. Oh! my god, he made an exceptional catch against the wall robbing"
            finishHit = "of game winning homerun. Yankees win the world series"

        if (score1 < score2):
            runDiff = score2 - score1
            scenerio = "Brewers down by"
        elif (score2 < score1):
            runDiff = score1 - score2
            scenerio = "Yankees down by"
        else:
            scenerio = "Score is tied"
        
        period = "."
        
        STORY = "Game 7 of the World Series; New York Yankees Vs. Milwaukee Brewers. Bottom of the %sth inning Brewers up bat. %s The score is the Brewers %s, the Yankees %s! %s is up to bat for the Brewers with %s %s %s%s The count %s-%s. Here's the pitch.... %s hits a lazer to right center field. Hicks turns and bolts towards the wall. This balls got a chance. Hick jumps and %s %s %s %s to %s"            
        print        
        print (STORY % (adj1, nounRunners, brewersScore, yankeesScore, name, out, scenerio, runDiff, period, ball, strike, name, catch, name, finishHit, brewersScore, yankeesScore))

            
    def ml_weird_day(self, name):
        print ("Please provide me with each of the follow...\n")
        noun1 = raw_input("A noun: ")
		    noun1 = checkNoun(noun1)

        adj1 = raw_input("An adjective: ")
		    adj1 = adjective(adj1)

        noun2 = raw_input("A plural noun: ")
		    noun2 = checkNoun(noun2)

        famous = raw_input("The name of a famous person: ")
        place = raw_input("A place: ")
        verbing1 = raw_input("A verb ending in 'ing': ")

        adj2 = raw_input("Another adjective: ")
		    adj2 = adjective(adj2)

        song = raw_input("Your favorite song: ")
        verbed = raw_input("A verb ending in 'ed': ")
        adverb = raw_input("An adverb: ")
        verbing2 = raw_input("Another verb ending in 'ing': ")
        model = raw_input("The name of a supermodel: ")

        adj3 = raw_input("One final adjective: ")
		    adj3 = adjective(adj3)

        STORY = "Once upon a time there was a %s. It had %s %s! One day it met %s on the side of the %s they were %s. It was very %s; they both looked like hobos! All of the sudden they started singing %s really loudly. They %s really %s! %s started %s with %s. They looked really %s!"
        print
        print (STORY % (noun1, adj1, noun2, famous, place, verbing1, adj2, song, verbed, adverb, famous, verbing2, model, adj3))

	def adjective(word):
		from PyDictionary import PyDictionary                                       # Imports a dictionary form the python libraries   
        dictionary = PyDictionary()                                             # Creates a variable containing the library
        word = dictionary.meaning(adj)                                          # Creates a variable that holds the meaning of the user entered word
		stop = False                                                                # Variable that holds a false value for while loops
        while stop == False:                                                    # While to make sure that the user enters the correct part of speech
            if "Adjective" in word:
                stop = True
            else:
                print ("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \nThe word you enter is not the correct part of speech. Here is the meaning of the word you entered. \n")
                print (meaning, "\n")
                adj = raw_input("Please try another word. ")
                word = dictionary.meaning(adj)
                print ("\n")
		return word

	def checkNoun(word):
		from PyDictionary import PyDictionary                                       # Imports a dictionary form the python libraries   
        dictionary = PyDictionary()                                             # Creates a variable containing the library
        word = dictionary.meaning(noun)                                         # Creates a variable that holds the meaning of the user entered word
		stop = False                                                                # Variable that holds a false value for while loops
        while stop == False:                                                    # While to make sure that the user enters the correct part of speech
            if "Noun" in word:
                stop = True
            else:
                print ("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \nThe word you enter is not the correct part of speech. Here is the meaning of the word you entered. \n")
                print (meaning, "\n")
                adj = raw_input("Please try another word. ")
                word = dictionary.meaning(adj)
                print ("\n")
		return word

if __name__ == "__main__":

    #if go == "baseball":
        #my = MADLIBS()
        #my.start()
    #elif go == "star wars":
        m2 = MADLIBS()
        m2.start()

