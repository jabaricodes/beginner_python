"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 01.3 - cookie recipe
Date: 08/31/2022

Description:
    This program outputs the amount of ingredients (butter,sugar, flour) needed to produce a desired number of cookies (user input).

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
    
    #allows user to indicate desrired number of cookies
    cookiesDesired = int(input("How many cookies do you want to make? "))

    #determines amount of ingredients for numberof cookies
    print(f"To make {cookiesDesired:,.0f} cookies, you will need:")

    #butter
    butterOut = cookiesDesired/38.4
    print(format(butterOut,'10,.2f')," cups of butter",'', sep='')
 
    #sugar
    sugarOut = cookiesDesired/32
    print(format(sugarOut,'10,.2f')," cups of sugar",'',sep='')

    #flour
    flourOut = cookiesDesired/19.2
    print(format(flourOut,'10,.2f')," cups of flour",'', sep='')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
