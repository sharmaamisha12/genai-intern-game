import re

PROFANITY_LIST = ["badword1", "badword2"]  # Add actual words

def is_clean(text: str) -> bool:
    return not any(bad_word in text.lower() for bad_word in PROFANITY_LIST)
