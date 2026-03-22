from app.utils.llm_factory import get_llm
from app.prompts.router_prompt import ROUTER_PROMPT

from app.agents.information_agent import information_agent
from app.agents.schedule_agent import schedule_agent
from app.agents.exit_agent import exit_agent
from app.agents.booking_agent import booking_agent
from app.tools.release_tool_langchain import release_tool


def decide_action(user_message: str, history: list) -> str:
    """
    Decide the next step in the conversation:
    CONTINUE / SCHEDULE / BOOK / END
    """
    msg = user_message.lower().strip()

    # Rule-based handling for short affirmative replies
    affirmatives = {
        "ok", "okay", "yes", "yes i would", "sure",
        "sounds good", "let's do it", "yes let's schedule"
    }

    if msg in affirmatives:
        for role, text in reversed(history):
            if role == "assistant":
                last_msg = text.lower()
                if "schedule an interview" in last_msg or "would you like to schedule" in last_msg:
                    return "SCHEDULE"
                break

    llm = get_llm()

    history_text = "\n".join(
        [f"{role}: {msg}" for role, msg in history[-4:]]
    )

    prompt = ROUTER_PROMPT.format(
        user_message=user_message,
        history_text=history_text
    )
    response = llm.invoke(prompt)

    raw = response.content.strip().upper()

    if "BOOK" in raw:
        return "BOOK"
    elif "SCHEDULE" in raw:
        return "SCHEDULE"
    elif "END" in raw:
        return "END"
    else:
        return "CONTINUE"


def main_agent(
    user_message: str,
    history: list,
    last_offered_slots: list,
    booked_slot: dict | None,
) -> tuple[str, list, dict | None]:
    """
    Main orchestrator agent.

    Flow:
    1. Decide the user's intent
    2. Route to the relevant agent
    3. Return the response, updated offered slots, and booked slot
    """
    action = decide_action(user_message, history)
    print(f"\nDEBUG - action: {action}")

    if action == "SCHEDULE":
        response, offered_slots = schedule_agent(user_message)

        # If the user already has a booked slot,
        # do not offer the same slot again during rescheduling.
        if booked_slot is not None:
            offered_slots = [
                slot for slot in offered_slots
                if not (
                    slot["date"] == booked_slot["date"]
                    and slot["time"] == booked_slot["time"]
                )
            ]

            if not offered_slots:
                return "Sorry, no available interview slots found.", [], booked_slot

            response = "Here are the next available interview slots:\n"
            for i, slot in enumerate(offered_slots, start=1):
                response += f"{i}. {slot['date']} at {slot['time']}\n"

        return response, offered_slots, booked_slot

    elif action == "BOOK":
        old_booked_slot = booked_slot
        response, new_booked_slot = booking_agent(user_message, last_offered_slots)

        # If a new slot was booked successfully and it is different
        # from the previous one, release the old booked slot.
        if (
            new_booked_slot is not None
            and old_booked_slot is not None
            and (
                old_booked_slot["date"] != new_booked_slot["date"]
                or old_booked_slot["time"] != new_booked_slot["time"]
            )
        ):
            release_tool.invoke({
                "req_date": old_booked_slot["date"],
                "req_time": old_booked_slot["time"]
            })

        return response, last_offered_slots, new_booked_slot

    elif action == "END":
        result = exit_agent(user_message)
        return result["response"], last_offered_slots, booked_slot

    else:
        response = information_agent(user_message, history, booked_slot)
        return response, last_offered_slots, booked_slot