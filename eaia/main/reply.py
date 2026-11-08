"""Turn whatever a human sent back into the {"type", "args"} item the inbox nodes expect.

Agent Inbox resumes with a list of structured items; the Trublica Runs page resumes with the text the person typed.
Both must work, so a plain string is a free-text response, and the words "accept" / "ignore" mean those actions.
"""
from typing import Any


def answer(raw: Any) -> dict:
    if isinstance(raw, list):
        raw = raw[0] if raw else ""
    if isinstance(raw, dict) and "type" in raw:
        return raw
    text = raw if isinstance(raw, str) else str(raw)
    word = text.strip().lower()
    if word in ("accept", "ignore"):
        return {"type": word, "args": None}
    return {"type": "response", "args": text}
