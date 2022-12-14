"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 10.4 - Sin Cos
Date: 11/16/2022

Description:
    This program uses matplotlib to draw a plot of sine and cosine from 0 to 2*pi on the same axes.

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
import matplotlib.pyplot as plt
import numpy as np
from math import *

"""Write new functions below this line (starting with unit 4)."""

def main():
    """Write your mainline logic below this line (then delete this line)."""
    fig, ax = plt.subplots()
    interval_wave = np.array([radians(i) for i in range(361)]) #sets limits for sine and cos waves
    sine_wave = np.sin(interval_wave) #plots sine wave as a function of the set limits
    cos_wave = np.cos(interval_wave) #plots cos wave as a function of the set limits
    
    ax.set_yticks([-1,1]) #sets y limits for curves
    ax.set_xticks([np.pi/2,np.pi,3*np.pi/2,2*np.pi,]) 
    ax.set_xticklabels(['$\\pi/2$', '$\\pi$', '$3\\pi/2$', '$2\\pi$']) #labels pi intervals 


    plt.plot(interval_wave,sine_wave, color = 'r') #plots sine wave in red
    plt.plot(interval_wave,cos_wave, color = 'b') #plots cos wave in blue
    

    for spine in ['top','right']: 
        ax.spines[spine].set_visible(False)
    for spine in ['bottom','left']:
        ax.spines[spine].set_position('zero') #sets position of x-axis to be in the middle of the graph

    plt.show()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
