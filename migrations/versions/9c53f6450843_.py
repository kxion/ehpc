"""empty message

Revision ID: 9c53f6450843
Revises: 3f766510a095
Create Date: 2016-10-12 10:18:46.054085

"""

# revision identifiers, used by Alembic.
revision = '9c53f6450843'
down_revision = '3f766510a095'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('course_users',
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['courses.id'], )
    )
    op.drop_table('students')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.drop_table('course_users')
    ### end Alembic commands ###
