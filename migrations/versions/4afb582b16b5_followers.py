"""followers

Revision ID: 4afb582b16b5
Revises: 6ddc3e6eda74
Create Date: 2023-04-05 02:11:37.715947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4afb582b16b5'
down_revision = '6ddc3e6eda74'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
