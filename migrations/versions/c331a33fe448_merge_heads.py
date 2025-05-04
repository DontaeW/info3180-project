"""Merge heads

Revision ID: c331a33fe448
Revises: 694482ca3e89, replace_description_with_name
Create Date: 2025-05-02 08:49:26.235870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c331a33fe448'
down_revision = ('694482ca3e89', 'replace_description_with_name')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
