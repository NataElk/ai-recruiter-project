from app.agents.main_agent import decide_action


def test_router():
    test_cases = [
        ("What skills are required?", "CONTINUE"),
        ("Tell me more about the role", "CONTINUE"),

        ("Can I schedule an interview?", "SCHEDULE"),
        ("Do you have anything next week?", "SCHEDULE"),
        ("I want a different time", "SCHEDULE"),
        ("Do you have something later?", "SCHEDULE"),

        ("I'll take the first one", "BOOK"),
        ("Book option 2", "BOOK"),
        ("The second slot works for me", "BOOK"),
        ("10 works for me", "BOOK"),
        ("14 is good for me", "BOOK"),
        ("I want the 10:00 slot", "BOOK"),

        ("Thanks, goodbye", "END"),
        ("I am not interested", "END"),
    ]

    for message, expected in test_cases:
        action = decide_action(message)

        print(f"\nMessage: {message}")
        print(f"Expected: {expected}, Got: {action}")

        assert action == expected