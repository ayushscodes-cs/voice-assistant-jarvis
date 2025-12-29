# conversation_memory.py

MAX_TURNS = 4

_conversation = []
_current_topic = None


VAGUE_FOLLOWUPS = [
    "tell me more",
    "elaborate",
    "elaborate more",
    "continue",
    "previous topic",
    "of previous topic",
    "go on",
]


def add_user(text: str):
    global _current_topic

    lowered = text.lower()

    # If vague follow-up, reuse topic
    if any(v in lowered for v in VAGUE_FOLLOWUPS):
        if _current_topic:
            text = f"Elaborate more about {_current_topic}"
    else:
        # This is a NEW real question → set topic explicitly
        _current_topic = text

    _conversation.append(f"User: {text}")
    _trim()


def add_jarvis(text: str):
    _conversation.append(f"Jarvis: {text}")
    _trim()


def build_prompt() -> str:
    context = "\n".join(_conversation)
    return f"""
You are Jarvis, a voice assistant.
Always continue the same topic unless the user clearly asks a new one.
Keep answers short and direct.

Conversation:
{context}

Jarvis:
"""


def clear():
    global _current_topic
    _conversation.clear()
    _current_topic = None


def _trim():
    global _conversation
    _conversation = _conversation[-MAX_TURNS:]
