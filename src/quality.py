import pandas as pd

#read the dataset
dataset_path = "datasets/Employee.csv"
df = pd.read_csv(dataset_path)

#dATA QUALITY REPORT
print("=" * 50)
print("DATA QUALITY REPORT")
print("=" * 50)

#Total Rows
print(f"Total Rows: {len(df)}")

#Duplicate Rows
duplicates  = df.duplicated().sum()
print(f"Duplicate Rows: {duplicates}")

#Missing Values
missing = df.isnull().sum().sum()
print(f"Total Missing Values: {missing}")

#Data Quality Percentage
print("\n" + "=" * 50)
print("DATA QUALITY PERCENTAGE")
print("=" * 50)

#Calulate Missing Value Percentage
total_cells = df.shape[0] * df.shape[1]
missing_percentage = (missing / total_cells) * 100

#Calculate Duplicate Percentage
duplicate_percentage = (duplicates / len(df)) * 100

print(f"Missing Value Percentage: {missing_percentage:.2f}%")
print(f"Duplicate Percentage: {duplicate_percentage:.2f}%")

#Data Quality Score
print("\n" + "=" * 50)
print("DATA QUALITY SCORE")
print("=" * 50)

# Start with a perfect Score
quality_score = 100

#Deduct points for missing values
quality_score -= missing_percentage * 1.5

#Deduct points for duplicate rows
quality_score -= duplicate_percentage * 2

#Keep Score within 0-100 range
quality_score = max(0, min(100, quality_score))
print(f"Data Quality Score: {quality_score:.2f}/100")

if quality_score >= 90:
    print("Data Quality Status: Excellent")
elif quality_score >= 75:
    print("Data Quality Status: Good")
elif quality_score >= 50:
    print("Data Quality Status: Average")
else:
    print("Data Quality Status: Poor")

#OUTLIERS DETECTION
print("\n" + "=" * 50)
print("OUTLIERS DETECTION")
print("=" * 50)

numeric_columns = df.select_dtypes(include=['number']).columns

for column in numeric_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    print(f"Column: {column}, Outliers Detected: {len(outliers)}")

#Column-Wise Quality Analysis
print("\n" + "=" * 50)
print("COLUMN-WISE QUALITY ANALYSIS")
print("=" * 50)

for column in df.columns:
    missing_count = df[column].isnull().sum()
    missing_percentage = (missing_count / len(df)) * 100

    print(f"Column: {column}")
    print(f"  Missing Values: {missing_count}")
    print(f"  Missing Percentage: {missing_percentage:.2f}%")

#ADVANCE TRUST SCORE
print("\n" + "=" * 50)
print("ADVANCE TRUST SCORE")
print("=" * 50)
trust_score = 100

#Missing values
trust_score -= missing_percentage * 1.5

#Duplicate rows
trust_score -= duplicate_percentage * 2

#outliers
total_outliers = 0
numeric_columns = df.select_dtypes(include=['number']).columns
for column in numeric_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    total_outliers += len(outliers)

trust_score -= (total_outliers * 0.2)
trust_score = max(0, min(100, trust_score))
print(f"Advance Trust Score: {trust_score:.2f}/100")

#QUALITY RECOMMENDATIONS
print("\n" + "=" * 50)
print("QUALITY RECOMMENDATIONS")
print("=" * 50)

if missing > 0:
    print(f"Fill {missing} missing values.")
else:
    print("No missing values detected.")
if duplicates > 0:
    print(f"Remove {duplicates} duplicate rows.")
else:
    print("No duplicate rows detected.")
if total_outliers > 0:
    print(f"Investigate {total_outliers} outlier values.")
else:
    print("No outliers detected.")
if trust_score >= 50:
    print("Data is Ready for Analysis")
else:
    print("Data needs cleaning before analysis.")
