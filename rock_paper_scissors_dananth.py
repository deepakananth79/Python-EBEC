"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 06.2 - rock paper scissors
Date: 10/24/2022

Description:
    Computer plays rock, paper, scissors against the user. If there is a tie, the game is played until there is no tie


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
#Function that determines the computer's choice for the game
def get_computer_choice():
    return r.choice(['rock', 'paper', 'scissors'])

#Function that gets the player's choice for the game
def get_player_choice():
    x = input('Choose rock, paper, or scissors: ')
    if ((x == 'paper') | (x == 'scissors') | (x == 'rock')):
        return x
    else:
        print('You made an invalid choice. Please try again.')
        get_player_choice()

#Function used to determine the winner of the game
def get_winner(c, u):
    if((c == 'rock') & (u == 'paper')):
        print('  paper beats rock')
        return('player')
    elif((c == 'rock') & (u == 'scissors')):
        print('  rock beats scissors')
        return('computer')
    elif((c == 'paper') & (u == 'rock')):
        print('  paper beats rock')
        return('computer')
    elif((c == 'paper') & (u == 'scissors')):
        print('  scissors beats paper')
        return('player')
    elif((c == 'scissors') & (u == 'paper')):
        print('  scissors beats paper')
        return('computer')
    elif((c == 'scissors') & (u == 'rock')):
        print('  rock beats scissors')
        return('player')
    else:
        print(f'  It\'s a tie. Starting over.')
        print('')
        return ('tie')

def main():
        c = get_computer_choice()
        u = get_player_choice()
        print(f'  The computer chose {c}, and you chose {u}.')
        w = get_winner(c, u)
        if(w == 'tie'):
            main()
        else:
            if(w == 'computer'):
                print('  You lost.  Better luck next time.')
            else:
                print('  You won the game!')
            print('Thanks for playing.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()