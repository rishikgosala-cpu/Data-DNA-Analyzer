import pandas as pd
import os

#Read dataset
dataset_path = "datasets/Employee.csv"
df = pd.read_csv(dataset_path)

#Get table name from the file name
table_name = os.path.splitext(os.path.basename(dataset_path))[0]

#Sql Schema Generator
print("=" * 50)
print("SQL SCHEMA GENERATOR")
print("=" * 50)

sql_lines = []
sql_lines.append(f'CREATE TABLE "{table_name}" ()')

columns = []
for column in df.columns:
    # Get the data type of the column
    datatype = df[column].dtype
    if datatype == "int64":
        sql_type = "NUMBER"
    elif datatype == "float64":
        sql_type = "FLOAT"
    elif datatype == "datetime64[ns]":
        sql_type = "DATE"
    else:
        sql_type = "VARCHAR2(255)"
    columns.append(f'    "{column}" {sql_type}')
sql_lines.append(",\n".join(columns))
sql_lines.append(");")

sql_script ="\n".join(sql_lines)

print(sql_script)

os.makedirs("output", exist_ok=True)
os.makedirs("sql", exist_ok=True)

file_name = f"sql/{table_name}_schema.sql"

with open(file_name, "w") as file:
    file.write(sql_script)

print(f"\nSQL file saved successfully!")
print(f"Location: {file_name}")


