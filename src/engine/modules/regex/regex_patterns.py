

class CommonPatterns:

    EMAIL = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    WEBSITE = r"https?://[^\s/$.?#].[^\s]*|www\.[^\s/$.?#].[^\s]*"
    PUNCTUATION = r"[^\w\s]"
    TO_FLOAT= r"[-+]?\d+(?:\.\d+)?"