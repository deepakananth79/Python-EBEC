"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 07.2 - number analysis
Date: 10/30/2022

Description:
    Program takes 10 user inputs in order to create a list. Then is calculates various statistics about the 10 numbers entered 
    in by the user.

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
#Function used to create the list of numbers
def get_number_list():
    n = []
    i = 0
    while(i < 10):
        n.append(float(input(f'  number {i+1:2} of 10: ')))
        i += 1
    return n

def main():
    print('Enter 10 numbers:')
    n = get_number_list()
    #Prints highest number
    print(f'Highest number: {max(n):.2f}')
    #Prints lowest number
    print(f'Lowest number: {min(n):.2f}')
    #Prints sum of the list
    print(f'Total: {sum(n):.2f}')
    #Prints average value of the list
    print(f'Average: {sum(n)/len(n):.2f}')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()