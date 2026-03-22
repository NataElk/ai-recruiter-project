from app.agents.information_agent import information_agent

def test_information_agent():
    response = information_agent(
        "What skills are required for this role?",
        []
    )

    print("\nAgent response:\n")
    print(response)

    assert response is not None
    assert len(response) > 0


if __name__ == "__main__":
    test_information_agent()