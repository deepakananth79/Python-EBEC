"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 01.3 - cookie recipe
Date: 09/08/2022

Description:
    Asks user for the number of cookies they wannt to make. Returns
    the amount of butter, sugar, and flour needed to make that many
    cookies


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
    #Number of cookies the user wants to make
    x = int(input('How many cookies do you want to make? '))
    #Cups of butter needed
    b = 1.25 * (x/48)
    #Cups of sugar needed
    s = 1.5 * (x/48)
    #Cups of flour needed
    f = 2.5 * (x/48)
    print('To make ' + format(x, ',') + ' cookies, you will need:')
    print(format(b, '10,.2f') + ' cups of butter')
    print(format(s, '10,.2f') + ' cups of sugar')
    print(format(f, '10,.2f') + ' cups of flour')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()