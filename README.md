# ETL Data Pipeline with Airflow, DBT, and AWS S3

## Project Overview

This project demonstrates a complete ETL data pipeline setup using Apache Airflow, dbt, PostgreSQL, and AWS S3. The pipeline extracts data from an API, stores it in AWS S3, loads it into a PostgreSQL database, and transforms it using dbt. The project showcases data engineering skills, particularly in managing data pipelines.

## ETL Pipeline Tasks

The ETL pipeline consists of three main tasks: data extraction, data import, and data transformation. Each task is managed by Apache Airflow using Python and Docker operators. Here’s a detailed explanation of each task:

![dbt_workflow_map](https://github.com/jacktse0225/elt_project/assets/122648649/e7251d2f-39a4-495d-a584-edb9bfa992ea)


### Task 1: Data Extraction

**Operator:** `PythonOperator`

**Function:** `run_elt_script`

**Description:** This task is responsible for extracting data from an external API and storing it in an AWS S3 bucket. The `run_elt_script` function runs a Python script (`data_extraction.py`) located in the `/opt/airflow/elt` directory. The script fetches data from the API and saves it to S3, making it available for subsequent steps in the pipeline.

### Task 2: Data Import

**Operator:** `PythonOperator`

**Function:** `run_data_import`

**Description:** This task imports the data stored in the AWS S3 bucket into a PostgreSQL database. The run_data_import function executes a Python script (data_import.py) located in the /opt/airflow/data_import directory. The script retrieves the data from S3 and loads it into the PostgreSQL database, preparing it for transformation.

### Task 3: Data Transformation
**Operator:** `DockerOperator`

**Image:** `ghcr.io/dbt-labs/dbt-postgres:1.4.7`

**Description:** This task transforms the data in the PostgreSQL database using dbt (data build tool). The dbt_run task uses a Docker container to run dbt commands, specifying the project and profiles directories. dbt applies transformation models to the raw data, producing clean and structured data ready for analysis.

## Technologies Used

- **Apache Airflow**: For orchestrating the ETL pipeline.
- **dbt**: For transforming data.
- **PostgreSQL**: As the database for storing data.
- **AWS S3**: For storing extracted data from the API.
- **Docker**: For containerizing the application and its dependencies.

## Project Structure

- `docker-compose.yml`: Defines the services and their configurations.
- `Dockerfile`: Specifies the environment setup for Airflow.
- `airflow/`: Contains Airflow DAGs and scripts.
  - `dags/`
  - `elt_script/`
  - `data_import/`
- `dbt_project/`: Contains dbt models, macros, and tests.
- `.env`: Contains environment variables for sensitive information.

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- AWS account with S3 bucket

### Installation

1. **Clone the repository**:

    ```bash
    git clone
    cd your-repository-name
    ```

2. **Set up environment variables**:

    Create a `.env` file with the following content and the actual access key:

    ```env
    API_KEY=your_key
    AWS_ACCESS_KEY_ID=your_key
    AWS_SECRET_ACCESS_KEY=your_key
    AIRFLOW__CORE__FERNET_KEY=your_key
    ```

3. **Run Docker Compose**:

    ```bash
    docker-compose up --build
    ```

### Usage

Once the services are up, you can access the Airflow webserver at `http://localhost:8080`. Use the following credentials:

- **Username**: airflow
- **Password**: password

### Data Flow

1. **Extract**: Data is extracted from an API and stored in AWS S3.
2. **Load**: The extracted data stored in S3 is then imported into the PostgreSQL database.
3. **Transform**: The data in PostgreSQL is transformed using dbt.

### Scheduling

The entire process, from extracting data from the API to storing it in S3, importing it into PostgreSQL, and transforming it using dbt, is scheduled and managed using Airflow.

### Notes

- Ensure your AWS credentials and S3 bucket configuration are correctly set in the `.env` file.
- The PostgreSQL database will be initialized with a sample dataset.
- Ensure your dbt profile matches the database configuration.

## Contributing

Feel free to open issues or submit pull requests for improvements.

## License

This project is licensed under the MIT License.
