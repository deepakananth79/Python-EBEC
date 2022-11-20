"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: road trip - Assignment Name
Date: 09/08/2022

Description:
    Program prints out the cost of a road trip after the input from the user 


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

    print('Road trip fuel cost estimator:')

    #Distance variable which stores the destination's distance in miles
    d = float(input('  How far away is your destination (miles)? '))
    #Price variable which stores the average price of gas
    p = float(input('  What is the average price of gas (dollars per gallon)? '))
    #MPG variable which stores the fuel efficiency of the vehicle
    mpg = float(input('  What is the fuel efficiency of your vehicle (mpg)? '))

    #Equation that calculates the total cost of the road trip using d, p, mpg
    c = int((2*d) * p // mpg)
    print()
    print('The fuel cost for this trip is approximately $' + str(c) + '.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
