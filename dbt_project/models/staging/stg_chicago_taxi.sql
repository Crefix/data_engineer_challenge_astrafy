SELECT
    unique_key,
    trip_start_timestamp,
    trip_end_timestamp,
    trip_seconds,
    trip_miles,
    fare,
    pickup_location,
    dropoff_location,
    payment_type,
    tips,
    CONCAT(
        SPLIT(SUBSTR(pickup_location, 8, LENGTH(pickup_location) - 8), ' ')[OFFSET(1)],
        ", ",
        SPLIT(SUBSTR(pickup_location, 8, LENGTH(pickup_location) - 8), ' ')[OFFSET(0)]
    ) AS trip_start_geo
FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
WHERE trip_start_timestamp BETWEEN '2023-06-01' AND '2023-12-31'