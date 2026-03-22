import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.tools.schedule_tool_langchain import schedule_tool


def test_tool():
    """
    Test the LangChain schedule tool invocation.
    """

    result = schedule_tool.invoke({
        "req_date": "2026-05-01",
        "req_time": "10:00:00"
    })

    print("\nTool result:\n")
    print(result)

    # Validate return type
    assert isinstance(result, list)

    # Validate structure of each returned slot
    for slot in result:
        assert "date" in slot
        assert "time" in slot


if __name__ == "__main__":
    test_tool()