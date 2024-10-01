"""empty message

Revision ID: 55e87825c3e5
Revises: 27c755f40a17
Create Date: 2024-09-30 17:59:07.011859

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '55e87825c3e5'
down_revision: Union[str, None] = '27c755f40a17'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
