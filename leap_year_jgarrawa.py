"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 02.1 - Leap Year
Date: 09/05/2022

Description:
    This program will determine what year consists of a leap year and has 29 or 28 days in February in the respective year

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

    CENTURY_100 = 100 
    LEAPYEAR_400 = 400 
    LEAPCRIT = 4 
    FEB29 = 29 
    FEB28 = 28 
    
    #Prompts the user to enter what year 

    leapYear4 = int(input("Enter a year: "))

    #divisible by 100 followed by 400 to account for a leap year

    if (leapYear4%CENTURY_100)==0 and (leapYear4%LEAPYEAR_400)==0:
        print(f"The year {leapYear4:.0f} is a leap year.")
        print(f"February of {leapYear4:.0f} has {FEB29:.0f} days.")

    else:

    #divisible by 100 followed by 400 to account for a leap year

        if (leapYear4%CENTURY_100)!=0 and (leapYear4%LEAPCRIT)==0:
            print(f"The year {leapYear4:.0f} is a leap year.")
            print(f"February of {leapYear4:.0f} has {FEB29:.0f} days.")

    #Outputs year that is not a leap year  
        else:
            print(f"The year {leapYear4:.0f} is not a leap year.")
            print(f"February of {leapYear4:.0f} has {FEB28:.0f} days.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
