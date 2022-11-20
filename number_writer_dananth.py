"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 8.4 - number writer
Date: 11/05/2022

Description:
    Asks user for how many numbers it should generate and then writes
    the random numbers to a text file


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
def main():

    #Asks for amount of random numbers to be generated in new file
    amountOfNums = int(input("How many numbers would you like? "))

    #Creates a list for random numbers to be stored in
    numberList = []

    #For loop goes through and stores requested amount of random numbers in list
    for i in range(amountOfNums):
        number = r.randrange(1019,1216) 
        #Number appended to list
        numberList.append(f"{number}\n")
        i+=1

    with open("random_numbers.txt", 'w') as fo: 
        fo.writelines(numberList) 

    

if __name__ == '__main__':
    main()