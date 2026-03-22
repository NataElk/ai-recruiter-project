from langchain_core.tools import StructuredTool
from app.tools.schedule_tool import get_next_slots

schedule_tool = StructuredTool.from_function(
    func=get_next_slots,
    name="Interview Scheduler",
    description=(
        "Get the next available interview slots for a Python Developer. "
        "Input must include: "
        "'req_date' (YYYY-MM-DD) and 'req_time' (HH:MM:SS). "
        "Returns a list of available slots."
    )
)