
import random

class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = random.randint(1000, 9999)  # Generating a random course ID
        self.course_name = course_name
        self.course_mark = course_mark

class Student:
    total_students = 0

    def __init__(self, student_number, student_name, student_age):
        self.student_id = random.randint(10000, 99999)  # Generating a random student ID
        self.student_number = student_number
        self.student_name = student_name
        self.student_age = student_age
        self.courses_list = []
        Student.total_students += 1

    def enroll_course(self, course_name, course_mark):
        course = Course(course_name, course_mark)
        self.courses_list.append(course)

    def get_student_details(self):
        return self.__dict__

    def get_student_courses(self):
        for course in self.courses_list:
            print(f"Course ID: {course.course_id}, Course Name: {course.course_name}, Course Mark: {course.course_mark}")

    def get_student_average(self):
        if len(self.courses_list) == 0:
            return 0
        total_marks = sum(course.course_mark for course in self.courses_list)
        return total_marks / len(self.courses_list)


students = []

while True:
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to Student\n"
                              "6.Exit"))
    except ValueError:
        print("Invalid selection. Please enter a valid option.")
        continue

    if selection == 1:
        student_number = input("Enter Student Number: ")
        student_name = input("Enter Student Name: ")
        while True:
            try:
                student_age = int(input("Enter Student Age: "))
                break
            except ValueError:
                print("Invalid Value")

        student = Student(student_number, student_name, student_age)
        students.append(student)
        print("Student Added Successfully")

    elif selection == 2:
        student_number = input("Enter Student Number: ")
        found_student = None
        for student in students:
            if student.student_number == student_number:
                found_student = student
                break
        if found_student:
            students.remove(found_student)
            print("Student Deleted Successfully")
        else:
            print("Student Not Exist")

    elif selection == 3:
        student_number = input("Enter Student Number: ")
        found_student = None
        for student in students:
            if student.student_number == student_number:
                found_student = student
                break
        if found_student:
            student_details = found_student.get_student_details()
            print("Student Details:")
            for key, value in student_details.items():
                print(f"{key}: {value}")
        else:
            print("Student Not Exist")

    elif selection == 4:
        student_number = input("Enter Student Number: ")
        found_student = None
        for student in students:
            if student.student_number == student_number:
                found_student = student
                break
        if found_student:
            average = found_student.get_student_average()
            print(f"Student Average: {average}")
        else:
            print("Student Not Exist")

    elif selection == 5:
        student_number = input("Enter Student Number: ")
        found_student = None
        for student in students:
            if student.student_number == student_number:
                found_student = student
                break
        if found_student:
            course_name = input("Enter Course Name: ")
            course_mark = float(input("Enter Course Mark: "))
            found_student.enroll_course(course_name, course_mark)
            print("Course Added Successfully")
        else:
            print("Student Not Exist")

    elif selection == 6:
        break