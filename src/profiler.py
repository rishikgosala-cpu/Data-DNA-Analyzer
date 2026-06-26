import pandas as pd
import os

#path to the dataset
dataset_path = "datasets/Employee.csv"
#Read the csv file
df = pd.read_csv(dataset_path)
#Display Data DNA profile
print("=" * 50)
print(" Data DNA Profile")
print("=" * 50)
print(f"Dataset Name: {os.path.basename(dataset_path)}")
print(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")

#column names
print("\n" + "=" * 50)
print("COLUMN NAMES")
print("=" * 50)

for column in df.columns:
    # Print each column name in the dataset
    print(column)

#DATA TYPES
print("\n" + "=" * 50)
print("DATA TYPES")
print("=" * 50)

print(df.dtypes)

#MISSING VALUES
print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)

print(df.isnull().sum())

#MEMORY USAGE
print("\n" + "=" * 50)
print("MEMORY USAGE")
print("=" * 50)

memory = df.memory_usage(deep=True).sum() / (1024)  
print(f"Memory Usage: {memory:.2f} KB")

#DATASET STATISTICS
print("\n" + "=" * 50)
print("DATASETSTATISTICS")
print("=" * 50)

print(df.describe(include="all"))

#Data DNA Fingerprint
print("\n" + "=" * 50)
print("DATA DNA FINGERPRINT")
print("=" * 50)

numeric_columns = df.select_dtypes(include=['number']).shape[1]
text_columns = df.select_dtypes(include=['object', 'string']).shape[1]
data_columns = df.select_dtypes(include=['datetime']).shape[1]

print(f"Numeric Columns: {numeric_columns}")
print(f"Text Columns: {text_columns}")
print(f"Date Columns: {data_columns}")