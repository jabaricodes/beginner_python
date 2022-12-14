"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 04.3 - Avg Grade
Date: 9/19/2022

Description:
    This program asks user to input a valid score five times then displays a letter grade after each grade as well as the average and corresponding letter grade.

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

def get_valid_score():
        a = float(input("Enter a score: ")) #asks the user to enter a score
        while a < 0 or a > 100:
            print("  Invalid Input. Please try again.")
            a = float(input("Enter a score: "))
        return a

def calc_average(list): #accepts the list of scores and returns the average of the scores
    sum=0
    for i in list:
        sum+=i 

    avg=sum/len(list)
    return avg


def determine_grade(c): #accepts score and returns a letter grade based on grading scale.
    if 92 <= c <= 100:
        return "A"
    elif 82 <= c < 92:
        return "B"
    elif  73 <= c < 82:
        return "C"
    elif  64 <= c < 73:
        return "D"
    elif 0 <= c < 64:
        return "F"

def main():
    """Write your mainline logic below this line (then delete this line)."""
    grades=[] #sets letter grade output determined by score
    for i in range(5):
        score=get_valid_score() 
        print(f"  The letter grade for {score:.1f} is {determine_grade(score)}.")
        grades.append(score)
    print()
    print("Results:")    
    print(f"  The average score is {calc_average(grades):.2f}.") #average score
    print(f"  The letter grade for {calc_average(grades):.2f} is {determine_grade(calc_average(grades))}.") #letter grade

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
