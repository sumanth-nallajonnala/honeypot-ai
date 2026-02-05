import re

def extract_intelligence(text: str):
    return {
        "bankAccounts": re.findall(r"\b\d{9,18}\b", text),
        "upiIds": re.findall(r"[a-zA-Z0-9.\-_]+@[a-zA-Z]+", text),
        "phishingLinks": re.findall(r"https?://[^\s]+", text),
        "phoneNumbers": re.findall(r"\+91\d{10}", text),
        "suspiciousKeywords": [
            "urgent" if "urgent" in text.lower() else ""
        ]
    }
