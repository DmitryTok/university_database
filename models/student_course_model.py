from sqlalchemy import Column, ForeignKey, Integer, Table

from .base import Base

student_course = Table(
    'student_course',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('student.id', ondelete='CASCADE')),
    Column('course_id', Integer, ForeignKey('course.id', ondelete='CASCADE'))
)
