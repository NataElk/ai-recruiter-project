import json
from datetime import datetime

from app.utils.llm_factory import get_llm
from app.tools.schedule_tool_langchain import schedule_tool
from app.prompts.schedule_prompt import EXTRACT_DATETIME_PROMPT

import re

def has_date_or_time_hint(message: str) -> bool:
    message = message.lower().strip()

    day_names = [
        "monday", "tuesday", "wednesday", "thursday",
        "friday", "saturday", "sunday"
    ]

    relative_date_terms = [
        "today", "tomorrow", "next week", "next month",
        "next monday", "next tuesday", "next wednesday",
        "next thursday", "next friday", "in 2 days", "in 3 days"
    ]

    time_terms = [
        "morning", "afternoon", "evening",
        "am", "pm", ":"
    ]

    # Day names
    if any(day in message for day in day_names):
        return True

    # Relative date phrases
    if any(term in message for term in relative_date_terms):
        return True

    # Basic time patterns like 10, 10:00, 2 pm, 14:00
    if any(term in message for term in time_terms):
        return True

    if re.search(r"\b\d{1,2}(:\d{2})?\s?(am|pm)?\b", message):
        return True

    return False


def is_generic_schedule_request(message: str) -> bool:
    message = message.lower().strip()

    generic_phrases = [
        "can i reschedule",
        "i want to reschedule",
        "another time",
        "different time",
        "change my interview",
        "move my interview",
        "book an interview",
        "schedule an interview",
    ]

    # If the message includes a date/time hint, it is NOT generic
    if has_date_or_time_hint(message):
        return False

    return any(phrase in message for phrase in generic_phrases)

def extract_datetime(user_message: str) -> dict:
    """
    Extract date and time from natural language using the LLM.
    """
    llm = get_llm()
    today = datetime.now().strftime("%Y-%m-%d")

    prompt = EXTRACT_DATETIME_PROMPT.format(
        today=today,
        user_message=user_message
    )

    response = llm.invoke(prompt)

    try:
        return json.loads(response.content)
    except Exception:
        raise ValueError("Failed to parse date/time from LLM response")


def schedule_agent(user_message: str) -> tuple[str, list]:
    """
    Scheduling agent.

    Flow:
    1. Detect whether the user is making a generic schedule/reschedule request.
    2. For generic requests, return the next available future slots directly.
    3. For specific date/time requests, extract date and time from the message.
    4. Call the scheduling tool.
    5. Return a formatted response and the offered slots.
    """
    message = user_message.lower().strip()
    today = datetime.now().strftime("%Y-%m-%d")

    if is_generic_schedule_request(message):
        req_date = today
        req_time = "00:00:00"
    else:
        extracted = extract_datetime(user_message)
        req_date = extracted["date"]
        req_time = extracted["time"]

    result = schedule_tool.invoke({
        "req_date": req_date,
        "req_time": req_time
    })

    if not result:
        return "Sorry, no available interview slots found.", []

    response = "Here are the next available interview slots:\n"
    for i, slot in enumerate(result, start=1):
        response += f"{i}. {slot['date']} at {slot['time']}\n"

    return response, result