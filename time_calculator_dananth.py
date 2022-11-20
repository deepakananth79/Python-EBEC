"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 02.4 - time calculator
Date: 09/10/2022

Description:
    Takes the input that the user put (seconds) and then displays the time
    in days, hours, minutes, and seconds.


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
    #user input time
    t = int(input('Please enter a time in seconds: '))

    if(t < 60):
        print(f'  {t:,} seconds is less than one minute.')
    else:
        #days
        d = int(t/86400)
        #hours
        h = int((t%86400)/3600)
        #minutes
        m = int((t%3600)/60)
        #seconds leftover
        s = int(t%60)

        print(f'  {t:,} seconds equals ', end = '')
        #Prints out the days calculated
        if d:
            print(f'{d} day(s)', end = '')
        #Prints out the hours calculated
        if h:
            if d:
                if (m or s):
                    print(', ', end = '')
                else:
                    print(' and ', end = '')
            print(f'{h} hour(s)', end = '')
        #Prints out the minutes calculated
        if m:
            if d or h:
                if s:
                    print(', ', end = '')
                else:
                    print(' and ', end = '')
            print(f'{m} minute(s)', end = '')
        #Prints out the seconds calculated
        if s:
            if d or h or m:
                print(' and ', end = '')
            print(f'{s} second(s)', end = '')
        print('.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
