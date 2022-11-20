"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 09.1 - capital quiz
Date: 11/13/2022

Description:
    Program runs a 10 question capitals quiz that tells thwe user
    whether they have inputted the correct or incorrect capital of
    the given state


Contributors:
    Deepak, dananth@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""

# this function gets the state and capital pairs from an input file and adds them to a dictionary
def get_state_data(): 

    # intiialize empty dictionary for state and capital pairings
    stateCapitals_Dictionary = {}

    with open('state_capitals.txt') as fo: 
        for list in fo:
            QandA = list.split(",") 
            oldKey = QandA[1] 
            key = oldKey[:-1].lstrip() 
            value = QandA[0] 
            stateCapitals_Dictionary[key] = value 
            

    return stateCapitals_Dictionary

def main():

    count = 0    
    totalCorrect = 0    
    questionList = get_state_data().items()
    # boolean stores whether or not program should exit
    exit = False; 

    while questionList:
        incorrectList = []  

        if exit == True:
            break
        for state,capital in questionList:
            userAnswer0 = input(f"What is the capital of {state} (enter 0 to quit)? ")
            userAnswer = userAnswer0.title()

            if userAnswer == '0': 
                exit = True
                break

            elif(userAnswer == capital):
                print("  That is correct!")
                totalCorrect+=1 
                count+=1   
            else:
                print("  That is incorrect.")
                print(f"  The capital of {state}"+f" is {capital}.")
                count+=1
                quizAgain = (state,capital)
                #adds temp item to the end of list
                incorrectList.append(quizAgain) 
        questionList = incorrectList


    print(f"You answered {totalCorrect}"+f" out of {count} questions correctly.")

if __name__ == '__main__':
    main()