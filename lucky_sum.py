"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 04.2 - Lucky Sum
Date: 10/02/2022

Description:
    Returns the sum of all the numbers in between the first and second integer
    that aren't divisible by 3


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
def lucky_sum(int1, int2):
    i = int1
    #Variable that will hold the sum (lucky number)
    s = 0
    if(int1 < int2):
        while(int1 <= int2):
            if(int1 % 3):
                s += int1
                int1 += 1
            else:
                int1 += 1
    else:
        while(int2 <= int1):
            if(int2 % 3):
                s += int2
                int2 += 1
            else:
                int2 += 1
    return s

def main():
    #Asks for the first integer value
    int1 = int(input('Enter the first integer: '))
    #Asks for the second integer value
    int2 = int(input('Enter the second integer: '))
    #Runs the function and returns the lucky number
    print(f'The sum of the lucky numbers is {lucky_sum(int1, int2):,d}.')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
