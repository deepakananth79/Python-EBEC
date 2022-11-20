"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 06.1 - Math Quiz
Date: 10/24/2022

Description:
    Returns a random 2 and 3 digit number. Then asks the user to input the sum. If they're wrong, the program will say so and 
    print the correct answer.


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
import random as r

"""Write new functions below this line (starting with unit 4)."""
#Function that randomly generates a number with d digits
def random_number(d):
    return int(r.uniform(10 ** (d-1), 10 ** d))

def main():
    #The 2 randomly generated numbers used for the math quiz
    x = random_number(2)
    y = random_number(3)

    print(f'{x:5}')
    print(f'+ {y:3}')
    print('-----')
    print('=', end = '')
    s = int(input(' '))

    #Statements that check if the user put in the right answer or not
    if((x + y) == s):
        print('Correct -- Good Work!')
    else:
        print(f'Incorrect. The correct answer is {x + y}.')

    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()