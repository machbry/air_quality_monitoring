# Backend for air quality monitoring

## Installing

### Prerequisites:

1. Follow installation steps [here](../README.md)
2. Python (≥ `3.11`) installed on your system.
3. Ensure you have `poetry` installed (you can also use `pip`)

### Steps:

1. **Navigate to the backend directory:**

   ```bash
   cd air_quality_monitoring/backend
   ```

2. **Configure `poetry` to create a Virtual Environment inside the project:**

   Ensure that poetry will create a `.venv` directory into the project with the command:

   ```bash
   poetry config virtualenvs.in-project true
   ```

3. **Install Project Dependencies using `poetry`:**

   Use `poetry` to install the project dependencies.

   ```bash
   poetry install --with dev
   ```

   This will read the `pyproject.toml` file in the repository and install all the dependencies specified.

4. **Make sure everything is all right using `poetry env info`:**

   ```bash
   poetry env info
   ```

5. **Activate the Virtual Environment:**

   ```bash
   poetry shell
   ```

## Datasets management

Each dataset has a folder (folder name = dataset name) in folder migrations/datasets with its revisions. Dataset must exists before doing revisions. 

1. **Navigate to the migrations directory:**

   ```bash
   cd migrations
   ```

2. **Create a new revision with alembic (optional)**

   ```bash
   alembic --name <dataset_name> revision -m "<revision description>"
   ```

   This will create a .py file in folder migrations/<dataset_name>.
   Then modify fonctions upgrade() and downgrade() accordingly to your wanted revision.
   
3. **Update schemas with alembic**

   ```bash
   alembic --name <dataset_name> upgrade head
   ```

   This will apply revisions in folder migrations/<dataset_name> up to the latest one.

4. **Add a new dataset (optional)**

   Create dataset on bigquery with a given name and location.

   Describe the dataset in the alembic.ini file (i.e. add a section) :

   ```
   [<dataset_name>]
   version_locations = ./datasets/<dataset_name>
   dataset_name = <dataset_name>
   dataset_location = <dataset_location>
   ```
