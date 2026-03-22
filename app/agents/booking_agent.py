from app.tools.booking_tool_langchain import booking_tool


def booking_agent(user_message: str, last_offered_slots: list) -> tuple[str, dict | None]:
    """
    Booking Agent

    Flow:
    1. Make sure there are offered slots in memory
    2. Detect which slot the user selected
    3. Try to book the selected slot
    4. Return a confirmation message and the booked slot
    """

    if not last_offered_slots:
        return (
            "I could not find any offered slots to book. Please ask for available interview times first.",
            None
        )

    message = user_message.lower().strip()
    selected_index = None
    requested_time = None

    # First: match by option number
    if message in {"1", "option 1", "option number 1", "slot 1", "first", "the first one"}:
        selected_index = 0
    elif message in {"2", "option 2", "option number 2", "slot 2", "second", "the second one"}:
        selected_index = 1
    elif message in {"3", "option 3", "option number 3", "slot 3", "third", "the third one"}:
        selected_index = 2

    # Second: if no option was selected, try matching by time
    if selected_index is None:
        for i, slot in enumerate(last_offered_slots):
            slot_time = slot["time"]      # e.g. "11:00:00"
            slot_hour = slot_time[:2]     # e.g. "11"
            slot_hhmm = slot_time[:5]     # e.g. "11:00"

            if slot_hour in message or slot_hhmm in message:
                selected_index = i
                requested_time = slot_hhmm
                break

    if selected_index is None:
        available_slots_text = "Here are the available slots:\n"
        for i, slot in enumerate(last_offered_slots, start=1):
            available_slots_text += f"{i}. {slot['date']} at {slot['time']}\n"

        if requested_time is not None:
            return (
                f"Sorry, {requested_time} is not one of the offered slots.\n{available_slots_text}",
                None
            )

        return (
            "I could not understand which slot you selected. "
            "Please reply with 1, 2, or 3, or write the exact time.\n"
            f"{available_slots_text}",
            None
        )

    if selected_index >= len(last_offered_slots):
        return (
            "That option is not available. Please choose one of the offered slots.",
            None
        )

    selected_slot = last_offered_slots[selected_index]

    success = booking_tool.invoke({
        "req_date": selected_slot["date"],
        "req_time": selected_slot["time"]
    })

    if success:
        return (
            f"Your interview has been booked for {selected_slot['date']} at {selected_slot['time']}.",
            selected_slot
        )

    return (
        "Sorry, that slot is no longer available. Please ask for available interview times again.",
        None
    )