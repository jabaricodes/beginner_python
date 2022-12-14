"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 04.4 - Prime Numbers
Date: 9/19/2022

Description:
    This program asks the user to input and number and then determines if it is prime or not prime.

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
def is_prime(prime): #sets requirement to determine prime number
    if prime == 1 or prime == 0:
        return False
        
    for i in range(2,int(prime**0.5)+1):
        if (prime %i == 0):
            return False #returns if not prime number
        
    return True #returns if prime number
       
def main():
    """Write your mainline logic below this line (then delete this line)."""

    num=int(input("Enter a positive integer (-1 to quit): "))
    while num >= 0: #continues until negative then ends program
        if is_prime(num):
            print(f"  {num} is prime!")
        else:
            print(f"  {num} is not prime.")
        num=int(input("Enter a positive integer (-1 to quit): "))

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
