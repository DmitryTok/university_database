from typing import Dict, List, Optional

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base
from .course_model import Course
from .student_course_model import student_course


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('group.id'))
    first_name = Column(String(50))
    last_name = Column(String(50))
    course: List[Course] = relationship(
        'Course',
        secondary=student_course,
        cascade='all, delete',
        backref='student',
        lazy='dynamic'
    )

    def to_dict(self) -> Dict[Optional[str], Optional[str | int]]:
        return dict(
            id=self.id,
            group_id=self.group_id,
            first_name=self.first_name,
            last_name=self.last_name,
        )
