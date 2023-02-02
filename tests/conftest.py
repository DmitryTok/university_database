import pytest

from models import Course, Group, Student
from task_10_sql.app.database import db
from task_10_sql.app.main import create_app
from task_10_sql.settings import TestConfig


@pytest.fixture(autouse=True, scope='module')
def app():
    app = create_app(TestConfig)
    app.config.from_object(TestConfig)
    yield app


@pytest.fixture(autouse=True, scope='module')
def client(app):
    yield app.test_client()


@pytest.fixture(autouse=True, scope='module')
def test_database(app):
    with app.app_context():
        db.create_all()
        yield db
        db.session.remove()
        db.drop_all()


@pytest.fixture(scope='module')
def test_data(app):
    student_1 = Student(first_name='test_name_1')
    student_2 = Student(first_name='test_name_2')
    course_1 = Course(name='course_1', description='description course_1')
    course_2 = Course(name='course_2', description='description course_2')
    group = Group(name='group')
    student_1.course.append(course_1)
    student_2.course.append(course_2)
    with app.app_context():
        db.session.add_all([student_1, student_2, course_1, course_2, group])
        db.session.commit()
        yield db
