from typing import Any, Dict, List, Optional, Tuple, Union

from models import Course, Group, Student
from task_10_sql.app.database import db

from .validators import ValidateAPIData


class GroupController:

    @staticmethod
    def get_all_groups() -> List[Tuple[int]]:
        groups = db.session.query(Group.id).all()
        return groups

    @staticmethod
    def get_all_groups_students() -> List[Tuple[int, str, int]]:
        count_student = db.session.query(
            Group.id,
            Group.name,
            db.func.count(Student.group_id)
        ).outerjoin(Student,
                    Group.id == Student.group_id).group_by(Group.id).all()
        return count_student

    @classmethod
    def serialize_group_response(cls, group_data: List[Tuple[int, str, int]]) -> List[Dict[str, Union[Any, None]]]:
        response_lst = []
        for groups in group_data:
            response_lst.append(
                {
                    'id': groups[0],
                    'name': groups[1],
                    'student_amount': groups[2]
                }
            )
        return response_lst


class StudentsController:

    @staticmethod
    def get_all_students() -> List[Student]:
        return db.session.query(Student).all()

    @classmethod
    def serialize_student_response(cls, student_data: List[Student]) -> List[Dict[str, Any]]:
        response_lst = []
        for item in student_data:
            response_lst.append(
                {'id': item.id,
                 'first_name': item.first_name,
                 'last_name': item.last_name,
                 'groups_id': item.group_id,
                 }
            )
        return response_lst

    @staticmethod
    def get_student_by_id(student_id: int) -> List:
        get_student = db.session.query(
            Student, Course
        ).outerjoin(
            Course, Student.course
        ).filter(Student.id == student_id).all()
        return get_student

    @classmethod
    def serialize_student_id_response(cls, student_id_data: List) -> Dict[str, Any]:
        course_lst: List[Dict[str, str | None] | None] = []
        for student, course in student_id_data:
            if course is None:
                course_lst.append(None)
            else:
                course_lst.append(
                    {
                        'id': course.id,
                        'name': course.name
                    }
                )
            response_dct = {
                'id': student.id,
                'first_name': student.first_name,
                'last_name': student.last_name,
                'group_id': student.group_id,
                'courses': course_lst
            }
        return response_dct

    @staticmethod
    def create_student(first_name: str, last_name: str, group_id: int) -> Dict[Optional[str], Optional[str | int]]:
        add_student = Student(
            first_name=first_name,
            last_name=last_name,
            group_id=group_id
        )
        db.session.add(add_student)
        db.session.commit()
        return add_student.to_dict()

    @staticmethod
    def delete_student_by_id(student_id: int) -> None:
        student = db.session.query(Student).filter_by(id=student_id).first()
        db.session.delete(student)
        db.session.commit()


class CoursesController:

    @staticmethod
    def get_all_courses() -> List[Course]:
        return db.session.query(Course).all()

    @classmethod
    def serialize_courses_response(cls, course_data: List[Course]) -> List[Dict[str, Union[int, None, str]]]:
        return [course.to_dict() for course in course_data]

    @staticmethod
    def create_course_student(student_id: Optional[int], course_id: Optional[int]) -> Optional[bool]:
        query_student = db.session.query(Student).filter_by(id=student_id).first()
        query_course = db.session.query(Course).filter_by(id=course_id).first()
        if query_student is None:
            return ValidateAPIData.validate_post_student_course_data(student_id, course_id)
        query_student.course.append(query_course)
        db.session.commit()
        return None

    @staticmethod
    def delete_course_student(student_id: Optional[int], course_id: Optional[int]) -> Optional[bool]:
        query_student = db.session.query(Student).filter_by(id=student_id).first()
        query_course = db.session.query(Course).filter_by(id=course_id).first()
        if query_student is None:
            return ValidateAPIData.validate_student_course_data(student_id, course_id)
        query_student.course.remove(query_course)
        db.session.commit()
        return None
