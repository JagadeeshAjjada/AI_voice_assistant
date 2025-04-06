import json
from pathlib import Path

HISTORY_FILE = Path("chat_history.json")

def save_chat_history(history):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f)

def load_chat_history():
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return []
