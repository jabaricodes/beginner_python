"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 07.3 - Roll Analysis
Date: 10/25/2022

Description:
    This program simulates the roll frequency of 1,000,000 for two die.

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


"""Write new functions below this line (starting with unit 4)."""
def roll_d6():
    a = rando.randint(1,6) #gives a random integer between 1 and 6
    return a

def get_2d6_rolls(roll2_num):
    list_dice = []
    for _ in range(roll2_num):
        b = roll_d6()
        b_rolls = roll_d6()
        final_roll = b + b_rolls
        list_dice.append(final_roll) #sets a list of possible scores for dice rolls
    return list_dice

def main():
    user_input = 1000000 #sets amount of simulations
    second_roll = get_2d6_rolls(user_input)
    print("Roll  Frequency")
    for n in range(2,13): #sets range of possible dice rolls
        print(f"{n:>3}    {(second_roll.count(n)/user_input):6.2%}") #outputs percentage frequency for each score
    
    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
