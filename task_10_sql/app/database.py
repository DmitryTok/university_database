from flask_sqlalchemy import SQLAlchemy

from models.base import metadata

db = SQLAlchemy(metadata=metadata)
