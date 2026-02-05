import os
from fastapi import HTTPException

SECRET_API_KEY = os.getenv("HONEYPOT_API_KEY")

def verify_api_key(api_key: str):
    if not SECRET_API_KEY:
        raise HTTPException(status_code=500, detail="API Key not configured")
    if api_key != SECRET_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
