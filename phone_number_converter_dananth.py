"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 08.2 - phone number converter
Date: 11/05/2022

Description:
    User inputs a phone number with words and the program returns a phone number with only numbers


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
#Function used in order to convert phone number with string into number with only numbers
def convert_number(phoneNum):

    newString = phoneNum.upper() 

    #Used to convert letters into numbers
    newString = newString.replace('A', '2')
    newString = newString.replace('B', '2')
    newString = newString.replace('C', '2')
    newString = newString.replace('D', '3')
    newString = newString.replace('E', '3')
    newString = newString.replace('F', '3')
    newString = newString.replace('G', '4')
    newString = newString.replace('H', '4')
    newString = newString.replace('I', '4')
    newString = newString.replace('J', '5')
    newString = newString.replace('K', '5')
    newString = newString.replace('L', '5')
    newString = newString.replace('M', '6')
    newString = newString.replace('N', '6')
    newString = newString.replace('O', '6')
    newString = newString.replace('P', '7')
    newString = newString.replace('Q', '7')
    newString = newString.replace('R', '7')
    newString = newString.replace('S', '7')
    newString = newString.replace('T', '8')
    newString = newString.replace('U', '8')
    newString = newString.replace('V', '8')
    newString = newString.replace('W', '9')
    newString = newString.replace('X', '9')
    newString = newString.replace('Y', '9')
    newString = newString.replace('Z', '9')

    return newString


def main():
    phoneNum = input("Enter a telephone number: ") 
    print("The phone number is " f"{convert_number(phoneNum)}") 

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()