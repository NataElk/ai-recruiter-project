from app.rag.rag_chain import ask_rag
from app.utils.llm_factory import get_llm
from app.prompts.info_prompt import INFO_PROMPT


def information_agent(user_message: str, history: list, booked_slot: dict | None = None) -> str:
    greetings = {"hi", "hello", "hey", "good morning", "good evening", "good afternoon"}

    if user_message.lower().strip() in greetings:
        if booked_slot is not None:
            return (
                f"Hi! You already have an interview scheduled for "
                f"{booked_slot['date']} at {booked_slot['time']}. "
                "You can ask about the role or request to reschedule."
            )
        return "Hi! How can I help you today? You can ask about the role or schedule an interview."

    rag_result = ask_rag(user_message)
    context = rag_result["context"]

    llm = get_llm()

    history_text = "\n".join(
        [f"{role}: {msg}" for role, msg in history[-5:]]
    )

    if booked_slot is not None:
        interview_status = (
            f"The user already has an interview scheduled for "
            f"{booked_slot['date']} at {booked_slot['time']}."
        )
    else:
        interview_status = "The user does not have an interview scheduled yet."

    prompt = INFO_PROMPT.format(
        history_text=history_text,
        context=context,
        user_message=user_message,
        interview_status=interview_status,
    )

    response = llm.invoke(prompt)
    return response.content