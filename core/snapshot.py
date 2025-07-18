# core/snapshot.py

import os
import json
from datetime import datetime

def capture_state(user_input, L, phi_score, phi_label, result):
    """捕获当前运行的状态快照，并保存为本地 JSON 文件和 JSONL 累计记录"""

    snapshot = {
        "timestamp": datetime.utcnow().isoformat(),
        "input": user_input,
        "L_vector": L,
        "phi_score": phi_score,
        "phi_label": phi_label,
        "result": result
    }

    # 自动创建日志和快照目录
    os.makedirs("snapshots", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

    # 保存为独立快照文件
    filename = f"snapshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    path_json = os.path.join("snapshots", filename)
    with open(path_json, "w", encoding="utf-8") as f_json:
        json.dump(snapshot, f_json, ensure_ascii=False, indent=2)
    print(f"[SNAPSHOT] 状态快照已保存：{path_json}")

    # 同步追加写入到 JSONL 日志
    with open("logs/state_snapshots.jsonl", "a", encoding="utf-8") as f_log:
        f_log.write(json.dumps(snapshot, ensure_ascii=False) + "\n")
