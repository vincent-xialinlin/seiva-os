# core/kernel.py

from core.dispatcher import route_intent
from core.snapshot import capture_state
from protocols.l_vector import encode_l_vector
from protocols.phi_func import compute_phi

def run_seiva_kernel(user_input: str, lang: str = "en") -> dict:
    """主执行入口：解析语言输入 → 状态感知 → 模块调用 → 返回结构响应"""
    print(f"[SEIVA-KERNEL] Input: {user_input} | Language: {lang}")

    # 1. 编码语言结构向量
    L = encode_l_vector(user_input)

    # 2. 计算协同态 Φ(L,t)
    phi = compute_phi(L)

    # 3. 调度响应模块
    result = route_intent(user_input, L, phi)

    # 4. 捕获状态快照
    capture_state(user_input, L, phi, result)

    return result
