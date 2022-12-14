"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 07.1 - Multiples of N
Date: 10/25/2022

Description:
    This program sets a function that accepts and integer as its first argument and a list of integers as its second argument. When called this function will return a list of numbers in the second argument that are multiples of the number in the first argument.

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
from random import *

"""Write new functions below this line (starting with unit 4)."""
def multiples_of(first_int, second_int):
    
    multiples_int = [] #sets list

    for i in second_int:
        if (i % first_int) == 0:
            multiples_int.extend([i]) #iterates numbers in list divisble by first integer input
    
    
    return multiples_int
     
def main():
    """Write your mainline logic below this line (then delete this line)."""
    multiple = 13 #sets items in list to be dividible by this number
    original = [19, 1599, -546, 10, 39, -58, 1, 85, 201, -91, 286, 799, 406] # sets original list

    print("Original list of numbers:")
    a = multiples_of(multiple, original)
    print(f"  { original}") #prints original list

    print(f"Numbers in the list that are multiples of {multiple}:")
    print(f"  {a}") #prints lists of multiples

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
