"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 07.1 - multiples of n
Date: 10/30/2022

Description:
    Program takes in a number and a list as arguments from the user. Then the program returns a list with only numbers that
    are multiples of the inputted numbed by the user.


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
def multiples_of(a, b):
    i = 0
    #Loop used in order to check the list for multiples of the number
    while(i < len(b)):
        if(b[i]%a):
            del b[i]
        else:
            i += 1
    return b

def main():
    #Number you want to find multiples of
    a = 13
    #List of numbers that you want to check
    b = [19, 1599, -546, 10, 39, -58, 1, 85, 201, -91, 286, 799, 406]
    print('Original list of numbers:')
    print(f'  {b}')
    print(f'Numbers in the list that are multiples of {a}:')
    print(f'  {multiples_of(a, b)}')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()