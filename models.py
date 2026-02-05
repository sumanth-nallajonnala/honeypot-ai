from pydantic import BaseModel

class HoneypotRequest(BaseModel):
    session_id: str
    message: str
