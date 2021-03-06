"""article add time

Revision ID: 8d5a4ae56094
Revises: 26cdedd8f618
Create Date: 2020-04-14 17:05:36.889916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d5a4ae56094'
down_revision = '26cdedd8f618'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('time', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'time')
    # ### end Alembic commands ###
