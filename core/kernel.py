# core/kernel.py

from core.dispatcher import route_intent
from core.snapshot import capture_state
from core.state_bus import calculate_l_vector, calculate_phi

def run_seiva_kernel(user_input: str, lang: str = "en") -> dict:
    """主执行入口：解析语言输入 → 状态感知 → 模块调用 → 返回结构响应"""
    print(f"[SEIVA-KERNEL] Input: {user_input} | Language: {lang}")

    # 1. 编码语言结构向量
    L = calculate_l_vector(user_input)

    # 2. 计算协同态 Φ(L,t)
    phi_score, phi_label = calculate_phi(L)

    print(f"[DISPATCH] L Vector: {L}")
    print(f"[DISPATCH] Φ(L,t): {phi_label} ({phi_score:.2f})")

    # 3. 调度响应模块
    result = route_intent(user_input, L, phi_label, phi_score)

    # 4. 捕获状态快照
    capture_state(user_input, L, phi_score, phi_label, result)

    return result
