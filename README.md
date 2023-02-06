![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![GitLab](https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white)

# University Database
### Run project
#### Clone repository to your computer
    Clone with SSH: git@github.com:DmitryTok/university_database.git
    Clone with HTTP: https://github.com/DmitryTok/university_database.git
#### Create and feel the .env file
DATABASE_URI=<...># specify that we use PostgreSQL database \
DEBUG_MODE=<...># This debugger should only be used during developing \
DATABASE_TEST_URI=<...># create database for a tests
#### Example    
    DATABASE_URI='postgresql://<user>:<password>@localhost:5432/<database_name>'
    DEBUG_MODE=True
    DATABASE_TEST_URI='postgresql://<user>:<password>@localhost:5432/<test_database_name>'
#### Fill your database
Run a docker-compose file
```
docker-compose up -d db
```
Specify which database you use
```
export DATABASE_URI='postgresql://<user>:<password>@localhost:5432/<database_name>'
```
Fill database if needed
```
python3 populate_db_data_entrypoint.py
```
Run app
```
python3 app.py
```
***
## Project author:
#### https://www.linkedin.com/in/dmitry-tokariev
#### https://github.com/DmitryTok

***
## Technology
    - Python 3.10
    - Flask
    - SQLAlchemy
    - PostgreSQL
    - Docker
    - Pytest
    - Swagger
