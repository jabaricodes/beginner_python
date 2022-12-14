"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 04.2 - Lucky Sum
Date: 9/19/2022

Description:
    This program returns the sum of the numbers not divisible by 3 betweem the user's inputted two lucky numbers.

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
def lucky_sum(num1,num2): #defines function for user to input 2 lucky numbers
    if num1 > num2:
        num1, num2 = num2, num1 #allows numbers to be interchangeable
    total = 0
    for i in range(num1,num2+1):
        if i%3!=0: #sets requirement for lucy sum
            total += i
    return total

def main():
    """Write your mainline logic below this line (then delete this line)."""
    #prompts user to input lucky numbers
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer: "))
    c = lucky_sum(a,b)   
    print(f"The sum of the lucky numbers is {c:,d}.")

    
    
    """Do not change anything below this line."""
if __name__ == "__main__":
    main()
