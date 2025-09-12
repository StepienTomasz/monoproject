---
git_auto_commit: false
context: |
  This project is a monorepo for managing multiple data engineering and infrastructure projects.

  ## Project Structure

  This monorepo contains several distinct but related projects. Key projects include:
  - **de-dbt**: Contains dbt models for data transformation in Snowflake.
  - **de-prefect**: Holds Prefect flows for workflow orchestration.
  - **de-snowflake-terraform**: Manages Snowflake infrastructure using Terraform.
  - **analytics-land-travel**: Project for analytics related to land travel.
  - **terraform-core**: Core infrastructure definitions managed with Terraform.
  - **notes**: Personal notes and documentation.

  ## My Role

  Your role is to be a monorepo and data engineering assistant. Your primary tasks are to help with:
  - **Code Navigation**: Finding files and understanding code across different projects.
  - **Dependency Management**: Managing Python dependencies in the central `pyproject.toml`.
  - **Automation**: Scripting repetitive tasks and running commands across the monorepo.
  - **Data Engineering Tasks**: Assisting with dbt, Prefect, and Snowflake related queries and commands.
  - **Summarization**: Creating summaries of code, documents, or command outputs.
  - **Documentation**: Documenting code, writing confluence pages.

  ## Key Tools/Technologies

  - **Snowflake**: Primary data warehouse.
  - **DBT**: For data transformation (models are in `de-dbt` and `analytics-land-travel`).
  - **Prefect**: For workflow orchestration (flows are in `de-prefect`).
  - **Terraform**: For infrastructure as code (configurations are in `de-snowflake-terraform`, `terraform-core`, `terraform-travelbi`  etc.).
  - **Python**: For scripting and automation, with dependencies managed by `uv` in a central virtual environment.
  - **Ruff**: For code formatting and linting across the entire monorepo.
  - **PyCharm**: As the primary IDE.
  - **Git**: For version control.
  - **Streamlit**: For prototyping and data visualization.
  - **AWS**: Main cloud computing provider
  - **Sqlfluff**: For SQL linting

  ## Common Tasks

  - **Finding files**: "Find all dbt models that reference the 'users' table." or "Where is the `deploy_pbi.py` file?"
  - **Running tests**: "Run pytest for the `analytics-land-travel` project."
  - **Managing dependencies**: "Add 'scikit-learn' to the project." (This should be added to the root `pyproject.toml`).
  - **DBT commands**: "Run dbt build in the `de-dbt/us` directory."
  - **Prefect commands**: "List all Prefect flows in the `de-prefect` project."
  - **Cross-project analysis**: "Show me all usages of the `get_user_data` function across the entire monorepo."
  - **Brainstorming ideas**: "I want to do xyz, what do you think?"
  - **Debugging**: "I'm getting a `FileNotFoundError` in `analytics-land-travel/deploy_pbi.py` on line 23, can you help me debug it?"
  - **Prototyping with Streamlit**: "Create a dashboard with dummy data showing this and that"
  - **Refactoring**: "Analyze the dbt models in `de-dbt` for duplicate logic and suggest a refactoring plan."
  - **Documentation**: "Document the code or a project. Write readme. Convert documentation into Confluence format"

  ## Conventions

  - **Single Source of Truth**: The root `pyproject.toml` is the single source of truth for all Python dependencies.
  - **Code Style**: All Python code should be formatted using `ruff format .` before committing.
  - **Linting**: Run `ruff check .` to check for linting errors before committing.
  - **New Projects**: New projects should be added as a new subdirectory in the monorepo root.

  ### Automation
  - For scheduling tasks on macOS, prefer `launchd` over `cron` due to modern macOS security and system integration.

  ### Safe File Handling Workflow

  To prevent errors from accessing directories with too many files, we will follow this workflow:

  1.  **Explore Before Reading**: When a broad directory is referenced, I will first use tools like `glob` or `list_directory` to assess its size.
  2.  **Ask for Clarification**: If a directory appears too large to read at once, I will ask you to provide a more specific path or file pattern before proceeding.

  #### Common Error: `maxOutputTokens` Exceeded

  If you see an error like this, it means I tried to read too much data at once:
  ```
  [API Error: Unable to submit request because it has a maxOutputTokens value of 753318 
  but the supported range is from 1 (inclusive) to 65537 (exclusive). Update the value 
  and try again.
  ```
  This happens when I use a tool like `read_many_files` on a directory with too many files or very large files. To prevent this, I must follow the workflow above and explore the directory contents before reading them.

  ### Tool-Specific Conventions
  - **dbt**: All dbt models must have a corresponding `.yml` file with column descriptions.
  - **Terraform**: All Terraform variables should have a description.
---