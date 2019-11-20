"""empty message

Revision ID: 83eb4cbb0abd
Revises: 5eba4824505e
Create Date: 2019-11-07 09:30:29.175751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "83eb4cbb0abd"
down_revision = "5eba4824505e"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "interests",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "users_interests",
        sa.Column("interest_id", sa.Integer(), nullable=True),
        sa.Column("user_id", sa.BigInteger(), nullable=True),
        sa.ForeignKeyConstraint(["interest_id"], ["interests.id"]),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
    )
    op.create_table(
        "projects_interests",
        sa.Column("interest_id", sa.Integer(), nullable=True),
        sa.Column("project_id", sa.BigInteger(), nullable=True),
        sa.ForeignKeyConstraint(["interest_id"], ["interests.id"]),
        sa.ForeignKeyConstraint(["project_id"], ["projects.id"]),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("projects_interests")
    op.drop_table("users_interests")
    op.drop_table("interests")
    # ### end Alembic commands ###