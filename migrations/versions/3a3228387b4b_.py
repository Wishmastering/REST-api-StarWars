"""empty message

Revision ID: 3a3228387b4b
Revises: 936f9e4d3333
Create Date: 2022-09-22 02:17:29.720861

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3a3228387b4b'
down_revision = '936f9e4d3333'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favorites', sa.Column('planets_id', sa.Integer(), nullable=False))
    op.drop_constraint('favorites_ibfk_1', 'favorites', type_='foreignkey')
    op.create_foreign_key(None, 'favorites', 'planets', ['planets_id'], ['id'])
    op.drop_column('favorites', 'planet_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favorites', sa.Column('planet_id', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'favorites', type_='foreignkey')
    op.create_foreign_key('favorites_ibfk_1', 'favorites', 'planets', ['planet_id'], ['id'])
    op.drop_column('favorites', 'planets_id')
    # ### end Alembic commands ###
