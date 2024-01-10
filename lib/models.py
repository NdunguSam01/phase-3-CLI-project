from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base=declarative_base()

class Student(Base):

    __tablename__='students'

    id=Column(Integer, primary_key=True, autoincrement=True)
    first_name=Column(String)
    last_name=Column(String)
    age=Column(Integer)

    marks=relationship("Mark", back_populates="students")
    courses=relationship("Course", secondary="marks", back_populates="students")

    def __repr__(self):
        return f"Student(id={self.id}, first_name={self.first_name},last_name={self.last_name}, age={self.age})"
    
    def mark(self):
        return self.marks
    
    def course(self):
        return self.courses
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
class Course(Base):

    __tablename__='courses'

    id=Column(Integer, primary_key=True)
    course_name=Column(String)

    students=relationship("Student", secondary="marks", back_populates="courses")
    marks=relationship("Mark", back_populates="courses")

    def __repr__(self):
        return f"Course(id={self.id} name={self.course_name}"

    def student(self):
        return self.students
    
    def mark(self):
        return self.marks
    
class Mark(Base):

    __tablename__='marks'

    id=Column(Integer, primary_key=True)
    student_id=Column(Integer, ForeignKey('students.id'))
    course_id=Column(Integer, ForeignKey('courses.id'))
    mark=Column(Integer)

    students=relationship("Student", back_populates="marks")
    courses=relationship("Course", back_populates="marks")

    def __repr__(self):
        return f"Mark(id={self.id}, student_id={self.student_id}, course_id={self.course_id}, mark={self.mark})"
    
    def student(self):
        return self.students
    
    def course(self):
        return self.courses
    
    def full_marks(self):
        return f"Mark for {self.students.full_name()}: {self.courses.course_name}- {self.mark}%"