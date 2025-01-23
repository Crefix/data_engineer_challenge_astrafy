# data_engineer_challenge_astrafy 🚖🌦️
This project implements modern data engineering stack, leveraging tools like Terraform, dbt, BigQuery, and Looker Studio.

------

## **Project Objectives** 🛠️
1. **Automate data ingestion**
2. **Transform and validate data**
3. **Secure data**
4. **Visualize Insights**

---
## **Tools and Technologies** 🖥️
| Tool            | Purpose                           |
|-----------------|-----------------------------------|
| **Terraform**   | Infrastructure as Code (IaC)     |
| **Google Cloud**| Cloud services (BigQuery, Cloud Functions, etc.) |
| **dbt Cloud**   | Data transformations and CI/CD   |
| **Looker Studio** | Dashboard for data visualization |

---

## **Repository Structure** 📂
```plaintext
.
├── .github/workflows/           # CI/CD workflows for Terraform
├── cloud_functions/             # Python scripts for ETL 
│   ├── daily_weather.py         # Job-based data ingestion
│   ├── historical_weather.py    # Trigger-once data ingestion
│   └── requirements.txt         # Python dependencies
├── dbt_project/                 # dbt project
│   └── models/                  # dbt models
│       ├── staging/             # Raw tables
│       └── marts/               # Final transformations
├── terraform-project/           # Terraform scripts for infrastructure setup
│   ├── main.tf                  # Main configuration
│   └── variables.tf             # Variable definitions
└── README.md                    # Project overview
```

---

## **Getting Started** 🚀

### **1. Prerequisites**
- **Google Cloud Platform**: Ensure you have access to a GCP project
- **Terraform**: Install [Terraform](https://www.terraform.io/downloads)
- **dbt Cloud**: Create a free dbt Cloud account
- **Looker Studio**: Access Google Looker Studio
- **Python**: 3.7+ installed 

### **2. Clone the Repository**
```bash
git clone https://github.com/Crefix/data_engineer_challenge_astrafy
cd data_engineer_challenge_astrafy
```

### **3. Set Up Infrastructure**
1. Navigate to the `terraform/` directory and then:
   ```bash
   cd terraform-project
   terraform init
   terraform plan
   terraform apply
   ```
2. This sets up:
   - A BigQuery table for incoming data weather

### **4. Configure dbt**
1. Log in to **dbt Cloud** and create a new project.
2. Connect the project to your BigQuery data warehouse
3. Clone this repository into the dbt Cloud IDE or connect your GitHub repository.
4. Run the following commands in the dbt Cloud IDE to set up your transformations:
   ```bash
   dbt build  # Create models and validate setup
   dbt run    # Run models to create tables/views in BigQuery
   ```
5. Schedule jobs to automate transformations.

### **4. Deploying Python to Cloud Functions**
This project includes two Cloud Functions for data ingestion:

1. Historical Weather Data Ingestion: Fetches weather data for a specific date range and loads it into BigQuery.
2. Real-Time Weather Data Ingestion: Fetches current weather data daily and loads it into BigQuery.

**Setting up the Python Environment**
* Navigate to the cloud_functions/ directory
* Install Python dependencies locally for testing
* Ensure you have a valid service account key with the proper API enabled (ie, BigQuery, Cloud Functions and Secret Manager) and the Google Cloud SDK installed
* Deploy the snippets to Cloud Functions, eg:
```bash
   gcloud functions deploy fetch_historical_weather \
    --runtime python310 \
    --trigger-http \
    --entry-point fetch_historical_weather \
    --region us-central1 \
    --allow-unauthenticated 
```
* Create a Cloud Scheduler job to trigger the functions
```bash
   gcloud scheduler jobs create http fetch_weather_daily \
    --schedule="0 0 * * *" \
    --uri="https://<YOUR_CLOUD_FUNCTION_URL>" \
    --http-method=POST
```

### **6. Build a dashboard**
See an example for inspiration at https://lookerstudio.google.com/s/g6YeGJxv64U

---

## **License** 📄
This project is unlicensed as it is just a job assignment application.

---

## **Contact** 📬
For questions or support, contact [crisnavas10@gmail.com].