from app.db.db_connection import get_connection


def book_slot(req_date, req_time, position="Python Dev") -> bool:
    """
    Book a specific interview slot only if it is still available.
    Returns True if booking succeeded, otherwise False.
    """

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE dbo.Schedule
    SET available = 0
    WHERE [date] = ?
      AND [time] = ?
      AND position = ?
      AND available = 1
    """

    cursor.execute(query, (req_date, req_time, position))
    conn.commit()

    success = cursor.rowcount > 0

    conn.close()
    return success