# Backend for air quality monitoring

## Installing

### Prerequisites:

1. Python (≥ `3.11`) installed on your system.
2. Ensure you have `poetry` installed (you can also use `pip`)

### Steps:

1. **Clone the GitHub Repository:**

   Clone the GitHub repository you want to install locally using the `git clone` command.

   ```bash
   git clone https://github.com/machbry/air_quality_monitoring
   ```

2. **Navigate to the backend directory:**

   Use the `cd` command to navigate into the backend directory.

   ```bash
   cd air_quality_monitoring/backend
   ```

3. **Configure `poetry` to create a Virtual Environment inside the project:**

   Ensure that poetry will create a `.venv` directory into the project with the command:

   ```bash
   poetry config virtualenvs.in-project true
   ```

4. **Install Project Dependencies using `poetry`:**

   Use `poetry` to install the project dependencies.

   ```bash
   poetry install --with dev
   ```

   This will read the `pyproject.toml` file in the repository and install all the dependencies specified.

5. **Make sure everything is all right using `poetry env info`:**

   ```bash
   poetry env info
   ```

6. **Activate the Virtual Environment:**

   ```bash
   poetry shell
   ```
