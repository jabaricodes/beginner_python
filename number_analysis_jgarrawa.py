"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 07.2 - Number Analysis
Date: 10/25/2022

Description:
    This program allows user to input a list of ten floating point numbers and then outputs the highest, lowest, total and average values of the list respectively.

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
def get_number_list():  

    
    num_list = [] #sets empty list for user input

    for i in range(1,10+1):
        item = (float(input(f"  number {i:2} of 10: "))) #prompts user to input float number
        num_list.append(item) #creates list 

    return num_list

def main(): 
    """Write your mainline logic below this line (then delete this line)."""
   
    print("Enter 10 numbers:")

    main_list = get_number_list()
    print(f'Highest number: {max(main_list):.2f}') #calcualtes max number
    print(f'Lowest number: {min(main_list):.2f}') #calculates min number
    print(f'Total: {sum(main_list):.2f}') #calculates sum of list
    print(f'Average: {sum(main_list)/len(main_list):.2f}') #calculates average of list
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
