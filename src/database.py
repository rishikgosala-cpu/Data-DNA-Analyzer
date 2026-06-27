import oracledb
from sqlalchemy import create_engine


def get_connection():

    connection = oracledb.connect(
        user="system",
        password="root",
        dsn="192.168.1.40:1521/XEPDB1"
    )

    return connection


def get_engine():

    engine = create_engine(
        "oracle+oracledb://system:root@192.168.1.40:1521/?service_name=XEPDB1"
    )

    return engine