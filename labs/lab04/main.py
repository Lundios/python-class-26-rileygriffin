# Starting file for LAB 4
# Include your course number, student first and last name, and date in the comment header
# CS 31 Lab Activity 4
# October 21, 2026
# Riley Griffin

import random
"""Be sure to use functions as the starting program does.
Ask for player's name. Output their name at least once.
Ask player if they would like to play an EASY, MEDIUM or HARD game.
easy = range of 1 to 10, limit tries to 5.
medium = range of 1 to 100, limit tries to 8.
hard = range of 1 to 1000, limit tries to 10.
If the player doesn't guess the number in the required amount of tries, they lose the game.
Keep track of the wins and loses for the player, displaying the score before asking if they would like to play again. 
Be sure to create a comment at the top of the program with your name, the date, and the class number, and assignment name.
Include comments to describe what you are doing in your program. Refer to your textbook code examples for an appropriate level of comments. """

wins = int(0)
losses = int(0)

#print title of program
def displayTitle():
  print("welcome to the guess the number game")
  print()

def playGame():
    global wins,losses
    print("""
    E: Easy   - Guess from 1 to 10, limit 5 attempts    
    M: Medium - Guess from 1 to 100, limit 7 attempts 
    H: Hard   - Guess from 1 to 1000, limit 10 attempts 
    """)
    while True:
        difficulty = input("What difficulty would you like to play? E/M/H: ").upper()
        if(difficulty == "H"):
          limit = 1000
          attempts = 10
          break
        elif(difficulty == "M"):
           limit = 100
           attempts = 7
           break
        elif(difficulty == "E"):
           limit = 10
           attempts = 5
           break
        else: 
            print("\nINVALID INPUT STOP.\n")
        
    secretNumber = random.randint(1,limit)
    print(f"I am thinking of a number from 1 to {limit}\n")
    count = 1 #keep track of the total number of attempts

    while(guess := int(input("Your guess: "))) != secretNumber:
        #THE GUESS IS INCORRECT
        if guess < secretNumber:
            print("Sorry, your guess is too low.")
        elif guess > secretNumber:
            print("Sorry, your guess is too high")
        count += 1 #increment guess attempt counter

        #check if any attempts left
        if count > attempts:
            print("You've ran out of chances.")
            losses += 1
            winLoss()
            break
    else:
         #if they guessed correctly
         print(f"Congrats! you guessed it in {count} tries!\n")
         wins += 1
         winLoss()
    

def main():
    #the main program driver
    displayTitle()

    #ask for player name
    userName = input("please give me your name: ")
    
    again = "y" #set initial game loop varible

    while again.lower() == "y": #play the game
         playGame()
         again = input(f"Would you like to play another round of the game, {userName}? y/n: ")
         print()
    print(f"Come back soon, Goodbye {userName}.")

def winLoss():
    print(f"you currently have {wins} wins and {losses} losses\n")


#if started as the main module call the main() function
if __name__ == "__main__":
    main()