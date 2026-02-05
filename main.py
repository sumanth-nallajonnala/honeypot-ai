from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader

from scam_detector import detect_scam
from agent import generate_agent_reply
from memory import save_message, get_turn_count
from extractor import extract_intelligence
from callback import send_guvi_callback

app = FastAPI(title="Agentic HoneyPot API")

# ---------------- CONFIG ----------------
API_KEY = "sk_honeypot_2026_secret"
MAX_TURNS = 8

api_key_header = APIKeyHeader(name="x-api-key")

# ---------------- AUTH ----------------
def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API key"
        )

# ---------------- API ----------------
@app.post("/api/honeypot")
def honeypot_api(
    data: dict,
    _: str = Depends(verify_api_key)
):
    session_id = data.get("session_id")
    message = data.get("message")

    if not session_id or not message:
        raise HTTPException(
            status_code=422,
            detail="session_id and message are required"
        )

    # Save scammer message
    save_message(session_id, "scammer", message)

    # Detect scam
    is_scam = detect_scam(message)

    # Agent reply
    reply = "Thank you for the information."
    if is_scam:
        reply = generate_agent_reply(get_turn_count(session_id))

    save_message(session_id, "agent", reply)

    intelligence = extract_intelligence(message)

    if get_turn_count(session_id) >= MAX_TURNS:
        send_guvi_callback(
            session_id=session_id,
            intelligence=intelligence,
            total_messages=get_turn_count(session_id)
        )

    return {
        "status": "success",
        "reply": reply,
        "turns": get_turn_count(session_id)
    }

@app.get("/")
def root():
    return {"status": "Honeypot API is running"}

import os

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
