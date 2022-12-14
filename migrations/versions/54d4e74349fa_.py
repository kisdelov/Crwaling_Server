"""empty message

Revision ID: 54d4e74349fa
Revises: 7d2f7b5531ee
Create Date: 2022-09-28 15:48:48.567574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54d4e74349fa'
down_revision = '7d2f7b5531ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('crawling_product', 'category2')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('crawling_product', sa.Column('category2', sa.VARCHAR(length=300), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
