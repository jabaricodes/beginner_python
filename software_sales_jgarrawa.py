"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 02.2 - Software Sales
Date: 09/05/2022

Description:
    This program outputs the discount given due to the amount of software package purchased 

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
    #Prompts user to input the quantity 

    softQuant = int(input("How many packages will be purchased: "))

    #Ouputs discount 

    disc1 = "10%"
    disc2 = "15%"
    disc3 = "30%"
    disc4 = "42%"

    #Sets paramaters for percentage discount 

    softDiscount1 = 0.90 * softQuant * 880
    softDiscount2 = 0.85 * softQuant * 880
    softDiscount3 = 0.70 * softQuant * 880
    softDiscount4 = 0.58 * softQuant * 880
    noDiscount = softQuant * 880

    #Evaluates range to ouput discount applied

    if softQuant >= 4 and softQuant <= 39:
        print(f"  {disc1} discount applied.")
        print(f"  The total price to purchase {softQuant} packages is ${softDiscount1:,.2f}.") 
    else:
        if softQuant >= 40 and softQuant <= 199:
            print(f"  {disc2} discount applied.")
            print(f"  The total price to purchase {softQuant} packages is ${softDiscount2:,.2f}.") 
        else:
            if softQuant >= 200 and softQuant <= 999:
                print(f"  {disc3} discount applied.")
                print(f"  The total price to purchase {softQuant} packages is ${softDiscount3:,.2f}.") 
            else: 
                if softQuant >= 1000:
                    print(f"  {disc4} discount applied.")
                    print(f"  The total price to purchase {softQuant} packages is ${softDiscount4:,.2f}.") 
                else:
                    #Sends user error 
                    if softQuant >= 1 and softQuant <=3: 
                        print("  No discount applied.")
                        print(f"  The total price to purchase {softQuant} packages is ${noDiscount:,.2f}.")
                    else: 
                        if softQuant <= 0:
                            print("  Invalid Input!")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
