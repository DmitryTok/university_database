from typing import Optional

from models import Course, Group, Student, student_course_model
from task_10_sql.app.database import db


class ValidateAPIData:

    @staticmethod
    def validate_student_group_data(group_data: Optional[int]) -> bool:
        if db.session.query(Group).filter_by(id=group_data).first() is None:
            return False
        else:
            return True

    @staticmethod
    def validate_student_course_data(student_data: Optional[int], course_data: Optional[int]) -> bool:
        if db.session.query(
            student_course_model.student_course
        ).filter_by(
            student_id=student_data, course_id=course_data
        ).first() is None:
            return False
        else:
            return True

    @staticmethod
    def validate_post_student_course_data(student_data: Optional[int], course_data: Optional[int]) -> bool:
        student = db.session.query(Student).filter_by(id=student_data).first()
        course = db.session.query(Course).filter_by(id=course_data).first()
        if student is None or course is None:
            return False
        else:
            return True
