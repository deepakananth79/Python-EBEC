"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 10.1 - monthly sales
Date: 11/20/2022

Description:
    User inputs the monthly sales, the program returns a pie chart of all of the data


Contributors:
    Deepak, dananth@purdue.edu [repeat for each]

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
#Imports matplot library module
import matplotlib.pyplot as plt

"""Write new functions below this line (starting with unit 4)."""


def main():

    #Contains the list of all the months to go through
    monthList = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    sales_list = []

    #Iterates through monthList
    for month in range(len(monthList)): 
        montly_sale = int(input(f"Enter the sales for {monthList[month]}: ")) 
        sales_list.append(montly_sale) 

    #Stores Purdue's "secondary color palatte"
    colorList = ('#4D4038','#BAA892','#5B6870','#6E99B4','#A3D6D7','#085C11','#849E2A','#C3BE0B','#E9E45B','#6B4536','#B46012','#FF9B1A')

    #Plotting instructions
    fig, ax = plt.subplots() 
    ax.set_title("Monthly Sales Values") 
    ax.pie(sales_list, colors = colorList, labels = monthList) 

    plt.show()

    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
