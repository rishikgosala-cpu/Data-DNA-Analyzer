import pandas as pd
import matplotlib.pyplot as plt
from src.database import get_engine

def create_visualizations():
    engine = get_engine()
    query = """SELECT * FROM CLOUD_COST"""
    df = pd.read_sql(query, engine)
    df.columns = df.columns.str.upper()

    # Visualization 1: Total Cost by Region
    plt.figure(figsize=(10, 6))
    df.groupby('REGION')['COST'].sum().plot(kind='bar', color='skyblue')
    plt.title('Total Cloud Cost by Region')
    plt.xlabel('Region')
    plt.ylabel('Total Cost')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("total_cost_by_region.png")
    plt.close()

    # Visualization 2: Total Cost by Service
    plt.figure(figsize=(10, 6))
    df.groupby('SERVICE_NAME')['COST'].sum().plot(kind='bar', color='salmon')
    plt.title('Total Cloud Cost by Service')
    plt.xlabel('Service Name')
    plt.ylabel('Total Cost')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("total_cost_by_service.png")
    plt.close()

    trend = df.groupby("USAGE_DATE")["COST"].sum()

    plt.figure(figsize=(8,5))

    trend.plot(
        kind="line",
        marker="o"
    )

    plt.title("Cloud Cost Trend")

    plt.xlabel("Date")

    plt.ylabel("Cost")

    plt.savefig("output/cost_trend.png")

    plt.close()


    print("Visualizations created and saved successfully.")

    print("\nCreating Cost Trend Data:")
    trend = df.groupby('USAGE_DATE')['COST'].sum()
    print(trend)

if __name__ == "__main__":
    create_visualizations()
