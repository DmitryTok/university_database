from models import Base
from task_10_sql.app.database import db
from task_10_sql.app.main import create_app
from task_10_sql.populate_db_data_script import (generate_course_name,
                                                 generate_group_name,
                                                 generate_students_names)
from task_10_sql.settings import Config

if __name__ == '__main__':
    with create_app(Config).app_context():
        Base.metadata.create_all(db.engine)
        generate_group_name()
        all_courses = generate_course_name()
        generate_students_names(all_courses)
