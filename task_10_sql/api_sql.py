from typing import Any, Dict, List, Optional, Tuple, Union

from flask import request
from flask_api import status
from flask_restful import Resource

from .controllers import CoursesController, GroupController, StudentsController
from .validators import ValidateAPIData


class GroupsListAPI(Resource):

    def get(self) -> List[Dict[str, Optional[str]]]:
        """
        Get all groups
        ---
        responses:
          200:
            description: Get all groups with count students
            schema:
              type: "object"
              properties:
                order:
                  type: "object"
              example: {"id": 4, "name": "BMW - 4", "student_amount": 2}
        tags:
          - group
        """
        group = GroupController.get_all_groups_students()
        serialized_data = GroupController.serialize_group_response(group)
        return serialized_data


class StudentAPI(Resource):

    def get(self, student_id: int) -> Tuple[Dict[str, str], Any] | Dict[str, Any]:
        """
        Get student by id
        ---
        parameters:
          - name: student_id
            in: path
            type: integer
            required: true
        responses:
          200:
            description: Info about student
            schema:
              type: "object"
              properties:
                order:
                  type: "object"
              example:
                {
                  "id": 1,
                  "first_name": "Tracee",
                  "last_name": "Thomas",
                  "group_id": 9,
                  "courses": [{"id": 2,"name": "Geometry"},{"id": 4,"name": "Philosophy"}]
                }
          404:
            description: Student not exist
        tags:
          - students_get_delete_by_id
        """
        student = StudentsController.get_student_by_id(student_id)
        if not student:
            return {'error': 'Student not exist'}, status.HTTP_404_NOT_FOUND
        serialized_data = StudentsController.serialize_student_id_response(student)
        return serialized_data

    def delete(self, student_id: int) -> Tuple[Dict[str, str], None] | Tuple[None, Any]:
        """
        Delete student by id
        ---
        parameters:
          - name: student_id
            in: path
            type: integer
            required: true
        responses:
          204:
            description: Delete student by id
          404:
            description: Student not found
        tags:
          - students_get_delete_by_id
        """
        student = StudentsController()
        if not student.get_student_by_id(student_id):
            return {'error': 'Student not found'}, status.HTTP_404_NOT_FOUND
        student.delete_student_by_id(student_id)
        return None, status.HTTP_204_NO_CONTENT


class StudentsListAPI(Resource):

    def get(self) -> List[Dict[str, Any]]:
        """
        Get all students
        ---
        responses:
          200:
            description: Get all students'
            schema:
              type: "object"
              properties:
                order:
                  type: "object"
              example: {"id": 1, "first_name": "Tracee","last_name": "Thomas","groups_id": 9}
        tags:
          - students_get_post
        """
        student = StudentsController.get_all_students()
        serialized_data = StudentsController.serialize_student_response(student)
        return serialized_data

    def post(self) -> Tuple[Dict[Optional[str], Optional[str | int]], int]:
        """
        Create new student
        ---
        parameters:
        - in: body
          name: User
          description: The user to create.
          schema:
            type: object
            required:
              - first_name
              - last_name
              - group_id
            properties:
              first_name:
                type: string
              last_name:
                type: string
              group_id:
                type: integer
        responses:
            201:
              description: Create new student
              schema:
                type: "object"
                properties:
                  order:
                    type: "object"
                example: {"id": 22, "first_name": "test_first_name", "last_name": "test_last_name", "group_id": 1}
            400:
              description: Group not found
        tags:
          - students_get_post
        """
        data: Any = request.get_json()
        if not ValidateAPIData.validate_student_group_data(data['group_id']):
            return {'error': 'Group not found'}, status.HTTP_400_BAD_REQUEST
        student = StudentsController.create_student(
            data['first_name'],
            data['last_name'],
            data['group_id']
        )
        return student, status.HTTP_201_CREATED


class CoursesListAPI(Resource):

    def get(self) -> List[Dict[str, Union[int, None, str]]]:
        """
        Get all courses
        ---
        responses:
          200:
            description: Get all courses
            schema:
              type: "object"
              properties:
                order:
                  type: "object"
              example: {"id": 1, "name": "Math", "description": "description for course Math"}
        tags:
          - course_all_get
        """
        course = CoursesController.get_all_courses()
        serialized_data = CoursesController.serialize_courses_response(course)
        return serialized_data


class StudentToCoursesAPI(Resource):

    def post(self, student_id: int, course_id: int) -> Tuple[Dict[str, str], Any] | Tuple[Any, Any]:
        """
        Add student to course
        ---
        parameters:
          - name: student_id
            in: path
            type: integer
            required: true
          - name: course_id
            in: path
            type: integer
            required: true
        responses:
          201:
            description: Add student to course
            schema:
              type: "object"
              properties:
                order:
                  type: "object"
              example: {
                      "id": 2,
                      "first_name": "Arturo",
                      "last_name": "Ruple",
                      "group_id": 2,
                      "courses": [{"id": 3, "name": "Geography"}]
                  }
          404:
            description: Course or Student not found
        tags:
          - student_course_post_delete
        """
        if not ValidateAPIData.validate_post_student_course_data(student_id, course_id):
            return {'error': 'Course or Student not found'}, status.HTTP_404_NOT_FOUND
        CoursesController.create_course_student(student_id, course_id)
        student = StudentsController.get_student_by_id(student_id)
        serialized_data = StudentsController.serialize_student_id_response(student)
        return serialized_data, status.HTTP_201_CREATED

    def delete(self, student_id: int, course_id: int) -> Tuple[Dict[str, str], Any] | Tuple[None, Any]:
        """
        Remove student from course
        ---
        parameters:
          - name: student_id
            in: path
            type: integer
            required: true
          - name: course_id
            in: path
            type: integer
            required: true
        responses:
          204:
            description: Remove student from course
          400:
            description: Course not found
        tags:
          - student_course_post_delete
        """
        if not ValidateAPIData.validate_student_course_data(student_id, course_id):
            return {'error': 'Course not found'}, status.HTTP_400_BAD_REQUEST
        CoursesController.delete_course_student(student_id, course_id)
        return None, status.HTTP_204_NO_CONTENT
