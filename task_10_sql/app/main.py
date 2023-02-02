from typing import Type

from flasgger import Swagger
from flask import Flask
from flask_restful import Api

from task_10_sql.api_sql import (CoursesListAPI, GroupsListAPI, StudentAPI,
                                 StudentsListAPI, StudentToCoursesAPI)
from task_10_sql.settings import Config, TestConfig

from .database import db


def create_app(config: Type[Config | TestConfig]) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    Swagger(app)
    api = Api(app)
    api.add_resource(GroupsListAPI, '/api/groups/')
    api.add_resource(StudentAPI, '/api/students/<student_id>/')
    api.add_resource(StudentsListAPI, '/api/students/')
    api.add_resource(StudentToCoursesAPI, '/api/students/<student_id>/courses/<course_id>/')
    api.add_resource(CoursesListAPI, '/api/courses/')
    return app
