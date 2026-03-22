import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.tools.booking_tool import book_slot


def test_booking_tool():
    result = book_slot("2026-12-29", "17:00:00")

    print("\nBooking result:\n")
    print(result)

    assert isinstance(result, bool)


if __name__ == "__main__":
    test_booking_tool()