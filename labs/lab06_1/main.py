# Starting file for LAB 6-1
# Include your course number, student first and last name, and date in the comment header
# CS 31 Lab Activity 6.1
# November 12, 2026
# Riley Griffin

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")
def get_scores():
    scoreList = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return scoreList
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scoreList.append(score)
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scoreList):
    #total
    scoreTotal = 0
    for score in scoreList:
        scoreTotal += score

    #Number of Scores
    count = len(scoreList)

    # calculate average score
    average = scoreTotal / count
                
    #Low Score:  
    low = min(scoreList)

    #High Score: 
    high = max(scoreList)

    #Median Score:
    sortedScores = sorted(scoreList)
    middle = count // 2
    if count % 2 == 1:
        median = sortedScores[middle]
    else:
        median = (sortedScores[middle - 1] + sortedScores[middle + 1]) / 2


    # format and display the result
    print()
    print("Total:             ", scoreTotal)
    print("Number of Scores:  ", count)
    print("Average Score:     ", average)
    print("Low Score:         ", low)
    print("High Score:        ", high) 
    print("Median Score:      ", median)

def main():
    display_welcome()
    scoreList = get_scores()
    process_scores(scoreList)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

