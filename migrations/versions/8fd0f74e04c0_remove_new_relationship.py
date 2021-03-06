"""Remove new relationship

Revision ID: 8fd0f74e04c0
Revises: 0182c0980a9c
Create Date: 2020-05-11 15:28:35.804664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fd0f74e04c0'
down_revision = '0182c0980a9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('posts_blog_id_fkey', 'posts', type_='foreignkey')
    op.drop_column('posts', 'blog_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('blog_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('posts_blog_id_fkey', 'posts', 'blogs', ['blog_id'], ['id'])
    # ### end Alembic commands ###
