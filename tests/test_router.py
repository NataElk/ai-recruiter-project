from app.agents.main_agent import decide_action


def test_router():
    """
    Test router classification for different user intents.
    """

    test_cases = [
        ("What skills are required?", "CONTINUE"),
        ("Tell me more about the role", "CONTINUE"),

        ("Can I schedule an interview?", "SCHEDULE"),
        ("Do you have anything next week?", "SCHEDULE"),

        ("I'll take the first one", "BOOK"),
        ("Book option 2", "BOOK"),
        ("The second slot works for me", "BOOK"),

        ("Thanks, goodbye", "END"),
        ("I am not interested", "END"),
    ]

    for message, expected in test_cases:
        action = decide_action(message)

        print(f"\nMessage: {message}")
        print(f"Expected: {expected}, Got: {action}")

        assert action == expected