from flask_sqlalchemy import SQLAlchemy

from afc_core.user.utils import hash_password
from afc_core.models.user import User


def get_user_by_email(email: str) -> User:
    user = User.query.filter_by(email=email).first()
    return user


def get_users():
    users = User.query.all()
    return users


def register_student(db: SQLAlchemy, form, avatar: str):
    new_user = User(email=form['email'], password=form['password'],
                    first_name=form['first_name'], last_name=form['last_name'], avatar=avatar, role="STUDENT")

    new_user.password = hash_password(new_user.password.encode('utf-8'))
    db.session.add(new_user)
    db.session.commit()


def register_teacher():
    pass


def reset_password():
    pass


def get_user(id: str) -> User:
    pass


def update_profile():
    pass
