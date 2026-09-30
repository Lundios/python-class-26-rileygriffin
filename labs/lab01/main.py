# Starting file for LAB 1
# Include your course number, student first and last name, and date in the comment header
# CS 31 Lab Activity 1
# September 30, 2026
# Riley Griffin

#2. Display Hello, World!
print("Hello, world!\n")

#3. Add Two Numbers
print("30+56 =" , 30+56) 

#4. Multiply Three Numbers
print("30*2*14 =" , 30*2*14)

#Variables
firstName = "Riley"
lastName  = "Griffin"
major     = "Computer Science"

#8. Display Your Name
print("\nMy name is " + firstName , lastName + ".")

#9. Display Your Major
print("My major is" , major + ".\n")

#10. Ask for num1
num1 = 101
while 0>=num1 or num1>=100:

    num1 = int(input("Enter a number from 0 - 100: "))

    if (0>num1 or num1>100):
         print("That value is not within 0-100.")

print("You entered" , str(num1) +".\n")

#Original Code
#num1 = int(input("Enter a number from 0 - 100: "))

#11. Ask for num2
num2 = 1
while 10>num2 or num2>10000:

    num2 = int(input("Enter a number from 10 - 10000: "))
    
    if (10>num2 or num2>10000):
         print("That value is not within 10-10000.")

print(" You entered" , str(num2) +".\n")

#Original Code
#num2 = int(input("Enter a number from 10 - 10000: "))

#12. Multiply num1 and num2
print(str(num1) + " x " + str(num2) + " = " + str(num1*num2))



#13. Experiment
# force user to input within the number requirements

#num3 = 101
#while 0>num3 or num3>100:
#    num3 = int(input("Enter a number from 0 - 100:"))
#    if (0>num3 or num3>100):
#         print("That value is not within 0-100.")


