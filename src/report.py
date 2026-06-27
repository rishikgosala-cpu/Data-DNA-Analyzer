import pandas as pd
from src.database import get_engine


def generate_report():

    engine = get_engine()

    query = """
    SELECT *
    FROM CLOUD_COST
    """

    df = pd.read_sql(query, engine)
    df.columns = df.columns.str.upper()


    print("===== CLOUD COST REPORT =====")


    total_cost = df["COST"].sum()

    average_cost = df["COST"].mean()


    print("\nTotal Cloud Cost:")
    print(total_cost)


    print("\nAverage Cost:")
    print(average_cost)


    report_path = "reports/cloud_cost_report.csv"


    df.to_csv(
        report_path,
        index=False
    )

    summary = {
        "Total Cost": [df["COST"].sum()],
        "Average Cost": [df["COST"].mean()],
        "Highest Cost Service": [
            df.groupby("SERVICE_NAME")["COST"].sum().idxmax()
        ],
        "Highest Cost Region": [
            df.groupby("REGION")["COST"].sum().idxmax()
        ]
    }


    summary_df = pd.DataFrame(summary)


    summary_path = "reports/cloud_cost_summary.csv"


    summary_df.to_csv(
        summary_path,
        index=False
    )


    print("\nSummary Report Generated:")
    print(summary_path)


    print("\nReport Generated:")
    print(report_path)


    engine.dispose()


if __name__ == "__main__":
    generate_report()