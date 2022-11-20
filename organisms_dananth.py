"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 03.4 - Organisms
Date: 09/23/2022

Description:
    User inputs a starting population, rate of growth, and length in days.
    Program returns the new population each day.


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

    #Starting population variable
    s = float(input('Starting population, in thousands: '))
    #Rate of population growth variable
    r = 1 + (float(input('Average daily increase, in percent: ')))/100
    #Variable storing days organism's population is growing for 
    d = float(input('Number of days to multiply: '))

    i = 0

    print('Day   Approx. Pop')
    while(i <= d):
        print(format(i, '3d'), end = '')
        #Approx Population Variable
        if(i != 0):
            s = s * r
        print(f'   {s:11,.3f}')
        i += 1

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
