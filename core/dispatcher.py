# core/dispatcher.py

from modules.replay_trace import run_replay_trace
from modules.scaffold_gen import run_scaffold_gen
from modules.prompt_resonator import run_prompt_resonator
from core.prompt_resonator import choose_prompt_style
from core.snapshot import capture_state

def route_intent(intent, L, phi_label, phi_score):
    print(f"[DISPATCH] Intent: {intent}")
    
    # 调用 prompt 风格选择器
    style = choose_prompt_style(L, phi_score, phi_label)
    print(f"[PROMPT] 使用风格: {style}")

    # 模拟结构生成路径
    if phi_score >= 0.9:
        output = f"[L5] → TaoistBuilder: 道家结构生成中…"
    elif phi_score >= 0.7:
        output = f"[L4] → ScaffoldGen: 正在搭建结构模板…"
    elif phi_score >= 0.5:
        output = f"[L3] → ScaffoldGen: 标准结构任务执行中…"
    else:
        output = f"[L1–L2] → ReplayTrace: 回放历史路径结构…"

    # 捕获运行状态
    capture_state(
        user_input=intent,
        L=L,
        phi_score=phi_score,
        phi_label=phi_label,
        result=output
    )

    return output
