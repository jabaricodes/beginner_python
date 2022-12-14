"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 03.2 - Sum Average
Date: 09/15/2022

Description:
    This program prompts a user to enter a series of positive numbers before quitting when a negative number is entered

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


"""Write new functions below this line (starting with unit 4)."""


def main():
    """Write your mainline logic below this line (then delete this line)."""
#prompts user to enter non-negative number
    nonNegnum = ("Enter a non-negative number (negative to quit): ")
    count, total = 0, 0
    sumAvg = float(input(nonNegnum))

    while sumAvg >= 0:
        count += 1 #counts all valid numbers entered
        total += sumAvg #adds up all valid numbers entered
        sumAvg = float(input(nonNegnum))
    if count > 0:  
        print(f"  You entered {count} numbers.")
        print(f"  Their sum is {total:.3f} and their average is {total/count:.3f}.") #calculates average of all valid numbers
    else:
        print("  You didn't enter any numbers.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
