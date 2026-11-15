# Starting file for PROJECT 2
# Include your course number, student first and last name, and date in the comment header
# CS 31 Project 2
# November 14, 2026
# Riley Griffin
# if started as the main module, call the main function

def main():
    #Output a title for the game.
    print("=" * 30)
    print(" Welcome to madlibs".upper())
    print("=" * 30)

    #Ask if the user would like to play a game.
    answer = input("\nWould you like to play? (Y/N): " ).lower()

    while answer != "y" and answer != "n":
        answer = input("\nPlease enter y or n: ").lower()

    if answer == "y" :
        play()
    else :
        print("")
    print("Bye!")

def play():
    storyCount = 0
    #Ask for the players name. Greet the player.
    name = input("\nWelcome, what is your name? ")
    print(f"\nHello {name}! It's time to create a story.")

    playAgain = "y"
    while playAgain == "y":
        #Ask the player to choose from TWO story ideas you have created.  Use an if statement here to separate the code for each choice.
        print("Which story would you like to do?")
        print("1. Mountain disaster")
        print("2. Corner market surprise")
        
        choice = input("\nPlease enter 1 or 2: ")

        #Ask the player to input between 6 to 10 names/words/numbers to fill in spots for your story. Please do not go over 10 inputs because it can get very long to run/test the programs! 
        #Create a short story to go along with the gameplay, substituting their inputted words into the story. Each story should be different and ask for different inputs. Do not reuse the same inputs for each story please. Your stories should be at a minimum of 4 sentences. 
        #choice 1 
        while choice != "1" and choice != "2":
             choice = input("Invalid input, please enter 1 or 2: ")
        if choice == "1":
                animal = input("(1) Give me an animal: ")
                place = input("(2) Give me a snowy place: ")
                drink = input("(3) Give me a drink: ")
                exclamation = input("(4) Give me an exclamation: ")
                room = input("(5) Give me a room in a house: ")
                gesture = input("(6) Give me a gesture or action: ")

                print(f"Here is your story {name}")
                print(f"\nYou're on a vacation in {place} enjoying a cup of {drink}. "
                      f"Suddenly the snow comes down so hard you get trapped inside. "
                      f"You hear a noise coming from the {room} and go into the {room}. "
                      f"{exclamation}! You shout, it's a {animal}! "
                      f"You {gesture} towards the {animal} which causes it to stay in the {room} till the storm is over. ")
 

            
        elif choice == "2":   
                neighbor = input("(1) Give me a name: ")
                snack = input("(2) Give the name of a snack you like: ")
                feature = input("(3) Give me an shocking appearance feature (like a horn): ")
                verb = input("(4) Give me a verb ending in -ing: ")
                color = input("(5) Give me a color: ")
                number = input("(6) Give me a number between 3 and 12: ")
                while not number.isdigit() or int(number) < 3 or int(number) > 12:
                     number = input("That is not within 3-12, try again: ")

                print(f"Here is your story {name}")
                print(f"\nYou walk to the corner market near your house to buy {snack}. " 
                      f"On the way you wave to your neighbor {neighbor}, who is {verb} on their lawn. "
                      f"Near the store you find {number} {color} kittens that have {feature}! "
                      f"Such strange kittens cause you to run away back home without your {snack}. ")

        #Create a counter to record how many stories they have created. Display the counter before asking if they would like to play again.
        storyCount += 1
        if storyCount == 1:
             print(f"\nYou have created {storyCount} story.")
        else:
            print(f"\nYou have created {storyCount} stories.")

        #Ask if the user would like to play again (use a loop for this). Validate the user input as being y/n. If they input something that is NOT one of your options, ask the player to try again. 
        playAgain = input("Would you like to play again? (y/n) ").lower()

        while playAgain != "y" and playAgain != "n":
             playAgain = input("Invalid input, please enter y or n: ").lower()

    print("\nThank you for playing!")





if __name__ == "__main__":
    main()