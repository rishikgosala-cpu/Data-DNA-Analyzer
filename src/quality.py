import pandas as pd


def quality_analysis(dataset_path):

    df = pd.read_csv(dataset_path)

    report = {}

    print("=" * 50)
    print("DATA QUALITY REPORT")
    print("=" * 50)

    total_rows = len(df)
    duplicates = df.duplicated().sum()
    missing = df.isnull().sum().sum()

    print(f"Total Rows: {total_rows}")
    print(f"Duplicate Rows: {duplicates}")
    print(f"Total Missing Values: {missing}")


    total_cells = df.shape[0] * df.shape[1]

    missing_percentage = (missing / total_cells) * 100
    duplicate_percentage = (duplicates / total_rows) * 100


    quality_score = 100

    quality_score -= missing_percentage * 1.5
    quality_score -= duplicate_percentage * 2

    quality_score = max(0, min(100, quality_score))


    print("\nDATA QUALITY SCORE")
    print(f"Score: {quality_score:.2f}/100")


    if quality_score >= 90:
        status = "Excellent"
    elif quality_score >= 75:
        status = "Good"
    elif quality_score >= 50:
        status = "Average"
    else:
        status = "Poor"


    print(f"Status: {status}")


    print("\nOUTLIERS DETECTION")

    total_outliers = 0

    numeric_columns = df.select_dtypes(include=['number']).columns


    for column in numeric_columns:

        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)

        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        outliers = df[
            (df[column] < lower) |
            (df[column] > upper)
        ]

        total_outliers += len(outliers)

        print(
            f"{column}: {len(outliers)} outliers"
        )


    trust_score = 100

    trust_score -= missing_percentage * 1.5
    trust_score -= duplicate_percentage * 2
    trust_score -= total_outliers * 0.2

    trust_score = max(0, min(100, trust_score))


    print("\nADVANCE TRUST SCORE")
    print(f"Trust Score: {trust_score:.2f}/100")


    print("\nQUALITY RECOMMENDATIONS")


    recommendations = []


    if missing > 0:
        recommendations.append(
            f"Fill {missing} missing values"
        )
    else:
        recommendations.append(
            "No missing values detected"
        )


    if duplicates > 0:
        recommendations.append(
            f"Remove {duplicates} duplicate rows"
        )
    else:
        recommendations.append(
            "No duplicate rows detected"
        )


    if total_outliers > 0:
        recommendations.append(
            f"Investigate {total_outliers} outliers"
        )
    else:
        recommendations.append(
            "No outliers detected"
        )


    for r in recommendations:
        print(r)


    report["quality_score"] = quality_score
    report["trust_score"] = trust_score
    report["status"] = status
    report["outliers"] = total_outliers
    report["recommendations"] = recommendations


    return report



if __name__ == "__main__":

    path = input("Enter CSV file path: ")

    result = quality_analysis(path)

    print(result)