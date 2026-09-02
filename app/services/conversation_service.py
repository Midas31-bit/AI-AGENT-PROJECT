conversations = {}

MAX_MESSAGES = 10

def get_conversation(session_id: str) -> list:
    if session_id not in conversations:
        conversations[session_id] = []
    return conversations[session_id]

def add_message_to_conversation(session_id: str, role: str, content: str):
    conversation = get_conversation(session_id)

    conversation.append({"role": role, "content": content})

    if len(conversation) > MAX_MESSAGES:
        del conversation[:-MAX_MESSAGES:]