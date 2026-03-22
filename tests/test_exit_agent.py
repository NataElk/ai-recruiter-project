from app.agents.exit_agent import exit_agent


def test_exit_agent():
    test_cases = [
        "Thanks, that's all",
        "Bye",
        "Thanks, what about salary?"
    ]

    for msg in test_cases:
        result = exit_agent(msg)

        print("\nUser:", msg)
        print("Exit:", result["exit"])
        print("Response:", result["response"])

        assert "exit" in result
        assert "response" in result
        assert isinstance(result["exit"], bool)
        assert isinstance(result["response"], str)
        assert len(result["response"]) > 0


if __name__ == "__main__":
    test_exit_agent()