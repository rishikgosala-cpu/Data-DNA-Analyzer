import oracledb

try:
    connection = oracledb.connect(
        user="system",
        password="root",
        dsn="192.168.1.40:1521/XEPDB1"
    )
    print("Connected to Oracle Database successfully!")
    cursor = connection.cursor()
    import pandas as pd

    df = pd.read_csv("datasets/Employee.csv")
    # sql_script = """
    # CREATE TABLE Employee (
    #    Education VARCHAR2(255),
    #    JoiningYear NUMBER,
    #    City VARCHAR2(255),
    #    PaymentTier NUMBER,
    #    Age NUMBER,
    #    Gender VARCHAR2(255),
    #    EverBenched VARCHAR2(255),
    #    ExperienceInCurrentDomain NUMBER,
    #    LeaveOrNot NUMBER
    # )
    # cursor.execute(sql_script)
    # connection.commit()

    insert_sql = """
    INSERT INTO EMPLOYEE (EDUCATION, JOININGYEAR, CITY, PAYMENTTIER, AGE, GENDER, EVERBENCHED, EXPERIENCEINCURRENTDOMAIN, LEAVEORNOT) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)
    """
    data = [tuple(row) for index, row in df.iterrows()]
    cursor.executemany(insert_sql, data)
    connection.commit()
    print("Data inserted successfully!")
    connection.close()
except Exception as e:
    print(e)

