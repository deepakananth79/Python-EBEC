"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 05.4 - mississippi turtles
Date: 10/16/2022

Description:
    A program that uses the turtle.py library in order to draw out the word mississippi turtles

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
    setup(600, 400)
    width(9)
    color("purple")
    speed(0)

def draw_e():
    forward(40)
    setheading(90)
    forward(20)
    pendown()
    setheading(0)
    backward(40)
    forward(40)
    setheading(90)
    circle(20, 300)
    penup()
    setheading(0)
    forward(30)

def draw_i():
    pendown()
    setheading(90)
    forward(30)
    penup()
    forward(20)
    pendown()
    dot(10)
    penup()
    backward(50)
    setheading(0)
    forward(20)


def draw_l():
    pendown()
    setheading(90)
    forward(70)
    penup()
    backward(70)
    setheading(0)
    forward(20)

def draw_M():
    pendown()
    setheading(90)
    forward(50)
    circle(-15, 180)
    setheading(90)
    backward(50)
    forward(50)
    circle(-15,180)
    forward(50)
    penup()
    setheading(0)
    forward(20)

def draw_p():
    setheading(90)
    backward(30)
    pendown()
    forward(70)
    backward(20)
    circle(-15)
    penup()
    setheading(90)
    backward(20)
    setheading(0)
    forward(50)

def draw_r():
    pendown()
    setheading(90)
    forward(40)
    backward(15)
    circle(-15, 180)
    penup()
    setheading(90)
    backward(25)
    setheading(0)
    forward(30)

def draw_s():
    pendown()
    forward(5)
    circle(7.5, 180)
    circle(-7.5, 180)
    forward(5)
    penup()
    setheading(90)
    backward(30)
    setheading(0)
    forward(25)

#Function used to draw the letter t
def draw_t():
    pendown()
    setheading(90)
    forward(70)
    backward(30)
    setheading(0)
    backward(20)
    forward(40)
    penup()
    setheading(90)
    backward(40)
    setheading(0)
    forward(20)

#Function used to draw the letter u
def draw_u():
    setheading(270)
    backward(40)
    pendown()
    forward(20)
    circle(20, 180)
    forward(20)
    backward(40)
    penup()
    setheading(0)
    forward(30)


def main():
    """After these lines, call your letter drawing functions
    as needed to draw the words "Mississippi turtles".
    """
    #Mississippi
    penup()
    goto(-200,0)
    draw_M()
    draw_i()
    draw_s()
    draw_s()
    draw_i()
    draw_s()
    draw_s()
    draw_i()
    draw_p()
    draw_p()
    draw_i()

    #Turtles
    penup()
    goto(-200, -100)
    draw_t()
    draw_u()
    draw_r()
    draw_t()
    draw_l()
    draw_e()
    draw_s()


"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
