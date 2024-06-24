import requests
import pandas as pd
from datetime import datetime
import os
import boto3
from botocore.exceptions import NoCredentialsError

def extracting_weather_data_by_city(api_key, city):
    try:
        result = requests.get(f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}')
        result.raise_for_status()

        try:
            data = result.json()["location"]
        except KeyError:
            raise KeyError(f"The key 'location' is not found for the city: {city}")
        except ValueError:
            raise ValueError("Invalid JSON received from the API")

        return data

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def dict_to_csv_string(data):
    df = pd.json_normalize(data)
    csv_string = df.to_csv(index=False)
    return csv_string

def upload_to_s3(csv_string, bucket_name, s3_key):
    s3 = boto3.client('s3')
    try:
        s3.put_object(Bucket=bucket_name, Key=s3_key, Body=csv_string)
        print(f"Successfully uploaded {s3_key} to {bucket_name}")
    except NoCredentialsError:
        print("Credentials not available")



def main():
    api_key = os.getenv('API_KEY')
    city = 'london'
    bucket_name = 'elt-project'
    s3_folder_name = 'python-weather-api/'
    weather_data = extracting_weather_data_by_city(api_key, city)
    csv_string = dict_to_csv_string(weather_data)
    s3_key = f"{s3_folder_name}{datetime.today().strftime('%Y_%m_%d')}_{city}_weather.csv"
    upload_to_s3(csv_string, bucket_name, s3_key)

if __name__ == "__main__":
    main()
