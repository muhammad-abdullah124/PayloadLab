import random

def mutate_payload(payload, mode="waf"):
    if mode == "waf":
        return insert_random_comments(payload)
    elif mode == "stealth":
        return payload.replace(" ", "%20")
    elif mode == "brute":
        return payload + random.choice(["<!-- -->", "#", "%00"])
    return payload

def insert_random_comments(payload):
    parts = payload.split(" ")
    return "/* */".join(parts) if len(parts) > 1 else payload