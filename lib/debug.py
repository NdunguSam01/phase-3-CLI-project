#!/usr/bin/env python3

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Student, Course, Mark

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine("sqlite:///school.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    print("\nPrinting student details")
    for student in session.query(Student).all():
        print(f"Student ID: {student.id}\nName: {student.full_name()} \nAge: {student.age}\n")

    print("\nPrinting all courses")
    for course in session.query(Course).all():
        print(course.course_name)

    print("\nPrinting all marks")
    for mark in session.query(Mark).all():
        print(mark.full_marks())

    print("\nPrinting a student's courses")
    for student in session.query(Student).all():
        courses=student.course()
        print(f"\nCourses for {student.full_name()}:")
        for course in courses:
            print(course.course_name)