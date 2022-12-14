"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 12.1 - Pyword
Date: 11/25/2022

Description:

    This program creates a variation of the game Jotto in Python.

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
import random as rando
from math import *

"""Write new functions below this line (starting with unit 4)."""

def point_to_fame(add_name, add_score):

    file = open('hall_of_fame.txt', 'a')
    file.write((str(add_score) + ", " + str(add_name) + '\n'))
    file.close()

def main_menu(): 

    while True:
        #prints main menu options
         
        print('----- Main Menu -----')
        print('1. New Game')
        print('2. See Hall of Fame')
        print('3. Quit\n')

        #prompts user to input their choice
        menu_choice = input("What would you like to do? ")

        #checks if user input is an intger for the main menu
        if not menu_choice.isdigit():
            print()
            print("Invalid choice. Please try again.")
            print()
            return 0

        #check if user input is not one of the main menu options
        elif int(menu_choice) != 1 and int(menu_choice) != 2 and int(menu_choice) != 3 :
            print()
            print("Invalid choice. Please try again.")
            print()
            return 0
        
        #checks if user inputs "3", prints message and closes program
        elif int(menu_choice) == 3:
            print("Goodbye.")
        
        return int(menu_choice)

#generates random game word       
def pick_game_words(game_words): 

        return rando.choices(game_words, k=3) 

#starts new game as per user input in main menu
def new_game():

    impossible = 64 
    genius = 32
    magnificent = 16
    impressive = 8
    splendid = 4
    great = 2
    phew = 1

    #generates list of words from text as a list
    game_words = [] 
    with open ("words.txt") as wo: 
        for word in wo:
            game_words.append(str(word.strip()))
    word3 = pick_game_words(game_words)
    
    #prompts user to input their name
    player_name = input("Enter your player name: ")
    print("")

    guesses = []
    combine_guess = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    total_score = 0
    #choose new word for each of the 3 rounds in the game
    for n_round in range(1,4):
        combine_guess = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
        ans = word3[n_round-1]
        #print(ans)
        print(f"Round {n_round}:")
        #allows user to have  6 guesses per round
        for n_guess in range(1,7):
            guess = input(f"{n_guess}? ").lower()
            
            #checks if user input is not 5 characters long
            while len(guess) != 5 or not guess.isalpha():
                if len(guess) != 5: 
                        print()
                        print("Invalid guess. Please enter exactly 5 characters.")
                        print()
                
                #checks if user input is not 5 characters long   
                else:
                    if not guess.isalpha():
                        print()
                        print("Invalid guess. Please only enter letters.")
                        print()
                        
                #outputs user's guess in all lower case letters     
                guess = input(f"{n_guess}? ").lower()
            
            #sets list of all letters in the alphabet and combines each index together for game output
            alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            alpha_check = ''.join(alphabet)

            #gives each index a character in game output
            check = []
            
            #checks each guess and determines if letter is in the word, right position or not in the word at all
            for i in range(len(guess)):
                if guess[i] == ans[i]:
                    check.append("!")
                    combine_guess[alphabet.index(guess[i])] = "!"

                elif guess[i] in ans:
                    check.append("?")
                    if combine_guess[alphabet.index(guess[i])] != "!":
                        combine_guess[alphabet.index(guess[i])] = "?"
                else:
                    check.append("X")
                    combine_guess[alphabet.index(guess[i])] = "X"
                continue
                
            #tracks user's guess to know which letters gave been previously used
            guess_tracker = ''.join(combine_guess)
            char_main = ''.join(check)
            guesses.append(char_main)
            #outputs information about user's guesses throughout the rounds
            print(f"   {char_main}     {guess_tracker}")   
            print(f"   {guess}     {alpha_check}")

            #informs that user is out of guesses and outputs the correct random word
            if guess == ans and n_guess == 0:
               print(f"Impossible! You earned {impossible} points this round.")
               total_score += impossible
               break
            elif guess == ans and n_guess == 1:
                print(f"Genius! You earned {genius} points this round.")
                total_score += genius
                break
            elif guess == ans and n_guess == 2:
                print(f"Magnificent! You earned {magnificent} points this round.")
                total_score += magnificent
                break
            elif guess == ans and n_guess == 3:
                print(f"Impressive! You earned {impressive} points this round.")
                total_score += impressive
                break
            elif guess == ans and n_guess == 4:
                print(f"Splendid! You earned {splendid} points this round.")
                total_score += splendid
                break
            elif guess == ans and n_guess == 5:
                print(f"Great! You earned {great} points this round.")
                total_score += great
                break
            elif guess == ans and n_guess == 6:
                print(f"Phew! You earned {phew} points this round.")
                total_score += phew
                break

            #tells the user the answer after they exhaust all their guesses
            elif n_guess == 6:
                print("You ran out of tries.")
                print(f"The word was {ans}.")
        
        #generates round summary of correct and incorrect guesses       
        print(f"Round {n_round} summary:")
            
        for g in guesses:
            print(f"   {g}")
        print()
        guesses = []

    point_to_fame(player_name, total_score)
    check_fame(player_name, total_score)
 
def check_fame(player_name, total_score):
  
    file = open('hall_of_fame.txt','r')
    data = file.readlines()
    file.close

    score_list = []

    file = open('hall_of_fame.txt','r')
    data = file.readlines()
    for lines in data:
        score_list.append(lines.strip().split(", ")[0])

    if len(score_list) < 10:
        print(f"Way to go {player_name}!")
        print(f"You earned a total of {total_score} points and made it into the Hall of Fame!")
        hall_of_fame()
    elif total_score > sorted(score_list, reverse=True)[9]:
        print(f"Way to go {player_name}!")
        print(f"You earned a total of {total_score} points and made it into the Hall of Fame!")
        hall_of_fame()
    else:
        print(f"You earned a total of {total_score} points.")
    
#generates Wordle Hall of Fame for top 10 highest scores
def hall_of_fame(): 

    file = open('hall_of_fame.txt','r')
    raw_data = file.readlines()
    file.close

    clean_data = []

    file = open('hall_of_fame.txt','r')
    raw_data = file.readlines()
    for line in raw_data:

        clean_data.append(line.strip().split(", "))

    #outputs hall of fame list
    print()
    print("--- Hall of Fame ---")
    print(" ## : Score : Player")
    counter_var = 1

    for index in range(1,11):
        high_scores = 0
        high_index = 0
        for index, u in enumerate(clean_data):
            if int(u[0]) > high_scores:
                high_scores = int(u[0])
                high_player = u[1].strip()
                high_index = index
        if len(clean_data) > 0:
            print(f" {counter_var:2} :    {high_scores:2} : {high_player}")
            counter_var += 1
        if len(clean_data) > high_index:
            del clean_data[high_index]
        
    print()   

def main():
    """Write your mainline logic below this line (then delete this line)."""
    
    print("Welcome to PyWord.\n")
    while True:
        q = main_menu()
        if q == 1:
            new_game()
        elif q == 2:
            hall_of_fame()
        if q == 3:
            break

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
