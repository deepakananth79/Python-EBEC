"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 10.4 - sin cos
Date: 11/20/2022

Description: 
    Draws a plot of a sine and cosine graph from 0 to 2pi
    

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
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np

"""Write new functions below this line (starting with unit 4)."""


def main():

    # plot initialization
    fig, ax = plt.subplots()

    # variable declaration
    xrange = np.arange(0,2*np.pi,0.01) # specifies the range for the x spine as 0 - 2pi with an increment of 0.1 radians
    sinValues = np.sin(xrange)
    cosineValues = np.cos(xrange)

    # plot manipulation
    plt.plot(xrange,sinValues, color = 'red')
    plt.plot(xrange,cosineValues, color = 'blue')
    ax.set_yticks([-1,1]) # specifies ticks for the y axis
    ax.set_xticks([1.6,3.2,4.7,6.3]) # specifies ticks for the x axis
    ax.set_xlim(0,6.5)
    xlabels = ['$\\pi/2$', '$\\pi$', '$3\\pi/2$', '$2\\pi$']
    ax.set_xticklabels(xlabels)


    # spine (axis + border) manipulatin
    for spine in ['top','right']:
        ax.spines[spine].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_position('zero')

    plt.show()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
