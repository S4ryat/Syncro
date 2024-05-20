
"""migration

Revision ID: 3d12004da810
Revises: e700030bb685
Create Date: 2024-05-20 19:57:05.227377

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d12004da810'
down_revision: Union[str, None] = 'e700030bb685'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
