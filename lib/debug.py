#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Student, Course, Mark
import click

engine = create_engine("sqlite:///school.db")
Session = sessionmaker(bind=engine)
session = Session()

def all_student_details(session):
    print("\t\t\nStudent details")
    for student in session.query(Student).all():
        print(
            {
                "Student ID": student.id,
                "Name": student.full_name(),
                "Age": student.age
            }
        )
        # print(f"Student ID: {student.id}\nName: {student.full_name()} \nAge: {student.age}\n")

def all_courses(session):
    print("\t\t\nCourses")
    for course in session.query(Course).all():
        course=[course]
        print(course)

def all_marks(session):
    print("\t\t\nAll student marks")
    for mark in session.query(Mark).all():
        marks=()
        marks+=(mark.full_marks(),)
        print(marks)


def student_courses(session):
    print("\t\t\nAll student course(s)")
    for student in session.query(Student).all():
        courses=student.course()
        print(f"\nCourse(s) for {student.full_name()}:")
        for course in courses:
            print(course.course_name)


@click.command
def main():
    click.echo("Welcome to Student Information Management System")
    click.echo("Select an option to get started")

    options=[
        "1: Display student data", 
        "2: Display all courses", 
        "3: Print all marks", 
        "4: Print a student's course(s)",
        "5: Add a new student", 
        "6: Add a new course", 
        "7: Add a new student mark"]

    for option in options:
        click.echo(option)

    choice=click.prompt("Enter your choice", type=int)

    if choice in range(1,len(options) +1):

        if choice == 1:
            all_student_details(session)

        elif choice == 2:
            all_courses(session)

        elif choice == 3:
            all_marks(session)

        elif choice == 4:
            student_courses(session)
            
        elif choice == 5:
            first_name=click.prompt("Student first name", type=str)
            last_name=click.prompt("Student last name", type=str)
            age=click.prompt("Student age:", type=int)
            Student().add_student(session, first_name, last_name, age)
            print("Student added successfully!")

        elif choice == 6:
            course_name=click.prompt("Course name", type=str)
            Course().add_course(session, course_name)
            print("Course added successfully!")

        elif choice == 7:
            print("Add a new mark function")
            all_student_details(session)
            student_id=click.prompt("Enter student ID from the table above", type=int)
            all_courses(session)
            course_id=click.prompt("Enter course ID from the table above", type=int)
            marks=click.prompt("Enter student mark", type=int)
            Mark().add_mark(session,student_id,course_id, marks)
            print("Mark added successfully!")

        if click.confirm('Do you want to continue?', default=False):
            main()

    else:
        click.echo('Invalid operation. Please select a valid operation.\n')
        main()

if __name__ == '__main__':
    main()