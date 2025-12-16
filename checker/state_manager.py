import json
from pathlib import Path

STATE_FILE = Path(__file__).parent / "state.json"

def load_state():
    if not STATE_FILE.exists():
        return {}
    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def get_transitions(previous, current):
    transitions = {}
    for key, current_available in current.items():
        previous_available = previous.get(key, False)
        transitions[key] = (not previous_available) and current_available
    return transitions
