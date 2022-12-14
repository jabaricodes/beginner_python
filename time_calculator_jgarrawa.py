"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 02.4 - Time Calculator
Date: 09/05/2022

Description:
    This program prompts the user to enter a number of seconds then dispalys the the total time un days, hours, minutes and seconds

Contributors:
    Darren Lie, lied@purdue.edu [repeat for each]

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


def main():
    """Write your mainline logic below this line (then delete this line)."""

    #promts user to enter time in seconds
    secondInt = int(input("Please enter a time in seconds: "))

    #calculation for seconds to days  
    intDay = secondInt // 86400

    #calculation for seconds to hours
    intHour = secondInt % 86400 // 3600

    #calculation for seconds into minutes
    intMinute = secondInt % 3600 // 60

    #remainder seconds calculation
    intSecRem = secondInt % 60 

    #converts input in seconds to its respective categories 

    if secondInt <= 59:
        print(f"  {secondInt} seconds is less than one minute.")
    else:
        print(f"  {secondInt:,d} seconds equals ", end='')
        if intDay:
            print(f"{intDay} day(s)", end='')
        if intHour:
            if intDay: # checks if there are any variables before hour (only days)
                if intMinute or intSecRem: # checks if there are any variables after hour (minutes and seconds)
                    print(', ',end='')
                else:
                    print(' and ', end='')
            print(f"{intHour} hour(s)", end='')
        if intMinute:
            if intDay or intHour:
                if intSecRem:
                    print(', ',end='')
                else:
                    print(' and ', end='')
            print(f"{intMinute} minute(s)", end ='')
        if intSecRem:
            if intDay or intHour or intMinute:
                print(' and ', end='')
            print(f"{intSecRem} second(s)", end='')
        print('.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
