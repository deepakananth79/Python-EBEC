"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 00.1 - hello user
Date: 09/04/2022

Description:
    Program prints out the statement "What is your name?" and then takes the input from the user and 
    responds with "Hello [input]! 


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
    #Line where the name variable is assigned
    #Name variable is the input from the user's response to the question
    name = input('What is your name? ')
    print('Hello ' + name + '!')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
