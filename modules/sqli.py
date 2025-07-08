import json
import random
from pathlib import Path

PAYLOAD_FILE = Path(__file__).resolve().parent.parent / 'payloads/sqli_payloads.json'

def load_sqli_payloads():
    with open(PAYLOAD_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_random_sqli(count=5, filters=None):
    payloads = load_sqli_payloads()
    if filters:
        payloads = [p for p in payloads if any(f in p.get('payload', '') for f in filters)]
    return random.sample(payloads, min(count, len(payloads)))