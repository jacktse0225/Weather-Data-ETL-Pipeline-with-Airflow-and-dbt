# Data Engineering Project: Weather Data Pipeline

This project demonstrates my data engineering skills, particularly in setting up and managing data pipelines using Docker, Apache Airflow, dbt, and PostgreSQL. The pipeline extracts weather data, transforms it using dbt, and loads it into a PostgreSQL database.

## Project Overview

The goal of this project is to build an end-to-end data pipeline that:
1. Extracts weather data from an external API.
2. Loads the raw data into a PostgreSQL database.
3. Transforms the raw data using dbt (data build tool).
4. Loads the transformed data back into the PostgreSQL database.

## Key Technologies

- **Docker:** Containerizes the entire application for easy deployment and environment consistency.
- **Apache Airflow:** Orchestrates the ETL (Extract, Transform, Load) pipeline.
- **dbt (data build tool):** Transforms the raw data into a more useful and structured format.
- **PostgreSQL:** Serves as the database for storing raw and transformed data.

## Project Structure

your-project/
│
├── airflow/
│ └── dags/
│ └── elt_dag.py
│
├── dbt_project/
│ ├── macros/
│ ├── models/
│ └── tests/
│
├── .env
├── Dockerfile
└── docker-compose.yml

