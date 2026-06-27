import oracledb


def connect_oracle():

    try:
        connection = oracledb.connect(
            user="system",
            password="root",
            dsn="192.168.1.40:1521/XEPDB1"
        )

        print("Connected to Oracle Database successfully!")

        return connection

    except Exception as e:
        print("Oracle Connection Failed")
        print(e)
        return None



def execute_sql_file(sql_file):

    connection = connect_oracle()

    if connection is None:
        return

    cursor = connection.cursor()

    with open(sql_file, "r") as file:
        sql = file.read()
    sql = sql.replace(";", "")  # Remove semicolons

    try:
        cursor.execute(sql)
        connection.commit()

        print("SQL schema executed successfully!")

    except Exception as e:
        print("SQL Execution Error")
        print(e)

    finally:
        cursor.close()
        connection.close()



if __name__ == "__main__":

    execute_sql_file(
        "sql/Employee_schema.sql"
    )