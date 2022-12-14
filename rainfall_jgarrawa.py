"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 03.3 - Rainfall
Date: 09/15/2022

Description:
    This program utilizes a series of nested loops to collect data and calculate the average rainfall over a period of years.

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

    yearsInt = int(input("Enter the number of years: ")) #prompts user to input amount of years
    months = ['Jan.','Feb.','Mar.','Apr.','May.','Jun.','Jul.','Aug.','Sep.','Oct.','Nov.','Dec.'] 
    rains=[]
    if yearsInt >= 1:
        for y in range( yearsInt): #chooses appropriate month for rainfall input
            print(f"  For year No. {y+1}")
            for month in months:    
                rainfall = float(input(f"    Enter the rainfall for {month}: "))
                while rainfall < 0 :
                    print("    Invalid input; rainfall cannot be negative.") #denies negative inputs
                    rainfall = float(input(f"    Enter the rainfall for {month}: "))
                rains.append(rainfall)

        total=0
        for i in rains:
            total+=i #adds rainfall

        print(f"There are {12*yearsInt} months.")
        print(f"The total rainfall was {total:.2f} inches.")
        print(f"The monthly average rainfall was {total/(12*yearsInt):.2f} inches.")
    else:
        print("Invalid input; years must be greater than 0.")            
    
                  
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
