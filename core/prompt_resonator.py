# core/prompt_resonator.py

def choose_prompt_style(L, phi_score, phi_label):
    """
    根据语言向量 L 和 Φ 协同得分，选择适合的 Prompt 风格
    """
    if phi_label == "L5":
        return "taoist_abstract"
    elif phi_label == "L4":
        return "scholarly_formal"
    elif phi_label == "L3":
        return "structured_summary"
    elif phi_label == "L2":
        return "guiding_outline"
    else:
        return "replay_hint"
