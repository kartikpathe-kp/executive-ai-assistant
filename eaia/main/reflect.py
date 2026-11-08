"""Background "learn from this feedback" runs.

The original agent starts these on a LangGraph server. Where there is none (the Trublica platform), the run is skipped:
learning from feedback is a bonus, and must never fail the email the person just answered.
"""
import logging

log = logging.getLogger(__name__)


async def reflect(client, rewrite_state: dict) -> bool:
    """Start the reflection run; True when it was started, False when it could not be."""
    try:
        await client.runs.create(None, "multi_reflection_graph", input=rewrite_state)
        return True
    except Exception as e:
        log.warning("skipping reflection run: %s: %s", type(e).__name__, e)
        return False
