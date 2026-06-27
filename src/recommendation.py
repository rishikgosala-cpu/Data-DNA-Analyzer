import pandas as pd
from src.database import get_engine
from src.utils import print_title


def generate_recommendations():

    engine = get_engine()

    query = """
    SELECT *
    FROM CLOUD_COST
    """

    df = pd.read_sql(query, engine)
    df.columns = df.columns.str.upper()


    print_title("====== CLOUD COST OPTIMIZATION REPORT ======")


    # Service analysis

    service_cost = df.groupby("SERVICE_NAME")["COST"].sum()

    highest_service = service_cost.idxmax()
    highest_cost = service_cost.max()


    print("\nHighest Cost Service:")
    print(highest_service, "=", highest_cost)


    print("\nRecommendation:")

    if highest_service == "EC2":
        print("Consider reducing unused EC2 instances or using auto-scaling.")

    elif highest_service == "RDS":
        print("Review database usage and optimize storage.")

    elif highest_service == "S3":
        print("Check unused storage and enable lifecycle policies.")

    else:
        print("Review usage patterns for optimization.")



    # Region analysis

    region_cost = df.groupby("REGION")["COST"].sum()

    highest_region = region_cost.idxmax()


    print("\nHighest Cost Region:")
    print(highest_region)


    print("\nRegion Recommendation:")
    print("Review resources running in this region for possible optimization.")


    engine.dispose()


if __name__ == "__main__":
    generate_recommendations()