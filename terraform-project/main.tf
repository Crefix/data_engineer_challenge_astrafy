provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_bigquery_dataset" "chicago_taxi_trips" {
  dataset_id = "Chicago_Taxi_Trips"
  project    = var.project_id
  location   = "US"
}

resource "google_bigquery_table" "weather" {
  dataset_id = google_bigquery_dataset.chicago_taxi_trips.dataset_id  # Proper reference to the dataset
  table_id   = "weather"
  project    = var.project_id

  schema = jsonencode([
    {
      "name" : "id",
      "type" : "INTEGER",
      "mode" : "REQUIRED"
    },
    {
      "name" : "temperature",
      "type" : "FLOAT"
    },
    {
      "name" : "timestamp",
      "type" : "TIMESTAMP"
    },
    {
      "name" : "weather_main",
      "type" : "STRING"
    },
    {
      "name" : "weather_description",
      "type" : "STRING"
    },
    {
      "name" : "humidity",
      "type" : "FLOAT"
    },
    {
      "name" : "wind_speed",
      "type" : "FLOAT"
    }
  ])

  time_partitioning {
    type                     = "DAY"
    field                    = "timestamp"
  }
}
