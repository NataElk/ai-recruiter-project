import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.tools.schedule_tool import get_next_slots


def test_schedule_tool():
    """
    Test the get_next_slots function with multiple scenarios,
    including edge cases.
    """

    test_cases = [
        ("2026-04-01", "09:00:00", "Basic request"),
        ("2026-04-01", "17:00:00", "Late time in same day"),
        ("2026-04-02", "09:00:00", "Next day"),
        ("2030-01-01", "09:00:00", "Far future (edge case)")
    ]

    for date, time, description in test_cases:
        print(f"\n=== Test: {description} ===")
        print(f"Input → date: {date}, time: {time}")

        slots = get_next_slots(date, time)

        print("\nReturned slots:")
        for slot in slots:
            print(slot)

        #  Validate return type
        assert isinstance(slots, list)

        #  Validate structure of each slot
        for slot in slots:
            assert "date" in slot
            assert "time" in slot

        #  Edge case: no available slots
        if len(slots) == 0:
            print(" No slots found (this may be valid depending on DB state)")

        #  Optional: ensure slots are sorted chronologically
        dates_times = [(s["date"], s["time"]) for s in slots]
        assert dates_times == sorted(dates_times)


if __name__ == "__main__":
    test_schedule_tool()