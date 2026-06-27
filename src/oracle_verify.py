from src.oracle_loader import connect_oracle


def verify_data(table_name):

    connection = connect_oracle()

    if connection is None:
        return

    cursor = connection.cursor()

    try:

        cursor.execute(
            f'SELECT COUNT(*) FROM "{table_name}"'
        )

        count = cursor.fetchone()[0]

        print("=" * 50)
        print("ORACLE VERIFICATION")
        print("=" * 50)

        print(f"Table: {table_name}")
        print(f"Rows Stored: {count}")


    except Exception as e:
        print("Verification Error")
        print(e)


    finally:
        cursor.close()
        connection.close()



if __name__ == "__main__":

    verify_data("Employee")