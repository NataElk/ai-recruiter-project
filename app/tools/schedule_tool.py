from datetime import date
from app.db.db_connection import get_connection


def get_next_slots(req_date, req_time, position="Python Dev", limit=3):
    conn = get_connection()
    cursor = conn.cursor()

    
    query = """
    SELECT TOP (?) [date], [time]
    FROM dbo.Schedule
    WHERE position = ?
      AND available = 1
      AND [date] <> CAST(GETDATE() AS DATE)
      AND (
            [date] > ?
         OR ([date] = ? AND [time] >= ?)
      )
    ORDER BY [date], [time]
    """

    cursor.execute(query, (limit, position, req_date, req_date, req_time))
    rows = cursor.fetchall()
    conn.close()

    results = []
    for row in rows:
        results.append({
            "date": str(row.date),
            "time": str(row.time)
        })

    return results