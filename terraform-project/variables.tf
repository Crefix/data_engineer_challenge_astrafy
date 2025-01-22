variable "project_id" {
  description = "The ID of the Google Cloud project"
  type        = string
}

variable "region" {
  description = "The region where BigQuery resources will be created"
  type        = string
  default     = "us-central1"
}

variable "gcp_credentials" {
  description = "Google Cloud service account key in JSON format"
  type        = string
}