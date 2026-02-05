def generate_agent_reply(turn_count: int) -> str:
    replies = [
        "Why will my account be blocked?",
        "Which bank is this regarding?",
        "How should I resolve this issue?",
        "Can you share the payment or verification details?",
        "Is there any deadline for this?"
    ]
    return replies[min(turn_count, len(replies) - 1)]
