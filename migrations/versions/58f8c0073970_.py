"""empty message

Revision ID: 58f8c0073970
Revises: 891a9041591a
Create Date: 2020-11-02 15:16:38.600169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58f8c0073970'
down_revision = '891a9041591a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('last_seen', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'last_seen')
    # ### end Alembic commands ###
