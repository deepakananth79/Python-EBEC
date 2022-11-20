"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 8.6 - step counter
Date: 11/05/2022

Description:
    Program that calculates and displays the average number of steps each
    month from the data from the steps text file


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


"""Write new functions below this line (starting with unit 4)."""
def main():

    allSteps = [] # stores values for daily steps from file

    with open('steps.txt') as fo: # context manager created
        for lines in fo:
            allSteps.append(int(lines.rstrip())) # appends each value of step to list as int

    # month list stores name of each month
    monthList = ["January","February","March","April","May","June","July","August","September","October","November","December"]

    print("The average steps taken each month were:")
    for month in monthList: # first for loop iterates through and prints each month in monthlist
        print(f"{month.rjust(10)} "+":", end = ' ') # each month is right justified with width 10 padding
        for step in month: # nested for loop should print average of each month
            if(month=="January"):
                print(f"{sum(allSteps[0:31])/len(allSteps[0:31]):.2f}") # uses sum() / len() functions to calculate mean for sliced portion of allSteps list
            elif(month == "February"):
                print(f"{sum(allSteps[31:59])/len(allSteps[31:59]):.2f}")
            elif(month == "March"):
                print(f"{sum(allSteps[59:90])/len(allSteps[59:90]):.2f}")
            elif(month == "April"):
                print(f"{sum(allSteps[90:120])/len(allSteps[90:120]):.2f}")
            elif(month == "May"):
                print(f"{sum(allSteps[120:151])/len(allSteps[120:151]):.2f}")
            elif(month == "June"):
                print(f"{sum(allSteps[151:181])/len(allSteps[151:181]):.2f}")
            elif(month == "July"):
                print(f"{sum(allSteps[181:212])/len(allSteps[181:212]):.2f}")
            elif(month == "August"):
                print(f"{sum(allSteps[212:243])/len(allSteps[212:243]):.2f}")
            elif(month == "September"):
                print(f"{sum(allSteps[243:273])/len(allSteps[243:273]):.2f}")
            elif(month == "October"):
                print(f"{sum(allSteps[273:304])/len(allSteps[273:304]):.2f}")
            elif(month == "November"):
                print(f"{sum(allSteps[304:334])/len(allSteps[304:334]):.2f}")
            elif(month == "December"):
                print(f"{sum(allSteps[334:366])/len(allSteps[334:366]):.2f}")
            break

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()