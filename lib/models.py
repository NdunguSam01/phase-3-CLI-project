from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base=declarative_base()

class Student(Base):

    __tablename__='students'

    id=Column(Integer, primary_key=True, autoincrement=True)
    first_name=Column(String)
    last_name=Column(String)
    age=Column(Integer)

    marks=relationship("Mark", back_populates="students", viewonly=True)
    courses=relationship("Course", secondary="marks", back_populates="students", viewonly=True)

    def __repr__(self):
        return f"Student ID:{self.id}, First Name:{self.first_name}, Last Name={self.last_name}, Age={self.age}"
    
    def mark(self):
        return self.marks
    
    def course(self):
        return self.courses
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def add_student(self, session, first_name, last_name, age):
        student=Student(first_name=first_name, last_name=last_name, age=age,)
        session.add(student)
        session.commit()
    
class Course(Base):

    __tablename__='courses'

    id=Column(Integer, primary_key=True)
    course_name=Column(String)

    students=relationship("Student", secondary="marks", back_populates="courses", viewonly=True)
    marks=relationship("Mark", back_populates="courses", viewonly=True)

    def __repr__(self):
        return f"Course ID:{self.id} Course Name={self.course_name}"

    def student(self):
        return self.students
    
    def mark(self):
        return self.marks
    
    def add_course(self, session, course_name):
        course=Course(course_name=course_name)
        session.add(course)
        session.commit()
    
class Mark(Base):

    __tablename__='marks'

    id=Column(Integer, primary_key=True)
    student_id=Column(Integer, ForeignKey('students.id'))
    course_id=Column(Integer, ForeignKey('courses.id'))
    mark=Column(Integer)

    students=relationship("Student", back_populates="marks")
    courses=relationship("Course", back_populates="marks")

    def __repr__(self):
        return f"Mark ID:{self.id}, Student ID:{self.student_id}, Course ID:{self.course_id}, Mark:{self.mark})"
    
    def student(self):
        return self.students
    
    def course(self):
        return self.courses
    
    def full_marks(self):
        return f"Marks for {self.students.full_name()}: Course name: {self.courses.course_name} Marks: {self.mark}%"
    
    def add_mark(self, session, student_id, course_id, mark):
        new_mark=Mark(student_id=student_id, course_id=course_id, mark=mark)
        session.add(new_mark)
        session.commit()