import pandas as pd
import os

def generate_sql_schema(dataset_path):

    # Read dataset
    df = pd.read_csv(dataset_path)

    # Get table name from file name
    table_name = os.path.splitext(os.path.basename(dataset_path))[0]

    print("=" * 50)
    print("SQL SCHEMA GENERATOR")
    print("=" * 50)

    columns = []

    for column in df.columns:
        datatype = df[column].dtype

        if datatype == "int64":
            sql_type = "NUMBER"
        elif datatype == "float64":
            sql_type = "FLOAT"
        elif str(datatype).startswith("datetime"):
            sql_type = "DATE"
        else:
            sql_type = "VARCHAR2(255)"

        columns.append(f'    "{column}" {sql_type}')

    sql_script = (
        f'CREATE TABLE "{table_name}" (\n'
        + ",\n".join(columns)
        + "\n);"
    )

    print(sql_script)

    os.makedirs("sql", exist_ok=True)

    file_name = f"sql/{table_name}_schema.sql"

    with open(file_name, "w") as file:
        file.write(sql_script)

    print("\nSQL file saved successfully!")
    print(f"Location: {file_name}")


if __name__ == "__main__":
    dataset_path = input("Enter CSV file path: ")
    generate_sql_schema(dataset_path)