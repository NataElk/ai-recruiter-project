from app.db.db_connection import get_connection


def release_slot(req_date, req_time, position="Python Dev") -> bool:
    """
    Release a previously booked slot (set available = 1)
    """

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE dbo.Schedule
    SET available = 1
    WHERE [date] = ?
      AND [time] = ?
      AND position = ?
    """

    cursor.execute(query, (req_date, req_time, position))
    conn.commit()

    success = cursor.rowcount > 0

    conn.close()
    return success