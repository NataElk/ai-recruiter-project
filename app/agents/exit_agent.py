import json

from app.utils.llm_factory import get_llm
from app.prompts.exit_prompt import EXIT_PROMPT


def exit_agent(user_message: str) -> dict:
    """
    Exit Advisor Agent.

    Decides whether the conversation should end
    and generates an appropriate response.
    """

    llm = get_llm()

    prompt = EXIT_PROMPT.format(user_message=user_message)
    response = llm.invoke(prompt)

    try:
        result = json.loads(response.content)
        return result
    except Exception:
        return {
            "exit": False,
            "response": "I'm here to help! Let me know if you have more questions."
        }