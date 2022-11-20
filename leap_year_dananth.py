"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 02.1 - Leap Year
Date: 09/09/2022

Description:
    Checks whether the inputted year by the user is a leap year or not


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


from operator import truediv


def main():
    #User inputted year that they want to check
    y = int(input('Enter a year: '))
    #Variable that tells program if it is a loop year or not
    x = False 

    #Checks if year is divisible by 100, then divisible by 400
    if((y % 100) == 0):
        if(y % 400):
            x = False
        else:
            x = True

    #Checks if year is divisible by 4 if not divisible by 100
    else:
        if(y % 4):
            x = False
        else:
            x = True
    
    #Prints out if the year was a leap year
    if(x == True):
        print('The year ' + str(y) + ' is a leap year.')
        print('February of ' + str(y) + ' has 29 days.')
    
    #Prints out if the year wasn't a leap year
    else:
        print('The year ' + str(y) + ' is not a leap year.')
        print('February of ' + str(y) + ' has 28 days.')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()