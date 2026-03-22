from langchain_core.tools import StructuredTool
from app.tools.booking_tool import book_slot

booking_tool = StructuredTool.from_function(
    func=book_slot,
    name="Interview Booking Tool",
    description=(
        "Book an interview slot. "
        "Input must include: "
        "'req_date' (YYYY-MM-DD) and 'req_time' (HH:MM:SS). "
        "Returns True if booking succeeded, False otherwise."
    )
)