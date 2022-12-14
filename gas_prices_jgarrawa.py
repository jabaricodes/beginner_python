"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 10.2 - Gas Prices
Date: 11/16/2022

Description:
    This program plots the 2008 weekly gas prices in a line graph.

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

"""Write new functions below this line (starting with unit 4)."""


def main():
    """Write your mainline logic below this line (then delete this line)."""

    week = [] #stores data into list
    with open('2008_Weekly_Gas_Averages.txt') as wga: #opens text file to get data
        for data in wga:
            week.append(float(data.strip())) #grabs data drom list
        
        fig, ax = plt.subplots()
        y = week #sets y-axis 
        x = range(1,53) #sets week 
        ax.plot(x,y) #plots gas price data
        ax.set_title('2008 Weekly Gas Prices') #sets title of chart
        ax.set_xlabel('Weeks (by number)')
        ax.set_ylabel('Average Price (dollars/gallon)') 
        ax.set_xticks([10,20,30,40,50]) #sets ticks for weeks
        ax.set_xlim(1,52) #sets yearly limit
        ax.set_ylim(1.5, 4.25)
        ax.grid()

        plt.show()
        wga.close()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
