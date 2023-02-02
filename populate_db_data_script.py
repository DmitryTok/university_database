import random
from typing import List

import names

from models import Base, Course, Group, Student
from task_10_sql.app.database import db
from task_10_sql.app.main import create_app
from task_10_sql.logger import logger
from task_10_sql.settings import Config

group_list = ['Google', 'Netflix', 'Tesla',
              'BMW', 'Mercedes', 'Facebook',
              'Apple', 'KFC', 'UFC', 'Burger King']

course_list = [
    'Math', 'Geometry', 'Geography',
    'Philosophy', 'Physics', 'Astronomy',
    'Psychology', 'Anatomy', 'Literature', 'Informatics'
]


def generate_group_name() -> List[Group]:
    logger.info('Start generate groups names')
    group_name = []
    generate_groups = [group for group in enumerate(group_list, 1)]
    for group in generate_groups:
        group_name.append(f'{group[1]} - {group[0]}')
    for item in group_name:
        insert_data = Group(name=item)
        db.session.add(insert_data)
    db.session.commit()
    logger.info('Successfully generated groups names data')
    return db.session.query(Group).all()


def generate_students_names(courses: List[Course]) -> List[Student]:
    logger.info('Start generate students names')
    names_list = [names.get_full_name() for _ in range(15)]
    for student_name in names_list:
        split_name = student_name.split()
        create_student = Student(group_id=random.randrange(1, 11), first_name=split_name[0], last_name=split_name[1])
        student_course = random.sample(courses, random.randrange(1, 4))
        for course in student_course:
            create_student.course.append(course)
            db.session.add(create_student)
    db.session.commit()
    logger.info('Successfully generated student names data')
    return db.session.query(Student).all()


def generate_course_name() -> List[Course]:
    logger.info('Start generate course names')
    for item in course_list:
        insert_data = Course(name=item, description=f'description for course {item}')
        db.session.add(insert_data)
    db.session.commit()
    logger.info('Successfully generated course names data')
    return db.session.query(Course).all()


if __name__ == '__main__':
    with create_app(Config).app_context():
        Base.metadata.create_all(db.engine)
        generate_group_name()
        all_courses = generate_course_name()
        generate_students_names(all_courses)
