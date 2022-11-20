"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 05.2 - square spiral
Date: 10/16/2022

Description:
    A program that creats a square spiral that grows in size for each cycle

Contributors:
    

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
from turtle import *

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(5)


def main():
    """Write your mainline logic below this line (then delete this line)."""
    #Sets the initial direction to 45 degrees northeast
    setheading(45)
    #Loop used in order to repetitively draw the line segments and increase in length each time
    for i in range(29):
        forward(12 * (i+1))
        right(90)
        i += 1


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
