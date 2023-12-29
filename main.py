import sys
print(f"Welcome to the university system\n")

name = str(input("What's your name?\n"))
print(f"Hello", name)

user_state = str(input("Are you registering or logging in?\n"))
if user_state == "registering":
    print(f"Answer the following questions\n")
else:
    print(f"Welcome back {name}")


age = int(input("How old are you?\n"))

if age >= 15:
    print(f"Welcome {name}!")
else:
    print(f"Sorry {name}, you are too young to join us!")
    sys.exit()

matric_number = int(input("What is your matric number?\n"))
print(f"Are you sure this is your Matric number? {matric_number}?")
if matric_number == "":
    print(f"You may proceed...")
else:
    print(f"Incorrect!")
university_courses = {
    1: "Introduction to Computer Science",
    2: "Calculus I",
    3: "English Composition",
    4: "History of Art",
    5: "Physics for Engineers",
    6: "Psychology 101",
    7: "Business Ethics",
    8: "Data Structures and Algorithms",
    9: "Linear Algebra",
    10: "Creative Writing",
    11: "Introduction to Economics",
    12: "Chemistry Fundamentals",
    13: "Political Science",
    14: "Digital Marketing Strategies",
    15: "Environmental Science",
    16: "Sociology of Culture",
    17: "Organic Chemistry",
    18: "Financial Accounting",
    19: "Introduction to Linguistics",
    20: "Statistics for Social Sciences"
}

university_programs = {
    1: "Computer Science",
    2: "Mathematics",
    3: "English Literature",
    4: "Art History",
    5: "Engineering",
    6: "Psychology",
    7: "Business Administration",
    8: "Computer Engineering",
    9: "Mathematical Sciences",
    10: "Creative Writing",
    11: "Economics",
    12: "Chemistry",
    13: "Political Science",
    14: "Marketing",
    15: "Environmental Studies",
    16: "Sociology",
    17: "Chemical Engineering",
    18: "Accounting",
    19: "Linguistics",
    20: "Social Sciences"
}

degrees = {
    1: "BsC",
    2: "Master's Degree",
    3: "PhD"
}

course_id = 0
while course_id not in university_courses:
    print("\nList of Courses:")
    for course_id, course in university_courses.items():
        print(f"{course_id}: {course}")
    
    course_id = int(input("\nPlease enter the course id: "))
    if course_id in university_courses:
        print(f"You have selected {university_courses[course_id]}")
    else:
        print(f"Invalid course id. Please select from the following ids: {', '.join(map(str, university_courses.keys()))}")

selected_program_id = 0
while selected_program_id not in degrees:
    print("\nList of Programs:")
    for program_id, program in degrees.items():
        print(f"{program_id}: {program}")
    
    selected_program_id = int(input("\nPlease enter the program id: "))
    if selected_program_id in degrees:
        print(f"You have selected {degrees[selected_program_id]}")
    else:
        print(f"Invalid program id. Please select from the following ids: {', '.join(map(str, degrees.keys()))}")

if selected_program_id == 1:
    print(f"Go to the Undergraduate's hall")

elif selected_program_id == 2:
    print(f"Go to Kashinski's hall")

elif selected_program_id == 3:
    print(f"Go to K.A Stroud's hall")