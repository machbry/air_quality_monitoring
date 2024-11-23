from logging.config import fileConfig

from sqlalchemy import create_engine
from alembic import context

from air_quality.database.models import metadata

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# target_metadata = None

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

engine = create_engine('bigquery://dev-air-quality-monitoring/index',
                       location='europe-west1')

target_metadata = metadata

context.configure(
    connection=engine.connect(),
    target_metadata = target_metadata,
    compare_type=True,
    dialect_name="bigquery"
)


def run_migrations_online():
    with engine.connect() as connection:
        context.configure(connection=connection)

        with context.begin_transaction():
            context.run_migrations()

def run_migrations_offline():
    url = 'bigquery://dev-air-quality-monitoring/index'
    context.configure(url=url, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
