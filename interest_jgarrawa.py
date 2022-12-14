"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 01.2 - Interest
Date: 08/31/2022

Description:
    This program performs a calculation for interest accrued over a period of time by predicting a future value using the parameters of principal deposit, annual interest rate, number of years left to earn interest and number of times per year the interest is compound.

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
    #initial message to prompt user to enter interest parameters
    message = "Enter the following parameters."
    print(message)

    #ask user to enter intial deposit
    depo_int = int(input("  The initial deposit? "))

    #ask user to enter the interest rate in percent
    intrstRate_prct = float(input("  The annual interest rate in percent? "))

    #ask user to enter number of years the account earn interest
    interest_years = float(input("  The number of years the account earn interest? "))

    #ask user to enter the numbe rof times interest is compounded each year
    numComp = int(input("  The number of times interest is compounded each year: "))

    #output the balance of the account for the equivalent amount of years
    accountBalance = depo_int*(1+(intrstRate_prct/100)/numComp)**(numComp*interest_years)

    print(f"The balance of this account will be ${accountBalance:,.2f} after {interest_years:.1f} years.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()