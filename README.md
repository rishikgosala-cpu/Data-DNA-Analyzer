Data-DNA-Analyzer:

Project Overview:

Data-DNA-Analyzer is a Python-based cloud cost analysis and reporting system that helps analyze cloud resource expenses stored in an Oracle Database. The project automates data ingestion, performs cost analysis, generates visualizations, provides optimization recommendations, and exports summary reports.

The project is designed to demonstrate practical skills in Python, Oracle SQL, Pandas, SQLAlchemy, and data visualization while following a modular software architecture.

Features:

- Import cloud cost data from CSV into Oracle Database
- Prevent duplicate data insertion
- Analyze total, average, and service-wise cloud costs
- Analyze region-wise and date-wise spending
- Identify the highest cost service and highest spending day
- Generate cloud cost visualizations using Matplotlib
- Provide cloud cost optimization recommendations
- Export detailed and summary reports in CSV format
- Execute the complete workflow using a single "main.py" file

Technologies Used:

- Python
- Oracle Database (Oracle XE)
- Oracle SQL
- Pandas
- SQLAlchemy
- Matplotlib
- CSV
- Git & GitHub
- Visual Studio Code

Project Structure:

Data-DNA-Analyzer/
│
├── data/
│   ├── cloud_cost.csv
│   └── datasets/
│
├── docs/
├── output/
│   ├── cost_trend.png
│   ├── total_cost_by_region.png
│   ├── total_cost_by_service.png
│   └── data_dna.db
│
├── reports/
│   ├── cloud_cost_report.csv
│   └── cloud_cost_summary.csv
│
├── screenshots/
├── sql/
├── src/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── app.py
│   ├── cloud_upload.py
│   ├── database.py
│   ├── ingestion.py
│   ├── profiler.py
│   ├── quality.py
│   ├── recommendation.py
│   ├── report.py
│   ├── sql_generator.py
│   ├── utils.py
│   └── visualization.py
│
├── tests/
│   └── test_database.py
│
├── .gitignore
├── LICENSE
├── main.py
├── README.md
└── requirements.txt

Installation:

1. Clone the repository:
   
   git clone <repository-url>

2. Navigate to the project folder:
   
   cd Data-DNA-Analyzer

3. Create a virtual environment:
   
   python -m venv .venv

4. Activate the virtual environment:
   
   Windows
   
   .venv\Scripts\activate

5. Install the required dependencies:
   
   pip install -r requirements.txt

How to Run:

Run the complete application using:

py main.py

The application will automatically:

- Import cloud cost data into Oracle Database
- Analyze cloud spending
- Generate visualizations
- Provide optimization recommendations
- Export CSV reports

Expected Output

After running the application:

- Cloud cost data is imported into the Oracle Database.
- Cost analysis is displayed in the terminal.
- Cost visualization charts are generated in the "output/" folder.
- Cloud cost reports are generated in the "reports/" folder.
- Optimization recommendations are displayed based on the analysis.

Future Enhancements

- Develop an interactive dashboard using Streamlit.
- Support multiple cloud providers (AWS, Azure, and Google Cloud).
- Enable real-time cloud cost monitoring.
- Add automated email reports.
- Integrate predictive cost forecasting using Machine Learning.

Author:

GOSALA RISHIK

B.Tech ,3rd Year ,IT Student | Data Analytics & Cloud Computing Enthusiast

This project was developed to demonstrate practical skills in Python, Oracle SQL, data analysis, visualization, and cloud cost optimization.


Screenshots:

Cost by Region:

"Cost by Region" (screenshots/total_cost_by_region.png)

Cost by Service:

"Cost by Service" (screenshots/total_cost_by_service.png)

Cost Trend:

"Cost Trend" (screenshots/cost_trend.png)

Project Workflow:

          CSV File
              │
              ▼
      Data Ingestion
              │
              ▼
     Oracle Database
              │
      ┌───────┼────────┐
      ▼       ▼        ▼
 Analysis  Visualization Recommendation
      │       │        │
      └───────┼────────┘
              ▼
      Report Generation
              │
              ▼
          CSV Reports