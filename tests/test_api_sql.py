import json

import mock
from flask_api import status


@mock.patch('task_10_sql.controllers.GroupController.serialize_group_response')
@mock.patch('task_10_sql.controllers.GroupController.get_all_groups')
def test_get_groups(mock_get_all_groups, mock_serialize_group_response, client):
    mock_get_all_groups.return_value = [(2, 'test_group_name_2', 0), (1, 'test_group_name_1', 0)]
    expected_response = mock_serialize_group_response.return_value = [
        {'id': 2, 'name': 'test_group_name_2', 'student_amount': 0},
        {'id': 1, 'name': 'test_group_name_1', 'student_amount': 0}
    ]

    response = client.get('/api/groups/')

    mock_serialize_group_response.assert_called_with = (
        [
            {'id': 2, 'name': 'test_group_name_2', 'student_amount': 0},
            {'id': 1, 'name': 'test_group_name_1', 'student_amount': 0}
        ]
    )
    mock_get_all_groups.assert_called_with = (
        [(2, 'test_group_name_2', 0), (1, 'test_group_name_1', 0)]
    )

    assert response.json == expected_response

    assert response.status_code == status.HTTP_200_OK


@mock.patch('task_10_sql.controllers.CoursesController.serialize_courses_response')
@mock.patch('task_10_sql.controllers.CoursesController.get_all_courses')
def test_get_courses(mock_get_courses, mock_serialize_courses_response, client, test_data):
    mock_get_courses.return_value = test_data
    expected_response = mock_serialize_courses_response.return_value = [
        {'id': 1, 'name': 'Math', 'description': 'description for course Math'},
        {'id': 2, 'name': 'Geometry', 'description': 'description for course Geometry'}
    ]

    response = client.get('/api/courses/')

    mock_serialize_courses_response.assert_called_with = (
        [
            {'id': 1, 'name': 'Math', 'description': 'description for course Math'},
            {'id': 2, 'name': 'Geometry', 'description': 'description for course Geometry'}
        ]
    )
    mock_get_courses.assert_called_with = test_data

    assert response.json == expected_response

    assert response.status_code == status.HTTP_200_OK


@mock.patch('task_10_sql.controllers.StudentsController.serialize_student_id_response')
@mock.patch('task_10_sql.controllers.StudentsController.get_student_by_id')
def test_get_student_by_id(mock_get_students_by_id, mock_serialize_student_id_response, client, test_data):
    mock_get_students_by_id.return_value = test_data
    mock_serialize_student_id_response.return_value = (
        {
            'id': 3,
            'first_name': 'Nancy',
            'last_name': 'Gentry',
            'group_id': 4,
            'course': [{'id': 1, 'name': 'Math'}, {'id': 6, 'name': 'Astronomy'}]
        }
    )

    response_200 = client.get('/api/students/1/')

    mock_get_students_by_id.assert_called_with = test_data
    mock_serialize_student_id_response.assert_called_with = (
        {
            'id': 3,
            'first_name': 'Nancy',
            'last_name': 'Gentry',
            'group_id': 4,
            'course': [{'id': 1, 'name': 'Math'}, {'id': 6, 'name': 'Astronomy'}]
        }
    )

    assert response_200.status_code == status.HTTP_200_OK


@mock.patch('task_10_sql.controllers.StudentsController.serialize_student_response')
@mock.patch('task_10_sql.controllers.StudentsController.get_all_students')
def test_get_students(mock_get_all_students, mock_serialize_student_response, client, test_data):
    mock_get_all_students.return_value = test_data
    expected_response = mock_serialize_student_response.return_value = [
        {'id': 1, 'first_name': 'Loyce', 'last_name': 'Pujol', 'groups_id': 2},
        {'id': 2, 'first_name': 'Scott', 'last_name': 'Panella', 'groups_id': 6}
    ]

    response = client.get('/api/students/')

    mock_get_all_students.assert_called_with = test_data
    mock_serialize_student_response.assert_called_with = (
        [
            {'id': 1, 'first_name': 'Loyce', 'last_name': 'Pujol', 'groups_id': 2},
            {'id': 2, 'first_name': 'Scott', 'last_name': 'Panella', 'groups_id': 6}
        ]
    )

    assert response.json == expected_response

    assert response.status_code == status.HTTP_200_OK


@mock.patch('task_10_sql.controllers.StudentsController.delete_student_by_id')
def test_delete_student_by_id(mock_delete_student_by_id, client):
    mock_delete_student_by_id.return_value = {'id': 1, 'first_name': 'Loyce', 'last_name': 'Pujol', 'groups_id': 2}

    response_1 = client.delete(
        '/api/students/1/',
    )

    mock_delete_student_by_id.assert_called_with = (
        {'id': 1, 'first_name': 'Loyce', 'last_name': 'Pujol', 'groups_id': 2}
    )

    assert response_1.status_code == status.HTTP_204_NO_CONTENT


@mock.patch('task_10_sql.controllers.StudentsController.create_student')
def test_create_student(mock_create_student, client):
    data = mock_create_student.return_value = {
        'first_name': 'test_name',
        'last_name': 'test_last_name',
        'group_id': 1
    }

    expected_response = {'first_name': 'test_name', 'last_name': 'test_last_name', 'group_id': 1}

    response = client.post(
        '/api/students/',
        content_type='application/json',
        data=json.dumps(data)
    )

    mock_create_student.assert_called_with = (
        {
            'first_name': 'test_name',
            'last_name': 'test_last_name',
            'group_id': 1
        }
    )

    assert response.json == expected_response

    assert response.status_code == status.HTTP_201_CREATED


@mock.patch('task_10_sql.controllers.CoursesController.create_course_student')
def test_create_student_to_course(mock_create_student_course, client, test_data):
    mock_create_student_course.return_value = test_data

    response = client.post('/api/students/1/courses/1/')

    mock_create_student_course.assert_called_with = test_data

    assert response.status_code == status.HTTP_201_CREATED


@mock.patch('task_10_sql.controllers.CoursesController.delete_course_student')
def test_delete_student_course(mock_delete_student_course, client, test_data):
    mock_delete_student_course.return_value = test_data

    response = client.delete('/api/students/1/courses/1/')

    mock_delete_student_course.assert_called_with = test_data

    assert response.status_code == status.HTTP_204_NO_CONTENT


@mock.patch('task_10_sql.controllers.StudentsController.create_student')
@mock.patch('task_10_sql.controllers.CoursesController.create_course_student')
@mock.patch('task_10_sql.controllers.CoursesController.delete_course_student')
@mock.patch('task_10_sql.controllers.StudentsController.delete_student_by_id')
@mock.patch('task_10_sql.controllers.StudentsController.get_student_by_id')
def test_errors_404_400(
        mock_get_students_by_id,
        mock_delete_student_by_id,
        mock_delete_course_student,
        mock_create_course_student,
        mock_create_student,
        client,
        test_data):
    mock_get_students_by_id.return_value = None
    mock_delete_student_by_id.return_value = None
    mock_delete_course_student.return_value = test_data
    mock_create_course_student.return_value = {
        'id': 3,
        'first_name': 'Nancy',
        'last_name': 'Gentry',
        'group_id': 4,
        'course': [{'id': 1, 'name': 'Math'}, {'id': 6, 'name': 'Astronomy'}]
    }
    data = mock_create_student.return_value = (
        {
            'first_name': 'test_name',
            'last_name': 'test_last_name',
            'group_id': 123
        }
    )

    response_get_student_404 = client.get('/api/students/1/')
    response_delete_student_404 = client.delete('/api/students/1/')
    response_delete_course_student_400 = client.delete('/api/students/1/courses/2/')
    response_create_course_student_400 = client.post('/api/students/1/courses/111/')
    response_create_student_400 = client.post(
        '/api/students/',
        content_type='application/json',
        data=json.dumps(data)
    )

    mock_get_students_by_id.assert_called_with = None
    mock_delete_student_by_id.assert_called_with = None
    mock_delete_course_student.assert_called_with = test_data
    mock_create_course_student.assert_called_with = (
        {
            'id': 3,
            'first_name': 'Nancy',
            'last_name': 'Gentry',
            'group_id': 4,
            'course': [{'id': 1, 'name': 'Math'}, {'id': 6, 'name': 'Astronomy'}]
        }
    )
    mock_create_student.assert_called_with = (
        {'first_name': 'test_name', 'last_name': 'test_last_name', 'group_id': 123}
    )

    assert response_get_student_404.status_code == status.HTTP_404_NOT_FOUND
    assert response_delete_student_404.status_code == status.HTTP_404_NOT_FOUND
    assert response_delete_course_student_400.status_code == status.HTTP_400_BAD_REQUEST
    assert response_create_course_student_400.status_code == status.HTTP_404_NOT_FOUND
    assert response_create_student_400.status_code == status.HTTP_400_BAD_REQUEST
