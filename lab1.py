# Input functions
def input_number_of_students():
    return int(input("Enter the number of students: "))
# Functions for getting the number of students
def input_student_information(num_students):
    students = []
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student DoB: ")
        students.append({'student_id': student_id, 'name': name, 'dob': dob, 'marks': {}})
    return students
# Function for getting courses from student list
def input_number_of_courses():
    return int(input("Enter the number of courses: "))
# Function for getting courses information 
def input_course_information(num_courses):
    courses = []
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        courses.append({'course_id': course_id, 'name': name})
    return courses

def select_course_and_input_marks(students, courses):
    course_id = input("Enter course ID to input marks: ")
    course = next((course for course in courses if course['course_id'] == course_id), None)
    if not course:
        print("Course not found.")
        return
    for student in students:
        mark = float(input(f"Enter marks for student {student['name']} (ID: {student['student_id']}): "))
        student['marks'][course_id] = mark

# Listing functions
def list_courses(courses):
    print("Courses:")
    for course in courses:
        print(f"ID: {course['course_id']}, Name: {course['name']}")

def list_students(students):
    print("Students:")
    for student in students:
        print(f"ID: {student['student_id']}, Name: {student['name']}, DoB: {student['dob']}")

def show_student_marks_for_course(students, courses):
    course_id = input("Enter course ID to show marks: ")
    course = next((course for course in courses if course['course_id'] == course_id), None)
    if not course:
        print("Course not found.")
        return
    print(f"Marks for course {course['name']}:")
    for student in students:
        if course_id in student['marks']:
            print(f"Student {student['name']} (ID: {student['student_id']}): {student['marks'][course_id]}")
        else:
            print(f"Student {student['name']} (ID: {student['student_id']}): No marks entered")

# Example usage
num_students = input_number_of_students()
students = input_student_information(num_students)
num_courses = input_number_of_courses()
courses = input_course_information(num_courses)
select_course_and_input_marks(students, courses)
list_courses(courses)
list_students(students)
show_student_marks_for_course(students, courses)