#!/usr/bin/env python3

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Student, Course, Mark
import click

fake = Faker()

engine = create_engine("sqlite:///school.db")
Session = sessionmaker(bind=engine)
session = Session()

def all_student_details(session):
    print("\nPrinting student details")
    for student in session.query(Student).all():
        print(f"Student ID: {student.id}\nName: {student.full_name()} \nAge: {student.age}\n")

def all_courses(session):
    print("\nPrinting all courses")
    for course in session.query(Course).all():
        print(course.course_name)

def all_marks(session):
    print("\nPrinting all marks")
    for mark in session.query(Mark).all():
        print(mark.full_marks())

def student_courses(session):
    print("\nPrinting a student's courses")
    for student in session.query(Student).all():
        courses=student.course()
        print(f"\nCourses for {student.full_name()}:")
        for course in courses:
            print(course.course_name)

@click.command()
@click.option('--option', type=click.IntRange(1,4), prompt="Select an option \n1: Display student data\n2: Display all courses\n3: Print all marks\n4: Print a student's courses\n")

def main(option):

    options=["Display student data", "Display all courses", "Print all marks", "Print a student's courses"]

    if option in range(1, len(options) +1):
        if option == 1:
            all_student_details(session)

        elif option == 2:
            all_courses(session)

        elif option == 3:
            all_marks(session)

        elif option == 4:
            student_courses(session)

        if click.confirm('Do you want to continue?', default=False):
            main()

    else:
        click.echo('Invalid operation. Please select a valid operation.')

if __name__ == '__main__':
    main()