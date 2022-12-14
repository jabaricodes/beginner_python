"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 08.1 - Pig Latin
Date: 11/03/2022

Description:
    This program prompts a user to enter a string and returns that string in the form of pig latin.

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

"""Write new functions below this line (starting with unit 4)."""
def pig(input_string):

    string_pig = "" #sets string output
    input_string = input_string.lower() #changes update to lowercase
    input_string = input_string.split() #splits entities of string
    
    
    for string in input_string:
        first_letter = string[0] #index first letter
        pig_latin = 'ay ' #add pig latin

        string_update = string + first_letter + pig_latin #concates string
        string_pig += string_update[1:]

    string_pig = string_pig[:-1].capitalize() #capitalizes first letter

    return string_pig
def main():
    """Write your mainline logic below this line (then delete this line)."""

    user_string = str(input("Enter a string: "))

    a = pig(user_string)

    print(f"Pig latin: {a}")

  
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
