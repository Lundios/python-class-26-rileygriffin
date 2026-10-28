# Starting file for LAB 5-1
# Include your course number, student first and last name, and date in the comment header
# CS 31 Lab Activity 5.1
# October 28, 2026
# Riley Griffin

import nameformat

def main():
    #greet user
    print("Hello! welcome to name format program.")
    menuChoice = 0

    #ask for player name
    firstName = input("Please enter your first name: ")
    lastName  = input("Please enter your last name : ")

    #display the menu
    print("* * MENU * *\n\n1 - Say Hello\n\n2 - Output Full Name\n\n3 - Output Last Name, First Name\n\n4 - Read Documentation\n\n5 - Exit")

    #ask user for menuchoice and continue till user decides to exit
    while menuChoice != "5":
         menuChoice =input("\nWhat is your choice? ")
         
         if(menuChoice == "1"):
            nameformat.sayHello(firstName)

         elif(menuChoice == "2"):
             nameformat.fullName(firstName, lastName)

         elif(menuChoice == "3"):
             nameformat.lastNameFirst(firstName, lastName)

         elif(menuChoice == "4"):
            print("Documentation")
            help(nameformat.sayHello)
            help(nameformat.fullName)
            help(nameformat.lastNameFirst)

         elif(menuChoice == "5"):
            print("Thank you, goodbye.")

         else:
            print("Invalid input, try again")

#if started as the main module call the main() function
if __name__ == "__main__":
    main()