import pandas as pd
from src.oracle_loader import connect_oracle


def insert_csv_data(csv_path, table_name):

    df = pd.read_csv(csv_path)

    connection = connect_oracle()

    if connection is None:
        return

    cursor = connection.cursor()


    columns = ",".join(
        [f'"{col}"' for col in df.columns]
    )


    placeholders = ",".join(
        [f":{i+1}" for i in range(len(df.columns))]
    )


    sql = f"""
    INSERT INTO "{table_name}"
    ({columns})
    VALUES ({placeholders})
    """


    data = [
        tuple(row)
        for row in df.values
    ]


    try:

        cursor.executemany(
            sql,
            data
        )

        connection.commit()

        print(
            f"{len(data)} rows inserted successfully!"
        )


    except Exception as e:

        print("Insert Error")
        print(e)


    finally:

        cursor.close()
        connection.close()



if __name__ == "__main__":

    insert_csv_data(
        "datasets/Employee.csv",
        "Employee"
    )