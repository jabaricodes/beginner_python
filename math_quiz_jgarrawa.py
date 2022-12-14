"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 06.1 - Math Quiz
Date: 10/03/2022

Description:
    This function returns a random 2 and 3 digit number and prompts the user to add them together and then outputs whether the calculation is correct or incorrect.

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
def random_number(a):
    
    num = rando.randint(10**(a-1),(10**a)-1) #function to choose random numbers
   
    return num

def main():
    """Write your mainline logic below this line (then delete this line)."""
    two_digit = random_number(2) #chooses random 2 number for first line of calculation
    three_digit = random_number(3) #chooses random 3 number for first line of calculation
    print(f"   {two_digit}")
    print(f"+ {three_digit}")
    print("-----")   
    user_input = int(input("= "))
    correct_answer = two_digit + three_digit
    if user_input == correct_answer:
        print("Correct -- Good Work!") #outputs good work if it is correct
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.") #outputs incorrect if computation is wrong
        
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
