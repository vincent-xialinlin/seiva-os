# core/graphkit.py

import json
from datetime import datetime
from pathlib import Path

class GraphKit:
    """
    GraphKit：用于将状态总线与任务结构转为可视化图谱
    """

    def __init__(self, output_dir="graph_outputs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def render_task_flow(self, state_bus_snapshot, filename="task_flow"):
        """
        渲染任务模块执行流
        """
        modules = state_bus_snapshot.get("module_trace", [])
        lines = ["graph TD"]
        for i in range(len(modules) - 1):
            lines.append(f"{modules[i]} --> {modules[i + 1]}")
        lines.append(f"classDef executed fill:#00c0aa,stroke:#000,color:#fff;")
        for mod in modules:
            lines.append(f"class {mod} executed;")
        self._save_mermaid(lines, filename)

    def render_ce_phi(self, ce, phi, filename="ce_phi"):
        """
        渲染 CE × Φ 协同效率图谱
        """
        lines = [
            "graph LR",
            f"CE[CE = {ce}] --> Phi[Φ(L,t) = {phi}]",
            "Phi --> CLADE[CLADE Level]",
        ]
        self._save_mermaid(lines, filename)

    def _save_mermaid(self, lines, filename):
        content = "\n".join(lines)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        full_path = self.output_dir / f"{filename}_{ts}.mmd"
        full_path.write_text(content, encoding="utf-8")
        print(f"[✅] Mermaid 图已保存: {full_path}")

    def export_snapshot_json(self, snapshot, filename="state_snapshot"):
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = self.output_dir / f"{filename}_{ts}.json"
        path.write_text(json.dumps(snapshot, indent=2), encoding="utf-8")
        print(f"[✅] 快照 JSON 已保存: {path}")
