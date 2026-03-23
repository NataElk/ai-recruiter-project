import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db.db_connection import get_connection


def test_connection():

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT @@VERSION")

    row = cursor.fetchone()

    print("Connected successfully!")
    print(row)

    conn.close()


if __name__ == "__main__":
    test_connection()
