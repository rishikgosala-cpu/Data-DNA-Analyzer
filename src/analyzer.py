import pandas as pd
from src.database import get_engine
from src.utils import print_title

def analyze_cost_data():

    engine = get_engine()
    query = """SELECT * FROM CLOUD_COST"""
    df = pd.read_sql(query, engine)
    df.columns = df.columns.str.upper()

    print_title("====== CLOUD COST ANALYSIS ======")
    print("\nFirst 5 Records:")
    print(df.head())

    print("\nTotal Cloud Cost:")
    print(df['COST'].sum())

    print("\nAverage Cost:")
    print(df['COST'].mean())

    print("\nCost by Region:")
    print(df.groupby('REGION')['COST'].sum())

    print("\nCost by Service:")
    cost_by_service = df.groupby('SERVICE_NAME')['COST'].sum()

    print(cost_by_service)
    print("\nHighest Cost Service:")
    print(cost_by_service.idxmax())

    print("\nCost By Date:")

    date_cost = df.groupby("USAGE_DATE")["COST"].sum()

    print(date_cost)


    highest_day = date_cost.idxmax()

    print("\nHighest Spending Day:")
    print(highest_day)


    print("\nCost Percentage By Service:")

    percentage = (
        cost_by_service / cost_by_service.sum()
    ) * 100

    print(percentage)

    engine.dispose()

if __name__ == "__main__":
    analyze_cost_data()
