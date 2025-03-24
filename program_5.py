# Elijah Budd
# 3/21/2025
# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

def course_info():
    courses = {}

    num_courses = int(input("How many courses would you like to enter? "))

    for i in range(num_courses):
        course_id = input("Enter the course ID (e.g., COS 2005): ")
        course_name = input("Enter the course name (e.g., Python Programming): ")
        courses[course_id] = course_name

    subject = input("Enter a subject to search for (e.g., COS): ")

    print("Courses matching the subject:", subject)
    for course_id, course_name in courses.items():
        if course_id.startswith(subject):
            print(f"Course ID: {course_id}, Course Name: {course_name}")

course_info()
