"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 02.5 - Fluid Mechanics
Date: 09/08/2022

Description:
    This program calculates the Reyndold's number using parameters of Velocity, diameter and kinematic viscosity

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
    #prompts user to enter temperature of the pipe

    pipeTemp = int(input("Enter the temperature in \u00B0C as 5, 20, or 50: "))

    #prompts user to enter velocity of water in pipe

    pipVelo = float(input("Enter the velocity of water in the pipe (m/s): "))

    #prompts user to enter the pipe's diamete

    diaPipe = float(input("Enter the pipe's diameter (m): "))

    #uses temperature input to determine Kinematic Viscosity

    pipeTemp5_kino = 0.00000152
    pipTemp20_kino = 0.0000010
    pipTemp50_kino = 0.000000554

    #uses temperature to calculate Reynolds Number

    reynCalc5 = (pipVelo*diaPipe)/pipeTemp5_kino
    reynCalc20 = (pipVelo*diaPipe)/pipTemp20_kino
    reynCalc50 = (pipVelo*diaPipe)/pipTemp50_kino

    #determines which Reynolds Number Calculation to use depending on Temperature

    if pipeTemp == 5:
        print(f"At {pipeTemp:.1f}\u00B0C, the Reynolds number for flow at {pipVelo} m/s in a {diaPipe} m diameter pipe is {reynCalc5:.2e}.") 
        
    else:
        if pipeTemp == 20:
            print(f"At {pipeTemp:.1f}\u00B0C, the Reynolds number for flow at {pipVelo} m/s in a {diaPipe} m diameter pipe is {reynCalc20:.2e}.")       
        else:
            if pipeTemp == 50:
                print(f"At {pipeTemp:.1f}\u00B0C, the Reynolds number for flow at {pipVelo} m/s in a {diaPipe} m diameter pipe is {reynCalc50:.2e}.")
                


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
