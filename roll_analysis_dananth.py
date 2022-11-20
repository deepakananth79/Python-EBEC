"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 07.3 - roll analysis
Date: 10/31/2022

Description:
    Simulates 1 million dice rolls with 2 dice and displays the distribution of each dice roll as a percentage


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
#Function that simiulates a single dice roll
def roll_d6():
    return r.randint(1,6)

#Function used to simulate 2 dice being rolled and then being added to a list 
def get_2d6_rolls(n):
    i = 0
    j = []
    while(i < n):
        j.append(roll_d6() + roll_d6())
        i += 1
    return j

def main():
    print('Roll  Frequency')
    j = get_2d6_rolls(1000000)
    z = 2
    #Loop used to print out the percent distribution of the sum of the 2 rolls
    while(z < 13):
        print(f'{z:3}  {(j.count(z)/len(j))*100:7.2f}%')
        z += 1

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
