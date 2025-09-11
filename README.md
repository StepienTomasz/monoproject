# Monorepo for Data & Infrastructure Projects

## Overview

This repository serves as a central monorepo for managing a variety of data engineering, analytics, and infrastructure projects. It is designed to provide a unified development environment while allowing each sub-project to maintain its own independent Git history and deployment lifecycle.

## Project Structure

The monorepo contains several distinct but related projects. Key projects include:

-   `de-dbt`: Contains dbt models for data transformation in Snowflake.
-   `de-prefect`: Holds Prefect flows for workflow orchestration.
-   `de-snowflake-terraform`: Manages Snowflake infrastructure using Terraform.
-   `analytics-land-travel`: Project for analytics related to land travel.
-   `terraform-core`: Core infrastructure definitions managed with Terraform.
-   `notes`: Personal notes and documentation.
-   `agm-replacement`: Project for the AGM replacement.
-   `de-prefect-docker`: Docker infrastructure for Prefect agents and runners.
-   `terraform-github`: Terraform configuration for managing the GitHub organization.
-   `terraform-travelbi`: Terraform infrastructure for the Travel BI team.

## Version Control Strategy

This repository utilizes a "mono-repo of multi-repos" approach.
˚
-   **Root Repository:** The root directory is a Git repository that tracks the shared configuration files (e.g., `pyproject.toml`, `ruff.toml`) and this README.
-   **Sub-project Repositories:** Each sub-project directory (like `de-dbt`, `de-prefect`, etc.) is its own independent Git repository.

The sub-project directories are listed in the root `.gitignore` file. **This is why they do not appear in the file list on GitHub for this central repository.** This setup allows you to work on all projects from a single IDE window while keeping the version history for each project separate.

You can `cd` into any sub-project directory to use `git` commands (like `commit`, `push`, `pull`) specific to that project.

## Development Environment

-   **Dependencies**: All Python dependencies for all projects are managed centrally in the root `pyproject.toml` file and installed using `uv`. This ensures a single, consistent environment.
-   **Linting & Formatting**: Code quality is maintained across all projects using `ruff`. Please run `ruff format .` and `ruff check .` before committing to any of the sub-repositories.
