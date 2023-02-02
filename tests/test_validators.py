from task_10_sql.validators import ValidateAPIData


def test_validate_student_group_data(test_data):
    validator_true = ValidateAPIData.validate_student_group_data(1)
    validator_false = ValidateAPIData.validate_student_group_data(2)

    assert validator_true
    assert not validator_false


def test_validate_student_course_data(test_data):
    validator_true = ValidateAPIData.validate_student_course_data(1, 1)
    validator_false = ValidateAPIData.validate_student_course_data(1, 2)

    assert validator_true
    assert not validator_false


def test_validate_post_student_course_data(test_data):
    validator_true = ValidateAPIData.validate_post_student_course_data(1, 1)
    validator_false = ValidateAPIData.validate_post_student_course_data(1, 111)

    assert validator_true
    assert not validator_false
