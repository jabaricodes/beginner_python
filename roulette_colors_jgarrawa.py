"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 02.3 - Roulette Colors
Date: 09/05/2022

Description:
    This program is a Roulette Colors game where the inputted number produces a color on the display

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

    #promts user to enter pocket number

    pockNum = int(input("Please choose a pocket number: "))

    #Initializes which number produces what color in the Roulette Game 

    if pockNum == 0:
        print(f"  Pocket number {pockNum} is green.")
    else:   
        if pockNum <=-1 :
            print("  Invalid Input!") 
        else:
            if pockNum >= 37:
                print("  Invalid Input!") 
            else:
                if (pockNum >= 1 and pockNum <= 10) and pockNum%2 != 0:
                    print(f"  Pocket number {pockNum} is red.")
                elif (pockNum >= 1 and pockNum <= 10) and pockNum%2 == 0:
                    print(f"  Pocket number {pockNum} is black.")
                elif (pockNum >= 11 and pockNum <= 18) and pockNum %2 != 0:
                    print(f"  Pocket number {pockNum} is black.")
                elif (pockNum >= 11 and pockNum <= 18) and pockNum %2 == 0:
                    print(f"  Pocket number {pockNum} is red.")
                else:
                    if pockNum%2 != 0 and (pockNum >= 19 and pockNum <= 28):
                        print(f"  Pocket number {pockNum} is red.")
                    elif pockNum%2 == 0 and (pockNum >= 19 and pockNum <= 28):
                        print(f"  Pocket number {pockNum} is black.")
                    elif pockNum %2 != 0 and (pockNum >= 29 and pockNum <= 36):
                        print(f"  Pocket number {pockNum} is black.")
                    elif (pockNum >= 29 and pockNum <= 36) and pockNum %2 == 0:
                        print(f"  Pocket number {pockNum} is red.")
                                    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
