"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 06.4 - Log Spiral
Date: 10/03/2022

Description:
    This program uses turtle commands to produce a logarithmic spiral.

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
from turtle import *
from math import*


"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(5)


def main():
    """Write your mainline logic below this line (then delete this line)."""

    coordinateA = 4 #set value for a
    coordinateB = 0.22 #set value for b
    speed(0)
    penup()
    goto(4,0)
    pendown()
    for teta in range(0,360*3+1,10): #sets 3 circles for spiral
        teta_rad = teta * pi/180 

        cartesian_x = (coordinateA*exp(coordinateB*teta_rad))*cos(teta_rad)
        cartesian_y = (coordinateA*exp(coordinateB*teta_rad))*sin(teta_rad)
        
        goto(cartesian_x,cartesian_y) #logaritmic finction to draw spiral
    


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
