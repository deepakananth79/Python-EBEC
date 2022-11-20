"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 04.5 - Prime List
Date: 10/03/2022

Description:
    User inputs a number, and the program returns all the prime numbers
    up to that inputted number


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
#Function used to determine if a number is prime
def is_prime(x):
    #Variable used to keep loop to check if divisible by anything less than 100
    i = 2
    #Used as 1 is not considered a prime number
    if(x != -1):
        if(((x == 1) | (x == 0))):
            return False
        while((i < 10000) & (i < x)):
            if(x%i):
                i += 1
            else:
                return False
        return True


def main():
    #Variable used to iterate the is_prime function multiple times
    i = 0
    #Variable used in order to print commas for the list of numbers
    w = 0
    x = int(input('Enter a positive integer: '))
    print(f'The primes up to {x} are: ', end = '')
    #Loop used to print all the prime numbers
    while(i <= x):
        if(is_prime(i)):
            if(w > 0):
                print(f', {i}', end = '')
            else:
                print(f'{i}', end = '')
                w = 1
            i += 1
        else:
            i += 1
    print('')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()