"""empty message

Revision ID: a68bf50b0489
Revises: None
Create Date: 2016-11-22 11:10:01.003609

"""

# revision identifiers, used by Alembic.
revision = 'a68bf50b0489'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('challenges',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=1024), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('materialID', sa.Integer(), nullable=True),
    sa.Column('practiceID', sa.Integer(), nullable=True),
    sa.Column('programID', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('knowledges',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=1024), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('idx_type', table_name='questions')
    op.alter_column(u'submit_problem', 'code',
               existing_type=mysql.TEXT(),
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(u'submit_problem', 'code',
               existing_type=mysql.TEXT(),
               nullable=True)
    op.create_index('idx_type', 'questions', ['type'], unique=False)
    op.drop_table('knowledges')
    op.drop_table('challenges')
    ### end Alembic commands ###