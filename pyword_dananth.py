"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 12.1 - pyword
Date: 12/12/2022

Description:
    Program that runs a game similar to wordle in the terminal. Also has a "hall of fame" txt file that 
    stores the highest scores from the game.


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

#Function that picks the words randomly, argument is a list of all the words
def pick_game_words(words):
    #List that stores the words from the word.txt file that were picked randomly
    secret_words = []
    i = 0
    #Loop used to randomly select 3 words to use for the game
    while(i < 3):
        secret_words.append(words[r.randint(0, len(words) - 1)])
        i += 1
    return secret_words

#Function that displays the main menu screen and redirects the user accordingly based off of the user input
def main_menu():
    print('----- Main Menu -----\n1. New Game\n2. See Hall of Fame\n3. Quit\n')
    user_input = input('What would you like to do? ')
    if(user_input == 1):
        #List used to store all of the words from the word.txt file
        words = []
        with open("words.txt") as fo:
            #For loop used to move each line from the word.txt file into a list
            for line in fo: 
                words.append(str(line.rstrip()))
        pick_game_words(words)
    elif(user_input == '2'):
        print('\n--- Hall of Fame ---\n ## : Score : Player')
        load_hall_of_fame()
        for player,score in load_hall_of_fame().items():
            print(f'{i:3} : {score:5s} : {player:s}')
        print('')
        main_menu()
    elif(user_input == '3'):
        print('Goodbye.')
    else:
        print('\nInvalid choice. Please try again.\n')
        main_menu()

#Function that returns the data from the hall_of_fame.txt file as a dictionary
def load_hall_of_fame():

    hall_of_fame_dict = {}

    #Opens the hall_of_fame.txt file and splits up the data from the file into a dictionary
    with open("hall_of_fame.txt") as fo:
        for i in fo:
            QandA = i.split(",") 
            oldKey = QandA[1] 
            key = oldKey[:-1].lstrip() 
            value = QandA[0] 
            hall_of_fame_dict[key] = value 
    
    return hall_of_fame_dict


#Function that runs the game itself
def game():
    player_name = input('Enter your player name: ')


def main():
    print('Welcome to PyWord.\n')
    main_menu()
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
