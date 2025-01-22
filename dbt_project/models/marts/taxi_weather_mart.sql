SELECT
    t.unique_key,
    t.trip_start_timestamp,
    t.trip_end_timestamp,
    t.fare,
    w.temperature,
    w.humidity,
    w.weather_main
FROM {{ ref('stg_chicago_taxi') }} t
LEFT JOIN {{ ref('stg_weather_data') }} w
ON DATE(t.trip_start_timestamp) = DATE(w.timestamp)