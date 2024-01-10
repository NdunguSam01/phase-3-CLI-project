from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Course, Mark
from faker import Faker

faker=Faker()

engine = create_engine("sqlite:///school.db")

Session = sessionmaker(bind=engine)
session = Session()

def add_data():

    # session.delete(Student)
    # session.delete(Course)
    # session.delete(Mark)

    students=[
        Student(first_name=faker.first_name(), last_name=faker.last_name(), age=faker.random_int(1, 30))
        for _ in range(10)
    ]

    for student in students:
        session.add(student)

    courses=[
        Course(course_name=faker.word())
    for _ in range(5)
    ]

    for course in courses:
        session.add(course)

    marks=[
        Mark(students=faker.random_element(students), courses=faker.random_element(courses), mark=faker.random_int(1, 100))
        for _ in range(10)
    ]

    for mark in marks:
        session.add(mark)

    session.commit()

if __name__ == "__main__":
    add_data()
    