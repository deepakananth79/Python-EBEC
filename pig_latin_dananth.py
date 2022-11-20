"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 08.1 - pig latin
Date: 11/05/2022

Description:
    User inputs a string. Then the program returns the same string, but in pig latin


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
#Function used in order to convert string into pig latin
def pig(text):
    split_text = text.split(' ')
    pig_sentence = ' '
    
    #Loop used to go through each word
    for word in split_text:
        if word in '!.%&?':
            pig_sentence = pig_sentence + word
        else:
            pig_word = word[1:] + word[0] + 'ay'
            pig_sentence = pig_sentence + pig_word + ' '
    
    s = pig_sentence.strip(' ')
    return s.capitalize()

def main():
    text = str(input('Enter a string: ')).lower()
    print("Pig latin: " + pig(text))
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()