from os import environ as env


class Config:
    SQLALCHEMY_DATABASE_URI = env.get(
        'DATABASE_URI',
        default='postgresql://postgres:password@localhost:5432/task_10_sql'
    )
    DEBUG = env.get('DEBUG_MODE', default=True)
    JSON_SORT_KEYS = env.get('JSON_SORT_KEYS', default=False)
    TESTING = False
    PORT = env.get('PORT', default=80)


class TestConfig:
    SQLALCHEMY_DATABASE_URI = env.get(
        'DATABASE_TEST_URI',
        default='postgresql://postgres:password@localhost:5432/task_10_sql_test'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
