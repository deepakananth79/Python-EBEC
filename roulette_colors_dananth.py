"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 02.3 - Roulette Colors
Date: 09/10/2022

Description:
    Tells the user the color of the pocket that the user chose


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
    #Pocket number that the user chose
    p = int(input('Please choose a pocket number: '))
    
    if(p == 0):
        print('  Pocket number 0 is green.')
    elif(1 <= p <= 10):
        if(p % 2):
            print('  Pocket number ' + str(p) + ' is red.')
        else:
            print('  Pocket number ' + str(p) + ' is black.')
    elif(11 <= p <= 18):
        if(p % 2):
            print('  Pocket number ' + str(p) + ' is black.')
        else:
            print('  Pocket number ' + str(p) + ' is red.')
    elif(19 <= p <= 28):
        if(p % 2):
            print('  Pocket number ' + str(p) + ' is red.')
        else:
            print('  Pocket number ' + str(p) + ' is black.')
    elif(29 <= p <= 36):
        if(p % 2):
            print('  Pocket number ' + str(p) + ' is black.')
        else:
            print('  Pocket number ' + str(p) + ' is red.')
    else:
        print('  Invalid Input!')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()