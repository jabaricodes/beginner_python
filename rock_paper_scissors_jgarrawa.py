"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 06.2 - Rock Paper Scissors
Date: 10/03/2022

Description:
    This program allows the user to play a game of rock paper scissors against the computer.

Contributors:
    Name, login@purdue.edu [repeat for each]

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
import random 
from random import choice

"""Write new functions below this line (starting with unit 4)."""
def get_computer_choice(): #gets computer's random choice
        game = ['rock', 'paper', 'scissors']
        game_rock = choice(game)
        return game_rock

def get_player_choice(): #prompts player to input choice
        player_choice = input("Choose rock, paper, or scissors: ")
        while player_choice != 'rock' and player_choice != 'paper' and player_choice != 'scissors':
            print("You made an invalid choice. Please try again.")
            player_choice = input("Choose rock, paper, or scissors: ")
        
        return player_choice

def get_winner(a, b): #decides game outcome beased on player choices

    if a == 'rock' and b == 'scissors':
        return "computer"
    elif a == 'scissors' and b == 'rock':
        return "player"
    if a == 'paper' and b == 'rock':
        return "computer"
    elif a == 'rock' and b == 'paper':
        return "player"
    if a == 'scissors' and b == 'paper':
        return "computer"
    elif a == 'paper' and b == 'scissors':
        return "player"
    elif a == b: #indicates tied game
        return "tie"
        
def main():
    """Write your mainline logic below this line (then delete this line)."""
    a = get_computer_choice()
    b = get_player_choice()
    c = get_winner(a,b)
    while c == "tie": #starts over if game is a tie
        print(f"  The computer chose {a}, and you chose {b}.")
        print("  It's a tie. Starting over.\n")
        a = get_computer_choice()
        b = get_player_choice()
        c = get_winner(a,b)

    if c == "player":
        print(f"  The computer chose {a}, and you chose {b}.")
        print(f"  {b} beats {a}")
        print("  You won the game!")
        print("Thanks for playing.")
    elif c == "computer":
        print(f"  The computer chose {a}, and you chose {b}.")
        print(f"  {a} beats {b}")
        print("  You lost.  Better luck next time.")
        print("Thanks for playing.")
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
