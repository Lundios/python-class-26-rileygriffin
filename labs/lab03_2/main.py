# Starting file for LAB 3-2
# Include your course number, student first and last name, and date in the comment header
# CS 31 Lab Activity 3.2
# October 15, 2026
# Riley Griffin
# display a welcome message
print("The Test Scores application")
print()

another_set = "y"
while another_set.lower() == "y":

    print("Enter test scores")
    print("Enter 'end' to end input")
    print("======================")

# initialize variables
    counter = 0
    score_total = 0
    test_score = 0
    user_entry = ""

    while user_entry != "end":
        user_entry = input("Enter test score: ")

        if user_entry == "end":
            break
        else:
            test_score = int(user_entry)
            if test_score >= 0 and test_score <= 100:
             score_total += test_score
             counter += 1
            else: 
                print(f"Test score must be from 0 through 100 Try again.")

# calculate average score
    average_score = round(score_total / counter)
                
# format and display the result
    print("======================")
    print(f"Total Score: {score_total}"
      f"\nAverage Score: {average_score}")

    print()
    another_set = input("Enter another set of test scores (y/n)? ")

print()
print("Bye!")

