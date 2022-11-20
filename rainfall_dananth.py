"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 03.3 - Rainfall
Date: 09/15/2022

Description:
    User inputs number of months, and then the program calculates the rain average and sum over the time period


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
    #Variable that stores the time period
    y = int(input('Enter the number of years: '))
    #List of the months
    m = ['Jan.','Feb.','Mar.','Apr.','May.','Jun.','Jul.','Aug.','Sep.','Oct.','Nov.','Dec.']
    i = 0
    s = 0
    j = 0

    if(y < 1):
        print('Invalid input; years must be greater than 0.')

    else:
        while(i <= y):
            while(j < (12*y)):
                if((j%12) == 0):
                    print(f'  For year No. {int(j/12)+1}')
                #Stores user input data for each month (one at a time)
                x = float(input(f'    Enter the rainfall for {m[i%12]}: ')) 
                if(x >= 0):  
                    #The variable that calculates the sum
                    j += 1 
                    s += x
                    i += 1
                else:
                    print('    Invalid input; rainfall cannot be negative.')

            #Variable storing average monthly rainfall
            a = s/(12*y)

    if(y > 0):
        print(f'There are {12 * y} months.')
        print(f'The total rainfall was {s:.2f} inches.')
        print(f'The monthly average rainfall was {a:.2f} inches.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()