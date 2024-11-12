"""
EdTech needs to manage online courses and student progress.
Problem Statement:
 * Student Enrollment
 * Assignment submissions
 * Grade Records
Tasks:
1. Create set of active students.
2. Imlement binary serach for student records.
"""
active_students = set()
assignment_submissions = {}
grade_records = {}

def enrollStudent(student_id):
    active_students.add(student_id)
    print("Student", student_id, "enrolled.")

def submitAssignment(student_id, assignment):
    if student_id not in active_students:
        print("Student", student_id, "is not enrolled.")
        return
    if student_id not in assignment_submissions:
        assignment_submissions[student_id] = []
    assignment_submissions[student_id].append(assignment)
    print("Assignment", assignment, "submitted by student", student_id)

def recordGrade(student_id, grade):
    if student_id not in active_students:
        print("Student", student_id, "is not enrolled.")
        return
    grade_records[student_id] = grade
    print("Grade", grade, "recorded for student", student_id)

def linearSearchStudent(student_id):
    for student in active_students:
        if student == student_id:
            return "Student " + student_id +" found."
    return "Student" + student_id + "not found."

def printData():
    print("Students Enrolled: \n", active_students)
    print("Assignments Submitted: \n", assignment_submissions)
    print("Grade Records: \n", grade_records)

def displayMenu():
    print("\nEdTech Management System")
    print("1. Enroll Student")
    print("2. Submit Assignment")
    print("3. Record Grade")
    print("4. Search for Student")
    print("5. Print All Data")
    print("6. Exit")

while True:
    displayMenu()
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        enrollStudent(input("Enter student ID to enroll: "))
    elif choice == '2':
        student_id = input("Enter student ID for assignment submission: ")
        assignment = input("Enter assignment name: ")
        submitAssignment(student_id, assignment)
    elif choice == '3':
        recordGrade(input("Enter student ID to record grade: "), input("Enter grade: "))
    elif choice == '4':
        print(linearSearchStudent(input("Enter student ID to search: ")))
    elif choice == '5':
        printData()
    elif choice == '6':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

