# cli/run_demo.py

from core.kernel import run_seiva_kernel
from core.state_bus import state_bus
from core.graphkit import GraphKit

def demo():
    print("🔁 Running SEIVA Demo...")

    # 示例输入
    user_input = "请为我生成一份关于人工智能未来的摘要结构"

    # 运行核心内核
    run_seiva_kernel(user_input, lang="zh")

    # 可视化输出
    graphkit = GraphKit()
    graphkit.render_task_flow(state_bus.snapshot(), filename="demo_task_flow")
    graphkit.render_ce_phi(ce=state_bus.get("CE", 0.0),
                           phi=state_bus.get("Φ", "L1"),
                           filename="demo_ce_phi")
    graphkit.export_snapshot_json(state_bus.snapshot())

if __name__ == "__main__":
    demo()


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

