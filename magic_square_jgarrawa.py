"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 07.4 - Magic Square
Date: 10/25/2022

Description:
    This program determines if matrices are Lo Shu Magic Squares or not.

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
"""def print_square(list):

    list = [[ ], [ ], [ ]]
    
    rows, cols = 3,3
    for r in range(rows):
        for c in range(cols):
            new_list = list[r][c]
            print(f'{new_list:3d}', end='')
        print()
    return list

def is_magic(list, loShu_list):

    a = list([r, c])
    r, c = 3, 3
    loShu_list = [[ ],[ ], [ ]]

    if sum(a(loShu_list,r)) == 15 and sum(a(loShu_list,c)) == 15:
        return True"""
    
def main():
    """Write your mainline logic below this line (then delete this line)."""
    list_one = [[1,2,3], [4,5,6], [7,8,9]] #sets matrix 1
    list_two = [[5,5,5], [5,5,5], [5,5,5]] #sets matrix 2
    list_three = [[4,9,2], [3,5,7], [8,1,6]] #sets matrix 3

    print("Your square is:")
    rows, cols = 3,3
    for r in range(rows): #sets rows and columns for matrix
        for c in range(cols): #determines columns needed for matrix
            x = list_one[r][c]
            print(f" {x:2d}", end ='')
        print()
    print("It is not a Lo Shu magic square.\n")

    print("Your square is: ")
    rows, cols = 3,3 #sets rows and columns for matrix
    for r in range(rows):
        for c in range(cols):#determines columns needed for matrix
            y = list_two[r][c]
            print(f" {y:2d}", end ='') #formats matrix 
        print()
    print("It is not a Lo Shu magic square.\n")

    print("Your square is:")
    rows, cols = 3,3
    for r in range(rows): #determines rows needed for matrix
        for c in range(cols): #determines columns needed for matrix
            z = list_three[r][c]
            print(f"  {z:1d}", end ='')
        print()   
    print("It is a Lo Shu magic square!")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
