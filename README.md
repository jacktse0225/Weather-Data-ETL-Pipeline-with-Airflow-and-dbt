# ETL Data Pipeline with Airflow, DBT, and AWS S3

## Project Overview

This project demonstrates a complete ETL data pipeline setup using Apache Airflow, dbt, PostgreSQL, and AWS S3. The pipeline extracts data from an API, stores it in AWS S3, loads it into a PostgreSQL database, and transforms it using dbt. The project showcases data engineering skills, particularly in managing data pipelines.

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
    git clone https://github.com/yourusername/your-repository-name.git
    cd your-repository-name
    ```

2. **Set up environment variables**:

    Create a `.env` file with the following content:

    ```env
    POSTGRES_DB=mydatabase
    POSTGRES_USER=user
    POSTGRES_PASSWORD=password
    AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgres+psycopg2://airflow:airflow@postgres/airflow
    AIRFLOW__CORE__FERNET_KEY=your_fernet_key
    AIRFLOW__WEBSERVER__DEFAULT__USER__USERNAME=airflow
    AIRFLOW__WEBSERVER__DEFAULT__USER__PASSWORD=password
    AIRFLOW__WWW_USER_USERNAME=airflow
    AIRFLOW__WWW_USER_PASSWORD=password
    AIRFLOW__WEBSERVER__SECRET_KEY=secret
    API_KEY=your_api_key
    AWS_ACCESS_KEY_ID=your_aws_access_key_id
    AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
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
