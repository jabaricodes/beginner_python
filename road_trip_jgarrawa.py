"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 01.1 - Road Trip
Date: 08/31/2022

Description:
    This program will estimate the cost of a road trip as the output by inputting paramaters such as distance, price and miles per gallon.

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
    #Initial message for fuel cost estimator
    print("Road trip fuel cost estimator:")

    #Ask user to input the distance to destination, in miles
    trip_distance = int(input("  How far away is your destination (miles)? "))

    #Ask user to input the average cost of fuel in dollars per gallon
    price_avg = float(input("  What is the average price of gas (dollars per gallon)? "))

    #Ask user to input fuel efficiency of vehicle in miles per gallon
    fuelEfficiency = float(input("  What is the fuel efficiency of your vehicle (mpg)? "))

    #Calculate estimation of fuel cost for road trip
    fuel_cost = int((2*trip_distance*price_avg/fuelEfficiency))
    print("\nThe fuel cost for this trip is approximately $",
        format(int(fuel_cost), '.0f'), '.', sep='')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
