"""empty message

Revision ID: de5f82a0a6bb
Revises: 1d204e7ba433
Create Date: 2016-11-06 19:17:40.740760

"""

# revision identifiers, used by Alembic.
revision = 'de5f82a0a6bb'
down_revision = '1d204e7ba433'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('submit_problem', 'code',
               existing_type=mysql.TEXT(),
               nullable=False)
    op.alter_column('submit_problem', 'status',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('submit_problem', 'status',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    op.alter_column('submit_problem', 'code',
               existing_type=mysql.TEXT(),
               nullable=True)
    ### end Alembic commands ###