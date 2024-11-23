# Backend for air quality monitoring

## Installing

### Prerequisites:

1. Follow installation steps [here](../README.md)
2. Python (≥ `3.11`) installed on your system.
3. Ensure you have `poetry` installed (you can also use `pip`)

### Steps:

1. **Navigate to the backend directory:**

   Use the `cd` command to navigate into the backend directory.

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

## Database management
   
1. **Update DB schema with alembic**

   ```bash
   alembic upgrade head
   ```
