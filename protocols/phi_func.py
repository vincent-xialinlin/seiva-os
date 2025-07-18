# protocols/phi_func.py

def compute_phi(L: dict) -> str:
    """
    Φ(L, t)：根据语言结构向量计算协同态等级 L1-L5
    - 简化线性权重公式：Φ = 0.3*Sd + 0.3*Lh + 0.2*Pc + 0.2*Ic
    """
    score = (
        0.3 * L["Sd"] +
        0.3 * L["Lh"] +
        0.2 * L["Pc"] +
        0.2 * L["Ic"]
    )

    if score < 0.4:
        return "L1"
    elif score < 0.55:
        return "L2"
    elif score < 0.7:
        return "L3"
    elif score < 0.85:
        return "L4"
    else:
        return "L5"
