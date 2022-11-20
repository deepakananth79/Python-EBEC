"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 04.3 - Avg Grade
Date: 10/03/2022

Description:
    Asks the user to enter a valid score 5 times, then the program should
    display a letter grade for each input. Then it calculates the 
    average grade ans corresponding grade.


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

#Function that determines if the score is valid or not and runs the loop
def get_valid_score():
    #Variable used to keep count of the number of iterations
    i = 0
    s = 0
    while(i < 5):
        g = float(input('Enter a score: '))
        if((g < 0) | (g > 100)):
            print('  Invalid Input. Please try again.')
        else:
            s += g
            print(f'  The letter grade for {g:.1f} is {determine_grade(g)}.')
            i += 1
    calc_average(s)

#Function that Calculates the Average Grade and prints out the final results
def calc_average(s):
    #Variable that stores the average value
    a = s/5
    print('')
    print('Results:')
    print(f'  The average score is {a:.2f}.')
    print(f'  The letter grade for {a:.2f} is {determine_grade(a)}.')

#Letter Grade Function
def determine_grade(g):
    if(g < 64):
        l = 'F'
    elif(g < 73):
        l = 'D'
    elif(g < 82):
        l = 'C'
    elif(g < 92):
        l = 'B'
    else:
        l = 'A'
    return l

def main():
    get_valid_score()
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()