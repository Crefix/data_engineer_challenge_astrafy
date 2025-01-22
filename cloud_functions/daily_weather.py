import requests
import logging
import os
from google.cloud import bigquery
from google.cloud.logging import Client as LoggingClient
from google.cloud.logging.handlers import CloudLoggingHandler
from datetime import datetime, timezone
from google.cloud import secretmanager

def get_secret(secret_name, project_id = os.environ["PROJECT_ID"]):
    """Fetches the secret value from Google Secret Manager."""
    client = secretmanager.SecretManagerServiceClient()
    secret_path = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
    response = client.access_secret_version(request={"name": secret_path})
    return response.payload.data.decode("UTF-8")


def fetch_weather_data():
    """Fetches current weather data for Chicago using the OpenWeather API"""
    logger = logging.getLogger("fetch_weather_data")
    try:
        logger.info("Fetching current weather data from OpenWeather API.")

        api_key = get_secret("OPENWEATHER")
        if not api_key:
            raise ValueError("API key is not set. Please configure the secret in Secret Manager.")

        # OpenWeather API setup
        lat = 41.85003  # Latitude for Chicago
        lon = -87.65005  # Longitude for Chicago
        url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'

        # API request
        response = requests.get(url)
        if response.status_code != 200:
            logger.error(f"API request failed with status {response.status_code}")
            response.raise_for_status()

        data = response.json()
        logger.info("Successfully fetched weather data from OpenWeather API")
        return data
    except Exception as e:
        logger.exception(f"Error while fetching weather data: {e}")
        raise

def insert_data_into_bigquery(data):
    """Inserts fetched weather data into BigQuery"""
    logger = logging.getLogger("insert_data_into_bigquery")
    try:
        logger.info("Inserting weather data into BigQuery")
        
        # BigQuery setup
        client = bigquery.Client(project="tenacious-torus-447715-b4")
        dataset_id = 'Chicago_Taxi_Trips'
        table_id = 'chicago_weather'

        table_ref = client.dataset(dataset_id).table(table_id)
        table = client.get_table(table_ref)

        # Prepare data for insertion
        rows_to_insert = [{
            "temperature": data["main"]["temp"],
            "timestamp": datetime.fromtimestamp(data["dt"], tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S'),
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "weather_main": data["weather"][0]["main"],
            "weather_description": data["weather"][0]["description"]
        }]
        
        # Insert rows into BigQuery
        errors = client.insert_rows_json(table, rows_to_insert)
        if errors:
            logger.error(f"Error inserting rows into BigQuery: {errors}")
            raise Exception(f"Error inserting rows: {errors}")

        logger.info("Data successfully inserted into BigQuery")
    except Exception as e:
        logger.exception(f"Error while inserting data into BigQuery: {e}")
        raise

def fetch_weather_and_log(request):
    # Initialize Cloud Logging
    logging_client = LoggingClient()
    handler = CloudLoggingHandler(logging_client)
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(handler)

    logger = logging.getLogger("fetch_weather_and_log")

    try:
        logger.info("Starting daily weather data fetch and insertion")

        # Fetch and insert weather data
        data = fetch_weather_data()
        insert_data_into_bigquery(data)

        logger.info("Daily weather data fetch and insertion completed successfully")
        return "Success!"
    except Exception as e:
        logger.exception(f"An error occurred: {e}")
        raise
