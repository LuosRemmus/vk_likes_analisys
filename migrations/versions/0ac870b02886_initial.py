"""initial

Revision ID: 0ac870b02886
Revises: 
Create Date: 2023-08-09 17:41:36.002113

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0ac870b02886'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('user_id', sa.String(), nullable=False),
                    sa.Column('first_name', sa.String(), nullable=True),
                    sa.Column('last_name', sa.String(), nullable=True),
                    sa.Column('city', sa.String(), nullable=True),
                    sa.Column('country', sa.String(), nullable=True),
                    sa.Column('bdate', sa.String(), nullable=True),
                    sa.Column('sex', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
