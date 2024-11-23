from sqlalchemy import Column, Integer, MetaData, String, Float, Date, TIMESTAMP, Table

metadata = MetaData()

atmo_table = Table('atmo', metadata,
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
    schema='index',
    bigquery_clustering_fields=["code_zone", "date_ech"]
)
