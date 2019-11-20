"""empty message

Revision ID: 0858717b48c7
Revises: 6692fc705e4c
Create Date: 2019-11-20 17:02:00.585936

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0858717b48c7'
down_revision = '6692fc705e4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('average')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('average',
    sa.Column('avg', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('avg', name='average_pkey')
    )
    # ### end Alembic commands ###
