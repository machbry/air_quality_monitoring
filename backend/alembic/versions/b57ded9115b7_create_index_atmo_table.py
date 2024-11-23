"""create index atmo table

Revision ID: b57ded9115b7
Revises: 
Create Date: 2024-11-23 19:13:03.712998

"""
from typing import Sequence, Union

from sqlalchemy import Column, Integer, String, Float, Date, TIMESTAMP
from alembic import op


table_name = 'atmo'
dataset_name = 'index'
table_columns = [
    Column("code_no2", Integer, nullable=True),
    Column("code_o3", Integer, nullable=True),
    Column("code_pm10", Integer, nullable=True),
    Column("code_pm25", Integer, nullable=True),
    Column("code_qual", Integer, nullable=True),
    Column("code_so2", Integer, nullable=True),
    Column("code_zone", String, nullable=True),
    Column("coul_qual", String, nullable=True),
    Column("date_dif", TIMESTAMP, nullable=True),
    Column("date_ech", Date, nullable=True),
    Column("epsg_reg", String, nullable=True),
    Column("lib_qual", String, nullable=True),
    Column("lib_zone", String, nullable=True),
    Column("source", String, nullable=True),
    Column("type_zone", String, nullable=True),
    Column("x_reg", Float, nullable=True),
    Column("x_wgs84", Float, nullable=True),
    Column("y_reg", Float, nullable=True),
    Column("y_wgs84", Float, nullable=True),
]

# revision identifiers, used by Alembic.
revision: str = 'b57ded9115b7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        table_name,
        *table_columns,
        if_not_exists=True,
        schema=dataset_name,
        bigquery_clustering_fields=["code_zone", "date_ech"]
    )

def downgrade() -> None:
    op.drop_table(table_name, 
                  schema=dataset_name,
                  if_exists=True)
