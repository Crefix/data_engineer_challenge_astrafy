{{ config(
    materialized='incremental'
) }}

WITH new_data AS (
    SELECT
        taxi.unique_key,
        taxi.trip_start_timestamp,
        taxi.trip_end_timestamp,
        taxi.trip_seconds,
        taxi.trip_miles,
        taxi.fare,
        taxi.pickup_location,
        taxi.dropoff_location,
        taxi.payment_type,
        taxi.tips,
        taxi.trip_start_geo,
        weather.temperature,
        weather.weather_main,
        weather.weather_description,
        weather.humidity,
        weather.wind_speed,
        weather.timestamp
    FROM {{ ref('stg_chicago_taxi') }} taxi
    LEFT JOIN {{ ref('chicago_weather') }} weather
    ON DATE(taxi.trip_start_timestamp) = DATE(weather.timestamp)
    WHERE 
        taxi.trip_start_timestamp BETWEEN '2023-06-01' AND '2023-12-31'
)

SELECT *
FROM new_data
{% if is_incremental() %}
    WHERE unique_key NOT IN (
        SELECT unique_key
        FROM {{ this }}
    )
{% endif %}