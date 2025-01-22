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
    tips
FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
WHERE trip_start_timestamp BETWEEN '2023-06-01' AND '2023-12-31'