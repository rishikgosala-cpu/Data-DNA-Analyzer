Data-DNA-Analyzer: Intelligent Dataset Fingerprinting & Trust Platform

A Python-based data analysis platform that profiles datasets, evaluates data quality, calculates trust scores, generates SQL schemas, and integrates with Oracle Database for automated data loading and verification.

---

Project Overview:

Data-DNA-Analyzer is designed to help analyze structured datasets by automatically generating dataset profiles, assessing data quality, creating trust scores, producing SQL schemas, and generating reports. The platform is dataset-independent and can be used with various CSV datasets such as employee records, sales data, healthcare data, and cloud cost datasets.

---

Features:

- Automated dataset profiling
- Intelligent dataset fingerprint generation
- Column-wise statistical analysis
- Missing value detection
- Duplicate record detection
- Outlier detection using the IQR method
- Data Quality Score calculation
- Trust Score generation
- Automated data quality recommendations
- Automatic SQL schema generation
- Oracle Database integration
- Report generation
- End-to-end execution through a single "main.py"

---

Tech Stack:

- Python
- Pandas
- Matplotlib
- Oracle Database (Oracle XE)
- SQL
- CSV
- Git & GitHub
- Visual Studio Code

---

Project Structure:

Data-DNA-Analyzer/
│
├── datasets/
├── reports/
├── screenshots/
├── sql/
├── src/
├── main.py
├── requirements.txt
├── README.md
└── LICENSE

---

Project Workflow:

CSV Dataset
      │
      ▼
Data Ingestion
      │
      ▼
Data Profiling
      │
      ▼
Quality Assessment
      │
      ▼
SQL Schema Generation
      │
      ▼
Oracle Database
      │
      ▼
Reports & Visualizations

---

Installation:

1. Clone the Repository

git clone https://github.com/rishikgosala-cpu/Data-DNA-Analyzer.git

2. Navigate to the Project Folder

cd Data-DNA-Analyzer

3. Create a Virtual Environment

python -m venv .venv

4. Activate the Virtual Environment (Windows)

.venv\Scripts\activate

5. Install the Required Dependencies

pip install -r requirements.txt

---

Run the Project

Run the complete application:

py main.py

The application automatically performs:

- Dataset ingestion
- Data profiling
- Data quality assessment
- SQL schema generation
- Oracle table creation
- Data loading
- Data verification
- Report generation

---

Demo:

The project supports analyzing multiple types of structured datasets.

The screenshots included in this repository demonstrate the analysis of a sample cloud cost dataset, showcasing the platform's profiling, reporting, visualization, and quality assessment capabilities.

Example outputs include:

- Cost Trend Analysis
- Total Cost by Region
- Total Cost by Service
- Data Quality Reports
- SQL Schema Generation

---

Database Integration:

Oracle Database is used for:

- Database connection
- Automatic table creation
- SQL schema execution
- Bulk CSV data insertion
- Data verification

---

Future Enhancements:

- Interactive Streamlit dashboard
- AWS / Azure / GCP cloud cost ingestion
- Machine learning-based data quality prediction
- Automated email reports
- Real-time monitoring dashboard
- REST API support
- Support for multiple database systems (MySQL, PostgreSQL, SQL Server)

---

License:

This project is licensed under the MIT License.

---

Author:

Rishik Gosala

B.Tech Information Technology Student

Interests:

- Cloud Computing
- Data Analytics
- Data Engineering
- Python Development
- SQL & Database Systems

Feel free to fork this repository, raise issues, or contribute to the project.