import pyodbc


def get_connection():
    conn = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=SIT-MB-066\\SQLEXPRESS;"
        "DATABASE=Tech;"
        "Trusted_Connection=yes;"
    )
    return conn