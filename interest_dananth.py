"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 01.2 - interest
Date: 09/08/2022

Description:
    A program that calculates the balance of a bank account with
    Principal, interest rate, years, and # of times compounded 
    yearly


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
    print('Enter the following parameters.')
    #Initial Deposit (Principal)
    P = float(input('  The initial deposit? '))
    #Annual Interest Rate in Percent
    r = float(input('  The annual interest rate in percent? '))/100
    #Number of years the account earns interest
    t = float(input('  The number of years the account earn interest? '))
    #Number of times the interest is compounded annually 
    n = float(input('  The number of times interest is compounded each year: '))

    #Equation that calculates the balance of the account (future value)
    fv = P * (1 + r/n)**(n * t)
    print('The balance of this account will be $' + str(format(fv, ',.2f')) + ' after ' + str(t) + ' years.')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
