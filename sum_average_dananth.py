"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 03.2 - sum average
Date: 09/14/2022

Description:
    User inputs numbers and the code returns the sum and average of 
    the inputted numbers


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


def main():
    i = 0
    #Sum variable
    s = 0
    #Number of iterations (numbers inputted)
    c = 0
    #Average variable
    a = 0

    while(i < 1):
        #Takes in the user's inputted number
        n = float(input('Enter a non-negative number (negative to quit): '))
        if(n <  0):
            #Ends the loop if a negative is entered
            i = 1
        else:
            #Calculates the sum and average
            s += n
            c += 1
            i = 0
            a = s/c

    #Prints out the results for sum and average
    if(c > 0):
        print(f'  You entered {c} numbers.')
        print(f'  Their sum is {s:.3f} and their average is {a:.3f}.')
    else:
        print(f'  You didn\'t enter any numbers.')
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()