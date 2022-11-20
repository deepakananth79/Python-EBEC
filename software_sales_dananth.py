"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 02.2 - Software Sales
Date: 09/09/2022

Description:
    User inputs how many packages they want to purchase. The program
    either returns "invalid input", "no discount applied", or the 
    appropriate discount that is applied. Then the total price of the 
    packages is displayed after.


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
    #Number of packages
    p = int(input('How many packages will be purchased: '))
    #Discount value
    d = 0.0

    if(p <= 0):
        print('  Invalid Input!')
    elif(1 <= p <= 3):
        print('  No discount applied.')
    elif(4 <= p <= 39):
        print('  10%' + ' discount applied.')
        d = 0.1
    elif(40 <= p <= 199):
        print('  15%' + ' discount applied.')
        d = 0.15
    elif(200 <= p <= 999):
        print('  30%' + ' discount applied.')
        d = 0.3
    elif(p >= 1000):
        print('  42%' + ' discount applied.')
        d = 0.42

    #Total Cost
    c = (p * 880)
    #Total Cost - Discount
    cd = c - (c * d)

    if(p > 0):
        print('  The total price to purchase ' + str(p) + ' packages is $' + format(cd, ',.2f') + '.')



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
