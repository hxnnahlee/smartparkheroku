"""empty message

Revision ID: 6abb0bb3013c
Revises: c7b83f505f6b
Create Date: 2019-11-20 17:29:00.770429

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6abb0bb3013c'
down_revision = 'c7b83f505f6b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('average', sa.Column('time_parked', sa.Float(), nullable=True))
    op.drop_column('average', 'avg')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('average', sa.Column('avg', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.drop_column('average', 'time_parked')
    # ### end Alembic commands ###
