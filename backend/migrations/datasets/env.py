import os
from logging.config import fileConfig

from dataclasses import dataclass

from sqlalchemy import create_engine, MetaData
from alembic import context


GOOGLE_PROJECT = os.environ.get("GOOGLE_PROJECT", "dev-air-quality-monitoring")

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


@dataclass
class Dataset:
    dialect: str
    name: str
    location: str
    gcp_project: str

    @property
    def url(self):
        return f"{self.dialect}://{self.gcp_project}/{self.name}"
    
    @property
    def metadata(self):
        return MetaData(schema=self.name)
    
    @property
    def engine(self):
        return create_engine(self.url, location=self.location)


def get_dataset_from_config(ini_config, gcp_project):
    # retrieve dataset informations from ini file
    ini_section = ini_config.get_section(ini_config.config_ini_section)

    return Dataset(dialect=ini_section["dialect_name"],
                   name=ini_section["dataset_name"],
                   location=ini_section["dataset_location"],
                   gcp_project=gcp_project)


def run_migrations_online():
    dataset = get_dataset_from_config(config, GOOGLE_PROJECT)

    with dataset.engine.connect() as connection:
        context.configure(connection=connection,
                          target_metadata=dataset.metadata,
                          compare_type=True,
                          dialect_name=dataset.dialect)

        with context.begin_transaction():
            context.run_migrations()

def run_migrations_offline():
    dataset = get_dataset_from_config(config, GOOGLE_PROJECT)

    context.configure(url=dataset.url, 
                      target_metadata=dataset.metadata,
                      dialect_name=dataset.dialect)

    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
