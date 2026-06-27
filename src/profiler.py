import pandas as pd
import os

def data_profiler(dataset_path):

    # Read the CSV file
    df = pd.read_csv(dataset_path)

    # Display Data DNA Profile
    print("=" * 50)
    print("DATA DNA PROFILE")
    print("=" * 50)
    print(f"Dataset Name: {os.path.basename(dataset_path)}")
    print(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")

    # Column Names
    print("\n" + "=" * 50)
    print("COLUMN NAMES")
    print("=" * 50)

    for column in df.columns:
        print(column)

    # Data Types
    print("\n" + "=" * 50)
    print("DATA TYPES")
    print("=" * 50)
    print(df.dtypes)

    # Missing Values
    print("\n" + "=" * 50)
    print("MISSING VALUES")
    print("=" * 50)
    print(df.isnull().sum())

    # Memory Usage
    print("\n" + "=" * 50)
    print("MEMORY USAGE")
    print("=" * 50)

    memory = df.memory_usage(deep=True).sum() / 1024
    print(f"Memory Usage: {memory:.2f} KB")

    # Dataset Statistics
    print("\n" + "=" * 50)
    print("DATASET STATISTICS")
    print("=" * 50)
    print(df.describe(include="all"))

    # Data DNA Fingerprint
    print("\n" + "=" * 50)
    print("DATA DNA FINGERPRINT")
    print("=" * 50)

    numeric_columns = df.select_dtypes(include=['number']).shape[1]
    text_columns = df.select_dtypes(include=['object', 'string']).shape[1]
    date_columns = df.select_dtypes(include=['datetime']).shape[1]

    print(f"Numeric Columns: {numeric_columns}")
    print(f"Text Columns: {text_columns}")
    print(f"Date Columns: {date_columns}")


if __name__ == "__main__":
    dataset_path = input("Enter CSV file path: ")
    data_profiler(dataset_path)