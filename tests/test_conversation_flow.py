from app.agents.main_agent import main_agent

def test_conversation_flow():
    conversation = [
        "Can I schedule an interview tomorrow?",
        "I'll take the first one",
        "Actually, I want another time",
        "14 works for me"
    ]

    history = []
    last_offered_slots = []
    booked_slot = None

    for i, msg in enumerate(conversation):
        print("\nUser:", msg)

        response, offered_slots, booked_slot = main_agent(
            msg,
            history,
            last_offered_slots,
            booked_slot
        )
        print("Agent:", response)

        history.append(("user", msg))
        history.append(("assistant", response))

        last_offered_slots = offered_slots

        assert response is not None
        assert isinstance(response, str)
        assert len(response) > 0

        if i == 0:
            assert isinstance(offered_slots, list)
            assert len(offered_slots) > 0
            assert "available interview slots" in response.lower()
            assert booked_slot is None

        elif i == 1:
            assert "booked" in response.lower()
            assert booked_slot is not None
            assert isinstance(booked_slot, dict)
            assert "date" in booked_slot
            assert "time" in booked_slot

        elif i == 2:
            assert isinstance(offered_slots, list)

            if "available interview slots" in response.lower():
                assert len(offered_slots) > 0
                assert booked_slot is None
            else:
                assert "no available interview slots found" in response.lower()
                assert len(offered_slots) == 0
                assert booked_slot is None

        elif i == 3:
            if len(last_offered_slots) == 0:
                return

            assert "booked" in response.lower()
            assert booked_slot is not None
            assert isinstance(booked_slot, dict)
            assert "date" in booked_slot
            assert "time" in booked_slot