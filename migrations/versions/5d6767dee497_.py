"""empty message

Revision ID: 5d6767dee497
Revises: 
Create Date: 2023-07-06 21:31:16.424801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d6767dee497'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('caretaker',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cat',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('color', sa.String(), nullable=False),
    sa.Column('personality', sa.String(), nullable=False),
    sa.Column('pet_count', sa.Integer(), nullable=False),
    sa.Column('caretaker_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['caretaker_id'], ['caretaker.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cat')
    op.drop_table('caretaker')
    # ### end Alembic commands ###
