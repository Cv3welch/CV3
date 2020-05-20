# This file was created by Christian Vaughn-Welch
# Sources: https://www.pythonforbeginners.com/code-snippets-source-code/game-hangman

#importing the time module
import time
import sys
import random
RUNNING = True
# word = None

Animals = ["MOUSE", "LION", "BIRD", "DOG", "CAT",]
Movies = ["HARRY POTTER", "LORD OF THE RINGS", "STAR WARS", "STAR TREK"]
Colors = ["YELLOW", "RED", "BLUE", "PURPLE", "GREEN", "BLACK", "WHITE"]

def play():
    # name = input("What is your name? ")
    # reply = (name, "Do you want to play hangman? Press Y for yes and N for no ")
    reply = input("Do you want to play hangman? Press Y for yes and N for no ")
    
    if reply == "Y":
        global RUNNING 
        RUNNING = True

    if reply == "N":
        RUNNING = False 
        print("Come back when you want to have fun :(" )
        sys.exit()

        '''
        This block asks the user if they wan't to play the game, if they assure that they do it starts the game
        If they decline, it shuts down the system
        '''

def category():
    which_category = input("What Category would you like to choose from? Animals, Movies, or Colors. or if you would like to end the game type 'Q' :) ")
    global word

    if which_category == "Animals":
        word = random.choice(Animals)
        # global word 

    if which_category == "Movies":
        word = random.choice(Movies)
        # global word

    if which_category == "Colors":
        word = random.choice(Colors)
    
    if which_category == "Q":
        print("Come back when you want to have fun :(" )
        sys.exit()

        '''
        This block of code, starts the game by asking the user what category they want to guess from, with the choices
        being, Animals, Movies, and Colors, and when they choose a category it randomly selects a word from whatever category they choose
        '''
# Creates an empty variable, where guesses can be inputed 
    guesses = ''
    turns = 6
    while turns > 0:         
        fails = 0             
        for char in word:      
            if char in guesses:    
                print(char)  
            else:
                print("_")    
                fails += 1    

        if fails == 0:        
                print("You won!!!")
                break   

        guess = input("guess a character:").capitalize()
        guesses += guess   

        if guess not in word:  
                turns -= 1        
                print("Wrong")
                print("You have", + turns, "more guesses")
        
        if turns == 0:           
                print("You Lose :( The word was", word)
            
'''
This block of code, gives the user with the ability to giuess a character, presents the user with, their progress in the game 
and tells the user how many more guesses they have left. Then creates an empty variable in guesses and then it defines how many turns the user is given, with 6 turns, because Theres the head, both arms and legs and then the torso, 
And then i created a counter, in fails that would represent all the letters you guess that aren't in the word.
If it is in the guesses then it prints the letter in the guesses and if not it adds one to the fails.
'''

play()
while RUNNING == True:
    category()
