"""empty message

Revision ID: cc7bb8f741c8
Revises: 
Create Date: 2022-09-28 15:47:38.932652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc7bb8f741c8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('crawling_shop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('createdDate', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('modifiedDate', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('name', sa.String(length=300), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('production_crawling_shop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('createdDate', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('modifiedDate', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('name', sa.String(length=300), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('crawling_product',
    sa.Column('createdDate', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('modifiedDate', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=300), nullable=True),
    sa.Column('category', sa.String(length=300), nullable=True),
    sa.Column('group', sa.String(length=300), nullable=True),
    sa.Column('member', sa.String(length=300), nullable=True),
    sa.Column('productUrl', sa.String(), nullable=True),
    sa.Column('activate', sa.Boolean(create_constraint=True), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('onSalePrice', sa.Float(), nullable=True),
    sa.Column('onSale', sa.Boolean(create_constraint=True), nullable=True),
    sa.Column('shop_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['shop_id'], ['crawling_shop.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('production_crawling_product',
    sa.Column('createdDate', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('modifiedDate', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=300), nullable=True),
    sa.Column('category', sa.String(length=300), nullable=True),
    sa.Column('group', sa.String(length=300), nullable=True),
    sa.Column('member', sa.String(length=300), nullable=True),
    sa.Column('productUrl', sa.String(), nullable=True),
    sa.Column('activate', sa.Boolean(create_constraint=True), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('onSalePrice', sa.Float(), nullable=True),
    sa.Column('onSale', sa.Boolean(create_constraint=True), nullable=True),
    sa.Column('shop_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['shop_id'], ['production_crawling_shop.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('production_crawling_product')
    op.drop_table('crawling_product')
    op.drop_table('production_crawling_shop')
    op.drop_table('crawling_shop')
    # ### end Alembic commands ###
