"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 04.5 - Prime List
Date: 9/19/2022

Description:
    This program uses the is_prime function from Assignment 04.4 and lists all of the prime numbers from 2 to a user specified input.

Contributors:
    Joyce Zou, zou121@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [Y] think through the meaning of a specific error or
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

def is_prime(num): #uses is_prime function to determine prime number
    if num == 1:
        return False
    for i in range(2,(int(num**0.5)+1)):
        if (num %i == 0):
            return False
    return True
 
def main():
    primeList=[]
    positiveInt = int(input("Enter a positive integer: "))  
    for i in range(2,positiveInt+1): #checks for all prime numbers
        if is_prime(i):
            primeList.append(i) #lists all prime numbers from 2 to user input

    print(f"The primes up to {positiveInt} are:",end=" ")
    for i in primeList[:-1]:
        if i != (positiveInt == True):
            print(i,end=', ') #separates list with comma
        else: 
            print(i)
    print(primeList[-1]) #prints up to lst prime number in list
    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
