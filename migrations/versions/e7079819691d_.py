"""empty message

Revision ID: e7079819691d
Revises: 3e7c9df63fd0
Create Date: 2020-11-02 16:21:37.954004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7079819691d'
down_revision = '3e7c9df63fd0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('date_of_failure', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'date_of_failure')
    # ### end Alembic commands ###
