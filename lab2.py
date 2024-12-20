class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    # Input functions
    def input_number_of_students(self):
        self.num_students = int(input("Enter the number of students: "))

    def input_student_information(self):
        for _ in range(self.num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student DoB: ")
            self.students.append(Student(student_id, name, dob))

    def input_number_of_courses(self):
        self.num_courses = int(input("Enter the number of courses: "))

    def input_course_information(self):
        for _ in range(self.num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            self.courses.append(Course(course_id, name))

    def select_course_and_input_marks(self):
        course_id = input("Enter course ID to input marks: ")
        course = next((course for course in self.courses if course.course_id == course_id), None)
        if not course:
            print("Course not found.")
            return
        for student in self.students:
            mark = float(input(f"Enter marks for student {student.name} (ID: {student.student_id}): "))
            student.marks[course_id] = mark

    # Listing functions
    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.name}")

    def list_students(self):
        print("Students:")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, DoB: {student.dob}")

    def show_student_marks_for_course(self):
        course_id = input("Enter course ID to show marks: ")
        course = next((course for course in self.courses if course.course_id == course_id), None)
        if not course:
            print("Course not found.")
            return
        print(f"Marks for course {course.name}:")
        for student in self.students:
            if course_id in student.marks:
                print(f"Student {student.name} (ID: {student.student_id}): {student.marks[course_id]}")
            else:
                print(f"Student {student.name} (ID: {student.student_id}): No marks entered")

# Example usage
school = School()
school.input_number_of_students()
school.input_student_information()
school.input_number_of_courses()
school.input_course_information()
school.select_course_and_input_marks()
school.list_courses()
school.list_students()
school.show_student_marks_for_course()