def detect_scam(text: str) -> bool:
    keywords = [
        "account blocked",
        "urgent",
        "verify",
        "upi",
        "bank",
        "lottery",
        "prize",
        "kyc"
    ]
    text = text.lower()
    return any(word in text for word in keywords)
