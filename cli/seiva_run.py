# cli/seiva_run.py

import sys
from core.kernel import run_seiva_kernel

def main():
    print("🌐 SEIVA OS 启动中... [Structured Explicit-Language Intelligence via Architecture]")
    lang = "auto"
    if len(sys.argv) > 1:
        if sys.argv[1] == "--lang":
            lang = sys.argv[2]
    run_seiva_kernel(lang)

if __name__ == "__main__":
    main()

from core.observer import analyze_input

# 替换原始 mock_clade 推断
obs_result = analyze_input(user_input)
clade_level = obs_result["clade"]



from core.state_bus import StateBus

state_bus = StateBus()
state_bus.update("user_input", user_input)
state_bus.update("ce", obs_result["ce"])
state_bus.update("phi", obs_result["phi"])
state_bus.update("clade", obs_result["clade"])


# 在 seiva_run.py 中调用示例：
from core.graphkit import GraphKit

graphkit = GraphKit()
graphkit.render_task_flow(state_bus.snapshot(), filename="demo_flow")
graphkit.render_ce_phi(ce=0.72, phi="L3", filename="demo_ce_phi")
graphkit.export_snapshot_json(state_bus.snapshot())

