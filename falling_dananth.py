"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 04.1 - Falling
Date: 10/02/2022

Description:
    Calculates the falling distance of an object using a function
    and a loop in order to iterate multiple times


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
#Variable for gravitatioal constant
g = 8.87

#Function that uses time as a parameter in order to calculate distance
def falling_dist(t):
    #Calculation used to get the distance
    d = 0.5 * g * (t**2)
    return d

def main():
    i = 5
    print('Time (s)  Distance (m)')
    print('----------------------')
    while(i < 51):
        print(f'{i:8}{falling_dist(i):14.1f}')
        i += 5

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
