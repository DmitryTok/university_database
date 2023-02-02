from models import Course, Group, Student
from task_10_sql.app.database import db
from task_10_sql.controllers import (CoursesController, GroupController,
                                     StudentsController)


def test_get_groups_controller():
    create_group = Group(name='test_group_name')
    db.session.add(create_group)

    result = GroupController.get_all_groups_students()
    expected_result = [(1, 'test_group_name', 0)]

    assert expected_result == result


def test_get_courses_controller():
    create_course = Course(name='test_course')
    db.session.add(create_course)
    db.session.commit()

    expected_result = db.session.query(Course).filter_by(id=create_course.id).first()
    result = db.session.query(Course).filter_by(id=1).first()

    assert expected_result == result


def test_get_students_controller():
    student = Student(first_name='student')
    course = Course(name='course', description='description')
    student.course.append(course)
    db.session.add_all([student, course])
    db.session.commit()

    expected_result = db.session.query(Student).all()
    result = StudentsController().get_all_students()

    assert result == expected_result


def test_get_student_by_id_controller():
    student = Student(first_name='student')
    course = Course(name='course', description='description')
    student.course.append(course)
    db.session.add_all([student, course])
    db.session.commit()

    expected_result_1 = db.session.query(Student).filter_by(id=1).first()
    result_1 = StudentsController().get_student_by_id(1)[0][0]

    assert result_1 == expected_result_1


def test_delete_student_by_id_controller():
    student = Student(first_name='student_1')
    course = Course(name='course_1', description='description')
    student.course.append(course)
    db.session.add_all([student, course])
    db.session.commit()

    data = db.session.query(Student).filter_by(id=1).first()
    expected_result_1 = StudentsController().delete_student_by_id(data.id)

    assert expected_result_1 is None


def test_create_student_controller():
    StudentsController().create_student('test_name', 'test_last_name', 1)

    expected_result = db.session.query(Student).filter_by(id=2).first()
    result = StudentsController().get_student_by_id(2)[0][0]

    assert expected_result == result


def test_create_student_to_course_controller():
    student = Student(first_name='student_1')
    course = Course(name='course_1', description='description')
    course_2 = Course(name='course_2', description='description')
    student.course.append(course)
    db.session.add_all([student, course, course_2])
    db.session.commit()

    CoursesController().create_course_student(student.id, course_2.id)
    get_student = StudentsController.get_student_by_id(student.id)
    result = StudentsController.serialize_student_id_response(get_student)
    expected_result = {
        'id': 5,
        'first_name': 'student_1',
        'last_name': None,
        'group_id': None,
        'courses': [{'id': 5, 'name': 'course_1'}, {'id': 6, 'name': 'course_2'}]
    }

    assert expected_result == result


def test_delete_student_course_controller():
    student = Student(first_name='student_1')
    course = Course(name='course_1', description='description')
    student.course.append(course)
    db.session.add_all([student, course])
    db.session.commit()

    expected_result_1 = CoursesController().delete_course_student(student.id, course.id)

    assert expected_result_1 is None
