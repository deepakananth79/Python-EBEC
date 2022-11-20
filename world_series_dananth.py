"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 09.2 - world series
Date: 11/13/2022

Description:
    User enters a year and then the program returns the team that won the world series in that year
    along with how many times they've won the world series


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

#this function returns two dictionaries
def load_winners_data(): 

    dictionary1 = {}
    dictionary2 = {}

    with open("WorldSeriesWinners.txt") as fo: 
        #puts all the lines from input file in list
        lines = list(fo.readlines()) 

        year = 1902 
        for line in lines: 
            if year == 1993 or year == 1903:
                year += 1 
            year += 1 
            key = (year) 
            value = line[:-1] 
            dictionary2[key] = value

        #for loop that generates dictionary with winners and number of times they've won
        for line in lines: 
            string = line
            value = string[:-1]
            if value in dictionary1.keys():
                dictionary1[value] += 1 
            else:
                dictionary1[value] = 1 
        return dictionary1, dictionary2


def main():
        dictionaryList = load_winners_data()

        year = int(input("Enter a year in the range 1903 -- 2021: "))
        if int(year) > 2021 or int(year) < 1903:
            print(f"  Data for the year {year} is not included in this system.")
        elif int(year) == 1904 or int(year) == 1994:
            print(f"  The World Series wasn't played in the year {year}.")
        else:
            print(f"  The {dictionaryList[1][year]} won the World Series in"+f" {year}.")
            print(f"  They have won the World Series {dictionaryList[0][dictionaryList[1][year]]} times.")

if __name__ == '__main__':
    main()