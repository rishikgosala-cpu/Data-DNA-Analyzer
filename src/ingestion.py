import pandas as pd
import os
from src.database import get_connection
from src.utils import check_file_exists 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_cost_data():

    file_path = os.path.join(BASE_DIR, "data", "cloud_cost.csv")

    check_file_exists(file_path)
    df = pd.read_csv(file_path)

    connection = get_connection()
    cursor = connection.cursor()

    for index, row in df.iterrows():
        cursor.execute(
    """
    INSERT INTO CLOUD_COST
    (
    service_name,
    region,
    cost,
    usage_date
    )
    SELECT :service, :region, :cost, TO_DATE(:date_value,'YYYY-MM-DD')
    FROM dual
    WHERE NOT EXISTS
    (
        SELECT 1
        FROM CLOUD_COST
        WHERE service_name = :service
        AND region = :region
        AND cost = :cost
        AND usage_date = TO_DATE(:date_value,'YYYY-MM-DD')
    )
    """,
    {
        "service": row.service_name,
        "region": row.region,
        "cost": row.cost,
        "date_value": row.usage_date
    }
)
    connection.commit()

    cursor.close()
    connection.close()

    print("Cloud cost data inserted successfully")


load_cost_data()