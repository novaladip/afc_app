from uuid import uuid4
from flask_sqlalchemy import SQLAlchemy


def generate_uuid() -> str:
    return str(uuid4())


db = SQLAlchemy()
