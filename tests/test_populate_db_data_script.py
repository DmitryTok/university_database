from models import Course, Group, Student
from task_10_sql.app.database import db
from task_10_sql.populate_db_data_script import (generate_course_name,
                                                 generate_group_name,
                                                 generate_students_names)


def test_generate_group_name():
    expected_result = generate_group_name()
    result = db.session.query(Group).all()
    assert expected_result == result


def test_generate_course_name():
    expected_result = generate_course_name()
    result = db.session.query(Course).all()
    assert expected_result == result


def test_generate_students_name():
    generate_group_name()
    courses = generate_course_name()
    expected_result = generate_students_names(courses)
    result = db.session.query(Student).all()
    assert expected_result == result
