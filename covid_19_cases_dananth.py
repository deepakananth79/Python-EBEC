"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 10.3 - covid 19 cases
Date: 11/20/2022

Description:
    Plot the covid 19 cases data from 2020 to 2022 by reading from a txt file that contains the data


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

    dates = []

    with open("2008_Weekly_Gas_Averages.txt") as fo:
        for line in fo:
            dates = line.rstrip('')

    print(dates)    
    x = []
    for date in dates:
         y, m, d = date.split('-')
         dt = datetime.date(int(y),int(m),int(d))
         x.append(dt)

    plt.show()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
