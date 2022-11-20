"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 10.2 - gas prices
Date: 11/20/2022

Description:
    Reads the data from a seperate text file, and displays the data in a graphical form


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

"""Write new functions below this line (starting with unit 4)."""


def main():

    #Variable initialization
    #Stores gas averages from input file
    gasAverage = [] 

    #Context manager created for file i/o
    with open("2008_Weekly_Gas_Averages.txt") as fo:
        for line in fo:
            #Adds each line from file at the end of the "gasAverage" list
            gasAverage.append(float(line.rstrip())) 

    # Plotting specifications
     #Initialize plot
    fig, ax = plt.subplots()  
    ax.set_title("2008 Weekly Gas Prices") 
    ax.set_xlabel("Weeks (by number)")
    ax.set_ylabel("Average Price (dollars/gallon)") 
    ax.set_xticks([10,20,30,40,50]) 
    ax.set_xlim(1,52) 
    ax.set_ylim(1.5,4.25) 
    ax.grid() 
    ax.plot(gasAverage) 

    plt.show()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
