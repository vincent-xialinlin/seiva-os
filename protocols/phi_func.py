# protocols/phi_func.py

def compute_phi(L):
    """
    返回协同效率分值 (Φ_score) + 协同等级标签 (Φ_label)
    """
    score = 0.25 * L['Sd'] + 0.25 * L['Lh'] + 0.25 * L['Pc'] + 0.25 * L['Ic']

    if score < 0.3:
        label = "L1"
    elif score < 0.5:
        label = "L2"
    elif score < 0.7:
        label = "L3"
    elif score < 0.9:
        label = "L4"
    else:
        label = "L5"

    return score, label
