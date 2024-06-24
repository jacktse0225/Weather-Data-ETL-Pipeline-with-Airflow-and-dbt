import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import boto3
from datetime import datetime
import os

def download_csv_from_s3(bucket_name, s3_folder_name, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY):
    directory = '/app/'
    directory_w_sub_folder = directory + s3_folder_name
    if not os.path.exists(directory_w_sub_folder):
        os.makedirs(directory_w_sub_folder)
    try:
        file_path_list = []
        s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        objects = s3.list_objects_v2(Bucket=bucket_name, Prefix=s3_folder_name)['Contents']
        csv_files_today = [obj['Key'] for obj in objects if obj['Key'].endswith('.csv') and obj['LastModified'].date() == datetime.today().date()]

        if not csv_files_today:
            raise KeyError("No CSV file created today")

        for csv_file in csv_files_today:
            file_path = os.path.join(directory, csv_file)
            s3.download_file(bucket_name, csv_file, file_path)
            file_path_list.append(file_path)
        print("Data is downloaded")
        return file_path_list

    except KeyError as e:
        print(e)
        return None


def csv_to_df(file_path_list):
    df_list = []
    for file_path in file_path_list:
        df = pd.read_csv(file_path)
        df_list.append(df)
    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df


def insert_data_from_csv(host, port, database, user, password, df, table_name):
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        connection_string = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
        engine = create_engine(connection_string)
        df.to_sql(table_name, engine, if_exists='append', index=False)

        print(f"Data inserted into {table_name} table successfully.")

        # Commit the transaction
        connection.commit()
        print("Data inserted successfully!")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL or inserting data:", error)

def remove_csv_file(file_path_list):
    for file_path in file_path_list:
        os.remove(file_path)
        print(f"CSV file {file_path} removed successfully.")

def main():
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    bucket_name = 'elt-project'
    s3_folder_name = 'python-weather-api/'
    file_path_list = download_csv_from_s3(bucket_name, s3_folder_name, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    df = csv_to_df(file_path_list)
    insert_data_from_csv(
        host="192.168.2.19",
        port="5432",
        database="mydatabase",
        user="user",
        password="password",
        df=df,
        table_name="weather_data"
    )
    remove_csv_file(file_path_list)


if __name__ == "__main__":
    main()