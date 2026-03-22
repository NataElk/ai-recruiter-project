from app.agents.schedule_agent import schedule_agent


def test_schedule_agent():
    response = schedule_agent("Can I schedule an interview next Wednesday afternoon?")

    print("\nAgent response:\n")
    print(response)

    assert response is not None
    assert len(response) > 0


if __name__ == "__main__":
    test_schedule_agent()