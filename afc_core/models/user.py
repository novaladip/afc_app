from flask_sqlalchemy import SQLAlchemy

from afc_core.models import db, generate_uuid


class User(db.Model):
    id: str = db.Column(db.String(), primary_key=True, default=generate_uuid)
    email: str = db.Column(db.String(100), unique=True, nullable=False)
    password: str = db.Column(db.String(100), nullable=False)
    first_name: str = db.Column(db.String(100), nullable=False)
    last_name: str = db.Column(db.String(100), nullable=False)
    role: str = db.Column(db.String(), nullable=False)
    avatar: str = db.Column(db.String(), nullable=True)

    def __init__(self, email, password, first_name, last_name, role, avatar):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.avatar = avatar
