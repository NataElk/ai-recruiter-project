from langchain_core.tools import StructuredTool
from app.tools.release_tool import release_slot

release_tool = StructuredTool.from_function(
    func=release_slot,
    name="Release Interview Slot Tool",
    description="Release a booked interview slot and make it available again."
)