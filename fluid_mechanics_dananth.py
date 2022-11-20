"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 02.5 - fluid mechanics
Date: 09/10/2022

Description:
    Calculates the Reynold's Number using the temperature, velocity, and diameter given by the user


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
    #Temperature variable
    t = float(input('Enter the temperature in \u00B0C as 5, 20, or 50: '))
    #Velocity variable
    v = float(input('Enter the velocity of water in the pipe (m/s): '))
    #Diameter variable
    d = float(input('Enter the pipe\'s diameter (m): '))

    #Viscosity variable assignment
    if t == 5:
        x = 0.00000152
    elif t == 20:
        x = 0.000001
    else:
        x = 0.000000554

    #Reynold's Number
    r = float((v*d)/x)

    print(f'At {t}\u00B0C, the Reynolds number for flow at {v} m/s in a {d} m diameter pipe is {r:.2e}.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
