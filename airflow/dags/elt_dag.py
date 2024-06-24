from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.operators.python import PythonOperator
import subprocess
from docker.types import Mount


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False
}

def run_elt_script():
    script_path = "/opt/airflow/elt/data_extraction.py"
    result = subprocess.run(["python", script_path],
                             capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Script failed with error: {result.stderr}")
    else:
        print(result.stdout)

def run_data_import():
    script_path = "/opt/airflow/data_import/data_import.py"
    result = subprocess.run(["python", script_path],
                            capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Script failed with error: {result.stderr}")
    else:
        print(result.stdout)



dag = DAG(
    'data_extract',
    default_args=default_args,
    description='Data extraction workflow',
    start_date=datetime(2024,6,11),
    schedule_interval='0 8 * * *',
    catchup=False,
)

t1 = PythonOperator(
    task_id="run_elt_script",
    python_callable=run_elt_script,
    dag=dag
)

t2 = PythonOperator(
    task_id="run_data_import",
    python_callable=run_data_import,
    dag=dag
)

t3 = DockerOperator(
    task_id='dbt_run',
    image='ghcr.io/dbt-labs/dbt-postgres:1.4.7',
    api_version='auto',
    auto_remove=True,
    command='run --profiles-dir /root --project-dir /dbt',
    docker_url='unix://var/run/docker.sock',  # assuming Docker is running on the same host
    network_mode='elt_network',
    mounts=[
        Mount(source='C:/Users/jackt/PycharmProjects/pythonProject/etl_project/dbt_project',
              target='/dbt', type='bind'),
        Mount(source='C:/Users/jackt/.dbt',
              target='/root/', type='bind')
    ],
    mount_tmp_dir=False,
    dag=dag
)

t1 >> t2 >> t3
