# core/snapshot.py

import json
from datetime import datetime

def capture_state(user_input, l_vec, phi_state, result):
    snapshot = {
        "timestamp": datetime.utcnow().isoformat(),
        "input": user_input,
        "L_vector": l_vec,
        "phi": phi_state,
        "result": result
    }
    with open("logs/state_snapshots.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(snapshot, ensure_ascii=False) + "\n")
