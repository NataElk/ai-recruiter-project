import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.tools.booking_tool_langchain import booking_tool


def test_booking_tool_langchain():
    result = booking_tool.invoke({
        "req_date": "2026-12-29",
        "req_time": "16:00:00"
    })

    print("\nBooking tool result:\n")
    print(result)

    assert isinstance(result, bool)


if __name__ == "__main__":
    test_booking_tool_langchain()