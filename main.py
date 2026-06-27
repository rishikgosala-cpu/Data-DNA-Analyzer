from src.ingestion import load_cost_data
from src.analyzer import analyze_cost_data
from src.visualization import create_visualizations
from src.recommendation import generate_recommendations
from src.report import generate_report

from src.profiler import data_profiler
from src.quality import quality_analysis
from src.sql_generator import generate_sql_schema
from src.oracle_loader import execute_sql_file
from src.oracle_insert import insert_csv_data
from src.oracle_verify import verify_data


print("===== DATA DNA ANALYZER =====")


# Existing pipeline

load_cost_data()

analyze_cost_data()

create_visualizations()

generate_recommendations()

generate_report()



# New Data Quality Pipeline

print("\n===== DATA QUALITY PIPELINE =====")


dataset_path = input(
    "\nEnter CSV file path for profiling: "
)


print("\n--- PROFILER ---")

profile = data_profiler(dataset_path)


print("\n--- QUALITY ANALYSIS ---")

quality = quality_analysis(dataset_path)


print("\n--- SQL GENERATOR ---")

generate_sql_schema(dataset_path)

print("\n--- ORACLE TABLE CREATION ---")

table_name = dataset_path.split("/")[-1].replace(".csv","")

sql_file = f"sql/{table_name}_schema.sql"

execute_sql_file(sql_file)


print("\n--- ORACLE DATA INSERTION ---")

insert_csv_data(
    dataset_path,
    table_name
)

print("\n=== ORACLE VERIFICATION ===")
verify_data(table_name)

print("\n===== PROJECT COMPLETED =====")