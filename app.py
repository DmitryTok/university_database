from task_10_sql.app.main import create_app
from task_10_sql.settings import Config

if __name__ == '__main__':
    app = create_app(Config)
    app.run(host='0.0.0.0', port=int(Config.PORT))
