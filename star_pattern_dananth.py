"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 05.3 - star pattern
Date: 10/16/2022

Description:
    A program that draws a star using a loop in order to make a star with the number of points that the user wants

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
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()


def main():
    """Write your mainline logic below this line (then delete this line)."""
    p = int(input('Enter the number of points you want on the star '))
    #Inside angle measure
    A = 360/p
    #Outside angle measure
    B = 2 * A
    #Function used to set the outline and fill color
    color('Black', 'Red')
    begin_fill()
    setheading(270 + A)
    #Loop used to draw the star
    for i in range(p):
        forward(60)
        right(A)
        backward(60)
        left(B)
    end_fill()    

"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
