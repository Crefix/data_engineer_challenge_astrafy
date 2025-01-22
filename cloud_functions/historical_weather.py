import requests
import logging
import google.cloud.logging
from google.cloud import bigquery
from google.cloud.logging.handlers import CloudLoggingHandler

def fetch_historical_weather(request):
    """Fetches historical weather data"""
    # Initialize Cloud Logging
    log_name = "historical_weather"
    gcloud_logging_client = google.cloud.logging.Client()
    gcloud_logging_handler = CloudLoggingHandler(
        gcloud_logging_client, name=log_name
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.WARNING)

    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(gcloud_logging_handler)
    logger.addHandler(stream_handler)

    try:
        # Log function start
        logger.info("Starting historical weather data fetch")

        # Open-Meteo API setup
        url = (
            "https://archive-api.open-meteo.com/v1/archive"
            "?latitude=41.85&longitude=-87.65"
            "&start_date=2023-06-01&end_date=2023-12-31"
            "&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
        )
        logger.info(f"API URL: {url}")

        # Fetch weather data
        response = requests.get(url)
        if response.status_code != 200:
            logger.error(f"Failed to fetch data. Status code: {response.status_code}")
            response.raise_for_status()
        
        weather_data = response.json()
        logger.info("Successfully fetched weather data from API")

        # BigQuery setup
        client = bigquery.Client()
        dataset_id = "Chicago_Taxi_Trips"
        table_id = "chicago_weather"
        table_ref = client.dataset(dataset_id).table(table_id)

        # Prepare rows for insertion
        rows_to_insert = []
        hourly_data = weather_data["hourly"]
        for i, timestamp in enumerate(hourly_data["time"]):
            row = {
                "timestamp": timestamp,
                "temperature": hourly_data["temperature_2m"][i],
                "humidity": hourly_data["relative_humidity_2m"][i],
                "wind_speed": hourly_data["wind_speed_10m"][i],
            }
            rows_to_insert.append(row)

        # Insert data into BigQuery
        errors = client.insert_rows_json(table_ref, rows_to_insert)
        if errors:
            logger.error(f"Failed to insert rows into BigQuery: {errors}")
        else:
            logger.info(f"Successfully inserted {len(rows_to_insert)} rows into BigQuery")

    except Exception as e:
        logger.exception(f"An error occurred: {e}")
        raise

    # Log function completion
    logger.info("Historical weather data fetch completed successfully")

    return "Historical data fetch completed successfully"