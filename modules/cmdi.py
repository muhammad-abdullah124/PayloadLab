import json
import random
from pathlib import Path

PAYLOAD_FILE = Path(__file__).resolve().parent.parent / 'payloads/cmdi_payloads.json'

def load_cmdi_payloads():
    with open(PAYLOAD_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_random_cmdi(count=5, filters=None):
    payloads = load_cmdi_payloads()
    if filters:
        payloads = [p for p in payloads if any(f in p.get('payload', '') for f in filters)]
    return random.sample(payloads, min(count, len(payloads)))