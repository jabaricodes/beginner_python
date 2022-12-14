"""
Author: Jabari Garraway, jgarrawa@purdue.edu
Assignment: 10.3 - Covid 19 Cases
Date: 11/16/2022

Description:
    This program plots the weekly postive COVID-19 Cases in Indiana in a bar chart.

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
import matplotlib.pyplot as plt
import datetime

def main():
    """Write your mainline logic below this line (then delete this line)."""
      
    col1 = [] #stores dates into list
    col3 = [] #stores amount of cases into list
    cumulative_sum = [] #cumulates sum of the weekly data

    with open('indiana_covid-19_data_fall_2022.txt') as icd: #opens text file to extract data
        for info in icd: 
            info.split() #splits data in each line into lists
            col1.append(info.split()[0]) #splits date column
            col3.append(float(info.split()[2])) #splits cases column
            cumulative_sum.append(sum(col3)/1000)   #account for data in the thousands
        fig, ax = plt.subplots()

        x = []
        for date in col1:
            y, m, d = date.split('-')
            date_time = datetime.date(int(y), int(m), int(d)) #formats date and time for plot
            x.append(date_time)
        fig.autofmt_xdate()

        y = cumulative_sum
        ax.bar(x,y,7) #plots bar chart with width 7
        ax.set_title('Weekly Positive COVID-19 Cases in Indiana')
        ax.set_xlabel('Date')
        ax.set_ylabel('Number of Cases (in thousands)')

        plt.show()
        icd.close()
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
