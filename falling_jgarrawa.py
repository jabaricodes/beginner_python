"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 04.1 - Falling
Date: 9/19/2022

Description:
    This program calulcates the distance travelled at a certain time.

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


    #calls funtion to set data frame

        a = falling_dist(5)
        print("Time (s)  Distance (m)")
        print("----------------------")
        for i in range(5,55,5):
            a = falling_dist(i)
            print(f"    {i:4}      {a:8.1f}")

    #introduces main function to calculate falling distance
def falling_dist(timeIncr):
    #time taken for object to travel at a certain distance looped in increments of 5 seconds
        GRAVITATION  = 8.87 #sets gravitational constant
        TIME = 5
    
        # calculates distance travelled at the specific time
        objDist = 0.5 * GRAVITATION * ((timeIncr)**2)
        return objDist

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
