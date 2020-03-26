from flask_sqlalchemy import SQLAlchemy

from afc_core.models import db
from afc_core.models.user import User
from afc_core.user.utils import hash_password


def get_user_by_id(id: str) -> User:
    user = User.query.filter_by(id=id).first()
    return user


def get_user_by_email(email: str) -> User:
    user = User.query.filter_by(email=email).first()
    return user


def get_users():
    users = User.query.all()
    return users


def create_user(user: User) -> User:
    db.session.add(user)
    db.session.commit()


def register_student(form, avatar: str):
    new_user = User(email=form['email'], password=form['password'],
                    first_name=form['first_name'], last_name=form['last_name'], avatar=avatar, role="STUDENT")

    new_user.password = hash_password(new_user.password)
    create_user(new_user)
    return new_user


def register_teacher(form, avatar: str) -> User:
    new_user = User(email=form['email'], password=form['password'], first_name=form['first_name'],
                    last_name=form['last_name'], avatar=avatar, role="TEACHER")
    new_user.password = hash_password(new_user.password)
    create_user(new_user)
    return new_user


def reset_password():
    pass


def get_user(id: str) -> User:
    pass


def update_profile():
    pass
