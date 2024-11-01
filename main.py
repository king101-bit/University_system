import sys
from tabulate import tabulate


def register():
    name = input("Enter your new account name: \n")
    age = int(input("How old are you?\n"))

    if age >= 15:
        print(f"Welcome {name}!")
    else:
        print(f"Sorry {name}, you are too young to join us!")
        sys.exit()

register()

university_programs = {
    1: "Computer Science",
    2: "Mathematics",
    3: "English Literature",
    # Add other programs as needed...
}

degrees = {
    1: "Bachelor's Degree",
    2: "Master's Degree",
    3: "PhD"
}

# Define the Result class to hold subjects and grades
class Result:
    def __init__(self, status, program, subjects):
        self.status = status
        self.program = program
        self.subjects = subjects  # List of tuples (subject, grade)

# Create a result object with sample data including multiple subjects and grades
result = Result(
    status="Available",
    program="Computer Science",
    subjects=[
        ("Mathematics", "A"),
        ("Data Structures", "B+"),
        ("Algorithms", "A-"),
        ("Operating Systems", "B"),
        ("Computer Networks", "A"),
    ]
)

def check_result(result=None):
    # Prompt the user if they want to check their result
    response = input("Would you like to check your result? (yes/no): ").strip().lower()

    # If the user says 'yes', check the result status
    if response == "yes":
        if result and result.status == "Available":
            display_result(result)
        else:
            print("Your results are not available.")
    else:
        print("Okay, not checking the result.")

def display_result(result):
    # Prepare headers for the table
    headers = ["Program", "Subject", "Grade"]

    # Prepare data rows, one for each subject
    data = [
        [result.program, subject, grade]
        for subject, grade in result.subjects
    ]

    # Display the table with fancy_grid format
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

# Call the function to check and display the result
check_result(result)