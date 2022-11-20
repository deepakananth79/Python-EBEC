"""
Author: Deepak Ananthakrishnan, dananth@purdue.edu
Assignment: 09.3 - course info
Date: 11/13/2022

Description:
    User inputs a course number, the program then outputs the matching course info for that course number


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


def get_course_data():
    #initilization of nested dictionary
    courseDictionary = {'CS101':{'instructor': 'Django','room': '3004', 'time': '9:00 a.m.'},
                        'CS102':{'instructor': 'Idle', 'room': '4501', 'time': '10:00 a.m.'},
                        'CS103':{'instructor': 'Rich', 'room': '6755', 'time': '11:00 a.m.'},
                        'NT110':{'instructor': 'Marshal', 'room': '1244', 'time': '12:00 p.m.'},
                        'CM241':{'instructor': 'Pickle', 'room': '1411', 'time': '2:00 p.m.'}, }

    return courseDictionary

def main():

    course = input("Enter a course number: ")
    #checks if user inputted course is in the dictionary
    if course in get_course_data(): 
        print(f"  The details for course {course} are:")
        courseInfo = get_course_data().get(course)
        for key,value in sorted(courseInfo.items()):
            #prints key and value information of everything in that course
            print(f'  {key.title().rjust(12)}:' , value) 
    else:
        print(f"  {course} is an invalid course number.")

if __name__ == '__main__':
    main()