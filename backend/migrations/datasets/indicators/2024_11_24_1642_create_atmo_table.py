"""create atmo table

Revision ID: caa8b233f065
Revises: 
Create Date: 2024-11-24 16:42:03.117687

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'caa8b233f065'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

table_name = 'atmo'
table_columns = [
    sa.Column("code_no2", sa.Integer, nullable=True),
    sa.Column("code_o3", sa.Integer, nullable=True),
    sa.Column("code_pm10", sa.Integer, nullable=True),
    sa.Column("code_pm25", sa.Integer, nullable=True),
    sa.Column("code_qual", sa.Integer, nullable=True),
    sa.Column("code_so2", sa.Integer, nullable=True),
    sa.Column("code_zone", sa.String, nullable=True),
    sa.Column("coul_qual", sa.String, nullable=True),
    sa.Column("date_dif", sa.TIMESTAMP, nullable=True),
    sa.Column("date_ech", sa.Date, nullable=True),
    sa.Column("epsg_reg", sa.String, nullable=True),
    sa.Column("lib_qual", sa.String, nullable=True),
    sa.Column("lib_zone", sa.String, nullable=True),
    sa.Column("source", sa.String, nullable=True),
    sa.Column("type_zone", sa.String, nullable=True),
    sa.Column("x_reg", sa.Float, nullable=True),
    sa.Column("x_wgs84", sa.Float, nullable=True),
    sa.Column("y_reg", sa.Float, nullable=True),
    sa.Column("y_wgs84", sa.Float, nullable=True),
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
