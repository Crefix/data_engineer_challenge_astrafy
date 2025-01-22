{{ config(
    materialized='incremental',
    partition_by={
        "field": "timestamp",
        "data_type": "TIMESTAMP"
    }
) }}

WITH base AS (
    SELECT
        *,
        ROW_NUMBER() OVER (ORDER BY timestamp ASC) - 1 AS auto_id  --Autoincremental ID
    FROM {{ source('Chicago_Taxi_Trips', 'weather') }}
),

incremental AS (
    SELECT
        auto_id AS id,
        temperature,
        timestamp,
        weather_main,
        weather_description,
        humidity,
        wind_speed
    FROM base
    {% if is_incremental() %}
        WHERE timestamp > (
            SELECT MAX(timestamp)
            FROM {{ this }}
        )
    {% endif %}
)

SELECT *
FROM incremental