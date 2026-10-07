# Starting file for LAB 2
# Include your course number, student first and last name, and date in the comment header
# CS 31 Lab Activity 2
# October 7, 2026
# Riley Griffin

import random

#define varibles
correctAnswerText = "Correct! heres the next question\n"
incorrectAnswerText = "Wrong! the answer was: "
correctAnswerCount = 0
username = ""
takeQuiz = ""
buffer = ("*" * 20)
userAnswer = 0

#welcome
print(buffer + "\n     Math Quiz\n" + buffer)

#user name greeting
username = input("Hello! What is your name? ")
print("\nWelcome", username)

#ask user to take quiz
takeQuiz = input("\nwould you like to take the math quiz? y/n ")

#create random numbers for quiz
randomNumberOne = random.randint(5, 10)
randomNumberTwo = random.randint(5, 12)
randomNumberThree = random.randint(100, 500)
randomNumberFour = random.randint(1000, 1100)

#generate correct answers to questions
answerOne   = randomNumberFour + randomNumberThree
answerTwo   = randomNumberTwo + randomNumberOne
answerThree = randomNumberThree - randomNumberOne
answerFour  = randomNumberOne * randomNumberTwo
answerFive  = randomNumberOne**2

#yes to taking quiz
if takeQuiz.lower() == "y":

 #reset correct answer count
    correctAnswerCount = 0

#question 1
    userAnswer = int(input(f"\nQuestion 1: what is {randomNumberFour} + {randomNumberThree}: "))

#check answer
    if userAnswer == answerOne:
        correctAnswerCount += 1
        print(correctAnswerText)
    else:
        print(incorrectAnswerText+str(answerOne))

#question 2
    userAnswer = int(input(f"\nQuestion 2: what is {randomNumberTwo} + {randomNumberOne}: "))

#check answer
    if userAnswer == answerTwo:
        correctAnswerCount += 1
        print(correctAnswerText)
    else:
        print(incorrectAnswerText+str(answerTwo))

#question 3
    userAnswer = int(input(f"\nQuestion 3: what is {randomNumberThree} - {randomNumberOne}: "))

#check answer
    if userAnswer == answerThree:
        correctAnswerCount += 1
        print(correctAnswerText)
    else:
        print(incorrectAnswerText+str(answerThree))

#question 4
    userAnswer = int(input(f"\nQuestion 4: what is {randomNumberOne} x {randomNumberTwo}: "))

#check answer
    if userAnswer == answerFour:
        correctAnswerCount += 1
        print(correctAnswerText)
    else:
        print(incorrectAnswerText+str(answerFour))

#question 5
    userAnswer = int(input(f"\nQuestion 5: what is {randomNumberOne}^2: "))

#check answer
    if userAnswer == answerFive:
        correctAnswerCount += 1
        print(correctAnswerText)
    else:
        print(incorrectAnswerText+str(answerFive))

#Score result
    print(f"\nyour final score is {correctAnswerCount}/5")

    if correctAnswerCount == 5:
        print("Perfect score! Good job.")
    elif correctAnswerCount == 4:
        print("Good job! Almost perfect.")
    elif correctAnswerCount == 2 or correctAnswerCount == 3:
         print("That was an attempt! keep trying.")
    else:
        print("Bad job.")

 #goodbye
    print(f"\nThank you {username} for taking this math quiz. Goodbye.")

# answer no to taking quiz
elif takeQuiz.lower() == "n": 
    print("See you later", username)

# bad answer to taking quiz
else: 
    print("Invalid input, try again")