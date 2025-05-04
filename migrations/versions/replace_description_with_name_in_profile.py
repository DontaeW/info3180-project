"""Replace description with name in Profile

Revision ID: replace_description_with_name
Revises: 
Create Date: 2024-06-01 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'replace_description_with_name'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Add new 'name' column
    op.add_column('Profile', sa.Column('name', sa.String(length=255), nullable=True))
    # Copy data from 'description' to 'name'
    op.execute('UPDATE "Profile" SET name = description')
    # Drop 'description' column
    op.drop_column('Profile', 'description')

def downgrade():
    # Add back 'description' column
    op.add_column('Profile', sa.Column('description', sa.String(length=255), nullable=True))
    # Copy data from 'name' to 'description'
    op.execute('UPDATE "Profile" SET description = name')
    # Drop 'name' column
    op.drop_column('Profile', 'name')
