"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 8.5 - number reader
Date: 11/05/2022

Description:
    Reads random numbers from a file and displays the number of random
    numbers, minimum value, maximum value, sum, and average


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

    lines = [] # creares array that stores numbers as lines

    with open("random_numbers.txt") as fo: # context manager created
        for line in fo: # for loop adds each line to list
            lines.append(int(line.rstrip()))

    # print statements
    print(f"{len(lines):,} numbers were read from the file.")
    print(f"Min: {min(lines):,}")
    print(f"Max: {max(lines):,}")

    total = 0 # accumulator
    for i in lines: # for loop to sum contents of list
        total += i
        i += 1
    sum = total

    print(f"Sum: {sum:,}")
    print(f"Avg: {sum/len(lines):,.1f}")


if __name__ == '__main__':
    main()

