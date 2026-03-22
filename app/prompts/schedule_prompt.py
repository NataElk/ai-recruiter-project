EXTRACT_DATETIME_PROMPT = """
Today is {today}.

Extract the requested interview date and time from the user message.

Rules:
- Convert relative dates such as:
  - "tomorrow"
  - "next Monday"
  - "Monday next week"
  - "in 3 days"
- If the user mentions a weekday without a calendar date, convert it to the next appropriate date.
- If no exact time is mentioned:
  - morning -> 09:00:00
  - afternoon -> 14:00:00
  - evening -> 18:00:00
  - otherwise default -> 09:00:00
- Return ONLY valid JSON.
- Do not add any explanation or markdown.

Format:
{{
    "date": "YYYY-MM-DD",
    "time": "HH:MM:SS"
}}

User message:
{user_message}
"""