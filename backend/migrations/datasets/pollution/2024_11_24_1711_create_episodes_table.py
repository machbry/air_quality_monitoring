"""create episodes table

Revision ID: 2f9a26945c87
Revises: 
Create Date: 2024-11-24 17:11:03.777782

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2f9a26945c87'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

table_name = 'episodes'
table_columns = [
    sa.Column("date_dif", sa.TIMESTAMP, nullable=True),
    sa.Column("code_pol", sa.Integer, nullable=True),
    sa.Column("date_ech", sa.Date, nullable=True),
    sa.Column("code_zone", sa.String, nullable=True),
    sa.Column("etat", sa.String, nullable=True),
    sa.Column("lib_zone", sa.String, nullable=True),
    sa.Column("lib_pol", sa.String, nullable=True)
]


def upgrade() -> None:
    op.create_table(
        table_name,
        *table_columns,
        if_not_exists=True,
        bigquery_clustering_fields=["code_zone", "date_ech"]
    )


def downgrade() -> None:
    op.drop_table(table_name, 
                  if_exists=True)

