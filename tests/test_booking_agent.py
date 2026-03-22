from app.agents.booking_agent import booking_agent


def test_booking_agent_unavailable_time():
    last_offered_slots = [
        {"date": "2026-03-19", "time": "10:00:00"},
        {"date": "2026-03-19", "time": "13:00:00"},
        {"date": "2026-03-19", "time": "14:00:00"},
    ]

    response, booked_slot = booking_agent("12 works for me", last_offered_slots)

    print("\nResponse:\n", response)

    assert booked_slot is None
    assert "not one of the offered slots" in response.lower()
    assert "10:00:00" in response
    assert "13:00:00" in response
    assert "14:00:00" in response