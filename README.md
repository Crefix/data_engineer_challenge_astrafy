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
├── terraform-project/           # Terraform scripts for infrastructure setup
│   ├── main.tf                  # Main configuration
│   ├── variables.tf             # Variable definitions
├── dbt_project/                 # dbt project
│   ├── models/                  # dbt models
│   │   ├── staging/             # Raw tables
│   │   ├── marts/               # Final transformations
│   └── tests/                   # Data quality tests
├── cloud_functions/             # Python scripts for data ingestion
│   ├── weather_scheduled.py     # Job-based data ingestion
│   ├── weather_once.py          # Trigger-once data ingestion
│   └── requirements.txt         # Python dependencies
└── README.md                    # Project overview
```

---

## **Getting Started** 🚀

### **1. Prerequisites**
- **Google Cloud Platform**: Ensure you have access to a GCP project.
- **Terraform**: Install [Terraform](https://www.terraform.io/downloads)
- **dbt Cloud**: Create a free dbt Cloud account
- **Looker Studio**: Access Google Looker Studio

### **2. Clone the Repository**
```bash
git clone https://github.com/your-repo/chicago-taxi-analysis.git
cd chicago-taxi-analysis
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
   dbt run    # Run models to create tables/views in BigQuery
   dbt test   # Run tests to validate data quality
   ```
5. Schedule jobs (associate with this repo) in dbt Cloud to automate transformations.

### **5. Build a dashboard**
See an example for inspiration at https://lookerstudio.google.com/s/g6YeGJxv64U

---

## **License** 📄
This project is unlicensed as it is just a job assignment application.

---

## **Contact** 📬
For questions or support, contact [crisnavas10@gmail.com].