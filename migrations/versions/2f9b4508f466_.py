"""empty message

Revision ID: 2f9b4508f466
Revises: 
Create Date: 2020-09-23 04:58:36.288782

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f9b4508f466'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('role', sa.String(), nullable=False),
    sa.Column('avatar', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('course',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(length=400), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('close_date', sa.DateTime(), nullable=False),
    sa.Column('teacher_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['teacher_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('enrollment',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('enroll_date', sa.DateTime(), nullable=True),
    sa.Column('student_id', sa.String(), nullable=True),
    sa.Column('course_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('enrollment')
    op.drop_table('course')
    op.drop_table('user')
    # ### end Alembic commands ###