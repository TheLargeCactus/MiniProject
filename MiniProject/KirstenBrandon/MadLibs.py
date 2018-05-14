#Kirsten/Brandon put your stuff in here

#THIS PROGRAM IS A MADLIB GAME
#AUTHORS: CRISTOBAL MITCHELL, BRANDON EASTON, KIRSTEN VILLA
#DATE MODIFIED: 05/05/2018
#VERSION: 0.1

#DEBUG FLAG
debug = False

#IMPORTS
import sys

#import Tkinter as tk
#from Tkinter import *

#import os
from PyDictionary import PyDictionary
dictionary = PyDictionary()

import autocorrect
from autocorrect import spell 

#################################################### Local variables #########################################################################################
count = 0
################################################## End local Variables #####################################################################################

################################################## Defintions ##############################################################################################

                                ############# Adjective word checker ################
def adjective(word):                                                                                    # def to check the user enter word for spelling and part(s) of speech
    userEnteredWord = word                                                                              # intializes the variable 'userEnteredWord' for spell checking
    word = spell(word)                                                                                  # Checks to see if the user word was spelled correctly. if not it corrects the word
    stop = False                                                                                        # Variable that holds a false value for while loops     
    count = 0                                                                                           # Initializes the variable 'count' to 0
    while userEnteredWord != word:                                                                      # If statement to check is the user entered word is spelled correctly.
        if count == 0:                                                                                  # If statement to for first time user mis-spelled word
            print("\nThe word you spelled is in-correct: ", userEnteredWord, '\n')                      # Prints the user entered word.
            print("Here's the correct spelling of the word: ", word, '\n')                              # Prints the correct spelling of the user entered word.
            userEnteredWord = input("Please spell the word again. ")                                    # Print the instructions for the user to spell the word again.
        if count > 0:                                                                                   # If statement if the user continues to mis-spell the word             
            userEnteredWord = input("\nOops! That's not correct either. Please try again: ")            # Prints instructions for the user to try again.
        if userEnteredWord == word:                                                                     # If statment to determine if the word is spell correctly
            userEnteredWord = word                                                                      # If word is spelled correctly, then it ends the While Loop
        count = count + 1                                                                               # Adds one the 'count' variable just in case the user has more than one mis-spelling on the same part of speech.
    print('\n')                                                                                         # Prints a blank line
    word = spell(word)                                                              # Checks to see if the user word was spelled correctly. if not it corrects the word
    meaning = dictionary.meaning(word)                                              # Creates a variable that holds the meaning of the user entered word
    stop = False                                                                    # Variable that holds a false value for while loops
    while stop == False:                                                            # While to make sure that the user enters the correct part of speech
        if "Adjective" in meaning:                                                  # Checks the definition with word to determine if the word is the correct part of speech
            print(meaning, '\n')                                                    # Prints the part(s) of speech with the definition
            stop = True                                                             # Variable to end the "While Loop'
        else:
            print ("\n The word you enter is not the correct part of speech. Here is the meaning of the word you entered. \n")  # Message to info the user that they enter the wrong part of speech
            print (meaning, "\n")                                                                                               # Prints the part(s) of speech and the definition of the user enter word that was not correct
            word = input("Please try another word. ")                                                                           # Instructs the user to enter another word
            word = spell(word)                                                                                                  # Checks to see if the user word was spelled correctly. if not it corrects the word
            meaning = dictionary.meaning(word)                                                                                  # Places the part(s) of speech and the definition in the variable 'meaning'.

    return word

                                 ############# End Adjective word checker ################      
                                 

                                ################### Noun word checker ####################
#Noun wordchecker
def noun(word):                                                                                         # def to check the user enter word for spelling and part(s) of speech
    userEnteredWord = word                                                                              # intializes the variable 'userEnteredWord' for spell checking
    word = spell(word)                                                                                  # Checks to see if the user word was spelled correctly. if not it corrects the word
    stop = False                                                                                        # Variable that holds a false value for while loops     
    count = 0                                                                                           # Initializes the variable 'count' to 0
    while userEnteredWord != word:                                                                      # If statement to check is the user entered word is spelled correctly.
        if count == 0:                                                                                  # If statement to for first time user mis-spelled word
            print("\nThe word you spelled is in-correct: ", userEnteredWord, '\n')                      # Prints the user entered word.
            print("Here's the correct spelling of the word: ", word, '\n')                              # Prints the correct spelling of the user entered word.
            userEnteredWord = input("Please spell the word again. ")                                    # Print the instructions for the user to spell the word again.
        if count > 0:                                                                                   # If statement if the user continues to mis-spell the word             
            userEnteredWord = input("\nOops! That's not correct either. Please try again: ")            # Prints instructions for the user to try again.
        if userEnteredWord == word:                                                                     # If statment to determine if the word is spell correctly
            userEnteredWord = word                                                                      # If word is spelled correctly, then it ends the While Loop
        count = count + 1                                                                               # Adds one the 'count' variable just in case the user has more than one mis-spelling on the same part of speech.
    print('\n')                                                                                         # Prints a blank line
    word = spell(word)                                                              # Checks to see if the user word was spelled correctly. if not it corrects the word
    meaning = dictionary.meaning(word)                                              # Creates a variable that holds the meaning of the user entered word
    stop = False                                                                    # Variable that holds a false value for while loops
    while stop == False:                                                            # While to make sure that the user enters the correct part of speech
        if "Noun" in meaning:                                                       # Checks the definition with word to determine if the word is the correct part of speech
            print ("Good job, you entered a noun!\n")
            print ("Below is the definition of", word)                      
            print(meaning, "\n")                                                    # Prints the part(s) of speech with the definition
            stop = True                                                             # Variable to end the "While Loop'
        else:
            print ("\n The word you enter is not the correct part of speech. Here is the meaning of the word you entered. \n")  # Message to info the user that they enter the wrong part of speech
            print (meaning, "\n")                                                                                               # Prints the part(s) of speech and the definition of the user enter word that was not correct
            word = input("Please try another word. ")                                                                           # Instructs the user to enter another word
            word = spell(word)                                                                                                  # Checks to see if the user word was spelled correctly. if not it corrects the word
            meaning = dictionary.meaning(word)                                                                                  # Places the part(s) of speech and the definition in the variable 'meaning'.

    return word

                                ################ End noun word checker ####################


                                ############### Plural noun word checker ##################
#Plural Noun wordchecker
def pluralNoun(word):                                                               # def to check the user enter word for spelling and part(s) of speech
    userEnteredWord = word                                                                              # intializes the variable 'userEnteredWord' for spell checking
    word = spell(word)                                                                                  # Checks to see if the user word was spelled correctly. if not it corrects the word
    stop = False                                                                                        # Variable that holds a false value for while loops     
    count = 0                                                                                           # Initializes the variable 'count' to 0
    while userEnteredWord != word:                                                                      # If statement to check is the user entered word is spelled correctly.
        if count == 0:                                                                                  # If statement to for first time user mis-spelled word
            print("\nThe word you spelled is in-correct: ", userEnteredWord, '\n')                      # Prints the user entered word.
            print("Here's the correct spelling of the word: ", word, '\n')                              # Prints the correct spelling of the user entered word.
            userEnteredWord = input("Please spell the word again. ")                                    # Print the instructions for the user to spell the word again.
        if count > 0:                                                                                   # If statement if the user continues to mis-spell the word             
            userEnteredWord = input("\nOops! That's not correct either. Please try again: ")            # Prints instructions for the user to try again.
        if userEnteredWord == word:                                                                     # If statment to determine if the word is spell correctly
            userEnteredWord = word                                                                      # If word is spelled correctly, then it ends the While Loop
        count = count + 1                                                                               # Adds one the 'count' variable just in case the user has more than one mis-spelling on the same part of speech.
    print('\n')                                                                                         # Prints a blank line
    word = spell(word)                                                              # Checks to see if the user word was spelled correctly. if not it corrects the word
    meaning = dictionary.meaning(word)                                              # Creates a variable that holds the meaning of the user entered word
    stop = False                                                                    # Variable that holds a false value for while loops
    while stop == False:                                                            # While to make sure that the user enters the correct part of speech
        if word.endswith('s'):
            if "Noun" in meaning:                                                   # Checks the definition with word to determine if the word is the correct part of speech
                print(meaning, '\n')                                                # Prints the part(s) of speech with the definition
                stop = True                                                         # Variable to end the "While Loop'
            else:
                print ("\n The word you enter is not the correct part of speech. Here is the meaning of the word you entered. \n")  # Message to info the user that they enter the wrong part of speech
                print (meaning, "\n")                                                                                               # Prints the part(s) of speech and the definition of the user enter word that was not correct
                word = input("Please try another word. ")                                                                           # Instructs the user to enter another word
                word = spell(word)                                                                                                  # Checks to see if the user word was spelled correctly. if not it corrects the word
                meaning = dictionary.meaning(word)                                                                                  # Places the part(s) of speech and the definition in the variable 'meaning'.
        else:
            print("The word you enter is not plural. Please try again.")
            word = input("Enter a plural noun: ")
            word = spell(word)
            meaning = ddictionary.meaning(word)

    return word

                                ############# End plural noun word checker ################


                                ################# Adverb word checker #####################

#Adverb word checker
def adverb(word):                                                                                       # def to check the user enter word for spelling and part(s) of speech
    userEnteredWord = word                                                                              # intializes the variable 'userEnteredWord' for spell checking
    word = spell(word)                                                                                  # Checks to see if the user word was spelled correctly. if not it corrects the word
    stop = False                                                                                        # Variable that holds a false value for while loops     
    count = 0                                                                                           # Initializes the variable 'count' to 0
    while userEnteredWord != word:                                                                      # If statement to check is the user entered word is spelled correctly.
        if count == 0:                                                                                  # If statement to for first time user mis-spelled word
            print("\nThe word you spelled is in-correct: ", userEnteredWord, '\n')                      # Prints the user entered word.
            print("Here's the correct spelling of the word: ", word, '\n')                              # Prints the correct spelling of the user entered word.
            userEnteredWord = input("Please spell the word again. ")                                    # Print the instructions for the user to spell the word again.
        if count > 0:                                                                                   # If statement if the user continues to mis-spell the word             
            userEnteredWord = input("\nOops! That's not correct either. Please try again: ")            # Prints instructions for the user to try again.
        if userEnteredWord == word:                                                                     # If statment to determine if the word is spell correctly
            userEnteredWord = word                                                                      # If word is spelled correctly, then it ends the While Loop
        count = count + 1                                                                               # Adds one the 'count' variable just in case the user has more than one mis-spelling on the same part of speech.
    print('\n')                                                                                         # Prints a blank line
    userEnteredWord = word                                                                              # intializes the variable 'userEnteredWord' for spell checking
    word = spell(word)                                                                                  # Checks to see if the user word was spelled correctly. if not it corrects the word
    stop = False                                                                                        # Variable that holds a false value for while loops     
    count = 0                                                                                           # Initializes the variable 'count' to 0
    while userEnteredWord != word:                                                                      # If statement to check is the user entered word is spelled correctly.
        if count == 0:                                                                                  # If statement to for first time user mis-spelled word
            print("\nThe word you spelled is in-correct: ", userEnteredWord, '\n')                      # Prints the user entered word.
            print("Here's the correct spelling of the word: ", word, '\n')                              # Prints the correct spelling of the user entered word.
            userEnteredWord = input("Please spell the word again. ")                                    # Print the instructions for the user to spell the word again.
        if count > 0:                                                                                   # If statement if the user continues to mis-spell the word             
            userEnteredWord = input("\nOops! That's not correct either. Please try again: ")            # Prints instructions for the user to try again.
        if userEnteredWord == word:                                                                     # If statment to determine if the word is spell correctly
            userEnteredWord = word                                                                      # If word is spelled correctly, then it ends the While Loop
        count = count + 1                                                                               # Adds one the 'count' variable just in case the user has more than one mis-spelling on the same part of speech.
    print('\n')                                                                                         # Prints a blank line
    word = spell(word)                                                              # Checks to see if the user word was spelled correctly. if not it corrects the word
    if userEnteredWord != word:                                                     # If statement to check is the user entered word is spelled correctly.
        print("The word you spelled is in-correct: ", userEnteredWord, '\n')        # Prints the user entered word.
        print("Here's the correct spelling of the word: ", word, '\n')              # Prints the correct spelling of the user entered word.
    word = spell(word)                                                              # Checks to see if the user word was spelled correctly. if not it corrects the word
    meaning = dictionary.meaning(word)                                              # Creates a variable that holds the meaning of the user entered word
    stop = False                                                                    # Variable that holds a false value for while loops
    while stop == False:                                                            # While to make sure that the user enters the correct part of speech
        if "Adverb" in meaning:                                                     # Checks the definition with word to determine if the word is the correct part of speech
            print(meaning, "\n")                                                    # Prints the part(s) of speech with the definition
            stop = True                                                             # Variable to end the "While Loop'
        else:
            print ("\n The word you enter is not the correct part of speech. Here is the meaning of the word you entered. \n")  # Message to info the user that they enter the wrong part of speech
            print (meaning, "\n")                                                                                               # Prints the part(s) of speech and the definition of the user enter word that was not correct
            word = input("Please try another word. ")                                                                           # Instructs the user to enter another word
            word = spell(word)                                                                                                  # Checks to see if the user word was spelled correctly. if not it corrects the word
            meaning = dictionary.meaning(word)                                                                                  # Places the part(s) of speech and the definition in the variable 'meaning'.

    return word

                                ############### End adverb word checker ###################


                                ############ word ending in 'ing' checker #################

#'ing' wordchecker
def Ing(word):                                                                                          # def to check the user enter word for spelling and part(s) of speech
    userEnteredWord = word                                                                              # intializes the variable 'userEnteredWord' for spell checking
    word = spell(word)                                                                                  # Checks to see if the user word was spelled correctly. if not it corrects the word
    stop = False                                                                                        # Variable that holds a false value for while loops     
    count = 0                                                                                           # Initializes the variable 'count' to 0
    while userEnteredWord != word:                                                                      # If statement to check is the user entered word is spelled correctly.
        if count == 0:                                                                                  # If statement to for first time user mis-spelled word
            print("\nThe word you spelled is in-correct: ", userEnteredWord, '\n')                      # Prints the user entered word.
            print("Here's the correct spelling of the word: ", word, '\n')                              # Prints the correct spelling of the user entered word.
            userEnteredWord = input("Please spell the word again. ")                                    # Print the instructions for the user to spell the word again.
        if count > 0:                                                                                   # If statement if the user continues to mis-spell the word             
            userEnteredWord = input("\nOops! That's not correct either. Please try again: ")            # Prints instructions for the user to try again.
        if userEnteredWord == word:                                                                     # If statment to determine if the word is spell correctly
            userEnteredWord = word                                                                      # If word is spelled correctly, then it ends the While Loop
        count = count + 1                                                                               # Adds one the 'count' variable just in case the user has more than one mis-spelling on the same part of speech.
    print('\n')                                                                                         # Prints a blank line
    userEnteredWord = word                                                          # intializes the variable 'userEnteredWord' for spell checking
    word = spell(word)                                                              # Checks to see if the user word was spelled correctly. if not it corrects the word
    if userEnteredWord != word:                                                     # If statement to check is the user entered word is spelled correctly.
        print("The word you spelled is in-correct: ", userEnteredWord, '\n')        # Prints the user entered word.
        print("Here's the correct spelling of the word: ", word, '\n')              # Prints the correct spelling of the user entered word.
    stop = False                                                                    # Variable that holds a false value for while loops
    while stop == False:                                                            # While to make sure that the user enters the correct part of speech
        if word.endswith('ing'):                                                    # Checks to see if the user entered word ends with 'ing'.
            print(meaning = dictionary.meaning(word))                               # Creates a variable that holds the meaning of the user entered word)
            stop = True
        else:
            print ("\n The word you enter does not end in 'ing'")                   # Message to info the user that they enter the wrong part of speech
            word = input("Please try another word. ")                               # Instructs the user to enter another word
            word = spell(word)                                                      # Checks to see if the user word was spelled correctly. if not it corrects the word
        
    return word

                                ######### End word ending in 'ing' checker ################

############################################################################# End Definitions ##########################################################################################################################################

class MADLIBS():

    running = True
    catch = ""
    finishHit = ""
    go = ""
    def __init__(self):

        pass



    def start(self):
        ################################################################## Print the title of the game program ##################################################
        print                                                                                                                                                   #
                                                                                                                                                                #
        print  ("****     ****     **     *******         **       ** ******    ********")                                                                      #
                                                                                                                                                                #
        print  ("/**/**   **/**    ****   /**////**       /**      /**/*////**  **////// ")                                                                     #
                                                                                                                                                                #
        print  ("/**//** ** /**   **//**  /**    /**      /**      /**/*   /** /**       ")                                                                     #
                                                                                                                                                                #
        print  ("/** //***  /**  **  //** /**    /**      /**      /**/******  /*********")                                                                     #
                                                                                                                                                                #
        print  ("/**  //*   /** **********/**    /**      /**      /**/*//// **////////**")                                                                     #
                                                                                                                                                                #
        print  ("/**   /    /**/**//////**/**    **       /**      /**/*    /**       /**")                                                                     #
                                                                                                                                                                #
        print  ("/**        /**/**     /**/*******        /********/**/*******  ******** ")                                                                     #
                                                                                                                                                                #
        print  ("//         // //      // ///////         //////// // ///////  ////////  ")                                                                     #
                                                                                                                                                                #
        print                                                                                                                                                   #
                                                                                                                                                                #
        print                                                                                                                                                   #
        ############################################################## End print the title of the game program ##################################################
        
        
        return self.player()                                                            # Return the player
    
################################################################## Definitions ##################################################################################
    def player(self):

        name = input("Player, what is your name? ")

        print ("Hello %s, lets get started...\n" % name)

        return self.game_select(name)

    def game_select(self, name):

        games = ["baseball", "weird day", "star wars", "vacation"]

        print ("The libs that are available...\n")

        for game in games:

            print (game, '\n')

        selected = input("Which game would you like to play? ").lower()
        #print('\n')
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



            elif selected == "vacation":
                go = "vacation"
                return self.m3_vacation(name)



        else:

            print ("I'm sorry that is not a valid selection \n")
            return self.game_select(name)

########################################################### STAR WARS ###################################################################################################

    def m2_game_star(self, name):
       
        print ("In a galaxy far, far away, there lived a \n")

        word = input("Please enter an adjective. ")                              # Instructs the user to enter an adjective        

        correctSpelling = spell(word)

        if correctSpelling == word:
            meaning = dictionary.meaning(word)
            print (meaning)
            adj = word
        else:
            print ("The word you spelled is incorrect,")
            print ("Here is your spelled word: ", word)
            word = input("please")        
       
                

        adj1 = input("please enter another adjective. ")
        meaning = dictionary.meaning(adj1)
        stop = False
        while stop == False:
            if "Adjective" in meaning:
                stop = True
            else:
                print ("\n \n The word you enter is not the correct part of speech. Here is the meaning of the word you entered. \n")
                print (meaning, "\n")
                adj1 = input("Please try another word. ")
                meaning = dictionary.meaning(adj1)
                print ("\n")

        noun = input("Please enter a noun ")
        meaning = dictionary.meaning(noun)
        print (noun," ", meaning)
        stop = False
        while stop == False:
            if 'Noun' in meaning:
                stop = True
            else:
                print ("\n \n The word you enter is not the correct part of speech. Here is the meaning of the word you entered. \n")
                print (meaning, "\n")
                noun = input("Please try another word. ")
                meaning = dictionary.meaning(noun)
                print ("\n")

        print ("\n Who prayed on the innocent people of \n")

        noun1 = input("Please enter a noun ")
              

        print ("\n His rein of terror ravished the villages of", noun1, ". Then one day a \n")

        adj2 = input("Please enter a adjective ")
        meaning = dictionary.meaning(adj2)

        stop = False
        while stop == False:
            if 'Adjective' in meaning:
                stop = True
            else:
                print ("\n \n The word you enter is not the correct part of speech. Here is the meaning of the word you entered. \n")
                print (meaning, "\n")
                noun = input("Please try another word. ")
                meaning = dictionary.meaning(adj2)
                print ("\n")

        print ("\n \n")


        STORY = "In a galaxy far, far away; there lived a %s %s %s. Who prayed on the innocent people of %s. His rein of terror ravished the villages of %s. Then one day a %s Jedi knight named %s came to %s and helped the people destroy the vileness monster."
        print (STORY % (adj, adj1, noun, noun1, noun1, adj2, name, noun1))


########################################################################  BASEBALL ######################################################################################################################

    def my_game_baseball(self, name):

        print ("\n")
        print ("Please provide me with each of the follow...\n")

        nouns = input("Enter the Brewers score. This number is a noun. ")
        print ("\n")
        brewersScore = nouns
        score1 = int(nouns)

        nouns = input("Enter the Yankees score. This number is a noun. ")
        print ("\n")
        yankeesScore = nouns
        score2 = int(nouns)

        adj1 = input("Enter a inning number 1-9. This number is an adjective to the Inning. Inning is a noun. ")
        print ("\n")

        nounRunners = input("How may runners on bases? This number is noun. ")
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
                nounRunners = input("How may runners on bases? This number is noun.")
        

        out = input("Enter the number of out(s). ")
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
                out = input("Enter the number of out(s).")

        ball = input("Enter the number of ball(s). ")
        print ("\n")

        while not ball in ("0", "1", "2", "3"):
            if ball < "0" or ball > "3":
                print ("Please enter a number between 0 to 3.")
                out = input("Enter the number of out(s).")

        strike = input("Enter the number of strike(s). ")
        print ("\n")

        while not strike in ("0", "1", "2"):
            if strike < "0" or strike > "2":
                print ("Please enter a number between 0 to 2.")
                out = input("Enter the number of strike(s).")

        play = input("Enter 'catch' or 'homerun' ")
        print ("\n")
        
        while not play in ("catch", "homerun"):
            if play == "catch":
                catch = "makes the catch. Oh! my god, he made an exceptional catch against the wall robbing"
                finishHit = "of game winning homerun. Yankees win the world series"
            elif play == "homerun":
                catch = "the ball tips off his glove. It's a homerun."
                finishHit = "wins the world series!"
                brewersScore = "5"                  
            else:
                print ("Please enter 'catch' or 'homerun' only")
                play = input("Enter 'catch' or 'homerun' ")  
         
              
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
                
        print (STORY % (adj1, nounRunners, brewersScore, yankeesScore, name, out, scenerio, runDiff, period, ball, strike, name, catch, name, finishHit, brewersScore, yankeesScore))

############################################################################ WEIRD DAY ##############################################################################################################
    def ml_weird_day(self, name):

        print ("Let's play 'Weird Day'!", "\nPlease provide me with each of the follow...\n")



        nouns = input("A noun: ")
        word = nouns
        noun(word)

        adj1 = input("An adjective: ")
        word = adj1
        adjective(word)

        nouns = input("A plural noun: ")
        word = nouns
        pluralNoun(word)

        famous = input("The name of a famous person: ")
        print("\n")

        place = input("A place: ")
        print("\n")

        verbing1 = input("A verb ending in 'ing': ")


        adj2 = input("Another adjective: ")

        song = input("Your favorite song: ")

        verbed = input("A verb ending in 'ed': ")

        adverb = input("An adverb: ")

        verbing2 = input("Another verb ending in 'ing': ")

        model = input("The name of a supermodel: ")

        adj3 = input("One final adjective: ")



        STORY = "Once upon a time there were %s. It had %s %s! One day it met %s on the side of the %s they were %s. It was very %s; they both looked like hobos! All of the sudden they started singing %s really loudly. They %s really %s! %s started %s with %s. They looked really %s!"

        print (STORY % (nouns, adj1, nouns, famous, place, verbing1, adj2, song, verbed, adverb, famous, verbing2, model, adj3))

################################################################ Vacations ############################################################################################################
    def m3_vacation(self, name):

        print ("Excellent choice! Please provide each of the following \n")

        adj_1 = input("enter an adjective: ")
        word = adj_1
        adjective(word)

        adj_2 = input("enter an adjective: ")
        word = adj_2
        adjective(word)
        
        noun_1 = input("Enter a noun: ")
        word = noun_1
        noun(word)
        
        noun_2 = input("Enter a noun: ")
        word = noun_2
        noun(word)
        
        animal = input("Enter a type of animal: ")
        game_1 = input("Enter a type of game: ")
        
        pl_noun_1 = input("Enter a plural noun: ")
        word = pl_noun_1
        pluralNoun(word)
        
        verbing_1 = input("Enter a verb ending in 'ing': ")
        word = verbing_1
        Ing(word)
        
        verbing_2 = input("Enter a verb ending in 'ing': ")
        word = verbing_2
        Ing(word)
        
        food_1 = input("Enter a type of food: ")
        verbing_3 = input("Enter a verb ending in 'ing': ")
        word = verbing_3
        Ing(word)
        
        noun_3 = input("Enter a noun: ")
        word = noun_3
        noun(word)
        
        plant = input("Enter a type of plant: ")
        pob = input("Enter a part of the body: ")
        place_1 = input("Enter a place: ")
        
        verbing_4 = input("Enter a verb ending in 'ing': ")
        word = verbing_4
        Ing(word)
        
        adj_3 = input("enter an adjective: ")
        word = adj_3
        adjective(word)
        
        num_1 = input("Enter a number: ")
        pl_noun_2 = input("Enter a plural noun: ")
        word = pl_noun_1
        pluralNoun(word)

        
        STORY = "A vacation is when you take a trip to some %s place with your %s family.\n Usually you go to some place that is near a/an %s or up on a/an %.\n A good vacation place is one where you can ride %s or play %s or go hunting for %s.\n I like to spend my time %s or %s. When parents go on a vacation, they spend their time eating three %s a day, and fathers play golf, and mothers sit around %s.\n Last summer, my little brother fell in a/an %s and got poison %s all over his %s.\n My family is going to go to %s, and I will practice %s.\n Parents need vacations more than kids because parents are always very %s and because they have to work %s hours every day all year making enough %s to pay for the vacation"
        
        print (STORY % (adj_1, adj_2, noun_1, noun_2, animal, game_1, pl_noun_1, verbing_1, verbing_2, food_1, verbing_3, noun_3, plant, pob, place_1, verbing_4, adj_3, num_1, pl_noun_2))
        




if __name__ == "__main__":
    
    # Weird Day
    m1 = MADLIBS()
    m1.start()

    # Star Wars
    m2 = MADLIBS()
    m2.start()

    # Baseball
    my = MADLIBS()
    my.start()

    #Vacation
    m3 = MADLIBS()
    m3.start()