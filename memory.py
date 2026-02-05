conversation_store = {}

def save_message(session_id: str, sender: str, text: str):
    if session_id not in conversation_store:
        conversation_store[session_id] = []
    conversation_store[session_id].append({
        "sender": sender,
        "text": text
    })

def get_history(session_id: str):
    return conversation_store.get(session_id, [])

def get_turn_count(session_id: str) -> int:
    return len(conversation_store.get(session_id, []))
