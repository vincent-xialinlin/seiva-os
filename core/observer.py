# core/observer.py

import random

def analyze_input(user_input: str) -> dict:
    """
    对用户输入进行语言特征分析，并输出结构指标。
    此处为简化版模拟，未来可接入 SpaCy + entropy 等工具。
    """
    ce = round(random.uniform(0.3, 0.95), 2)  # 模拟 CE 值
    clade = infer_clade(ce)

    return {
        "ce": ce,
        "phi": ce,  # 此处暂等同处理，未来分离 Φ(L,t)
        "clade": clade,
        "snapshot": {
            "input_length": len(user_input),
            "token_density": len(user_input.split()) / max(1, len(user_input)),
        }
    }

def infer_clade(ce_score: float) -> str:
    if ce_score < 0.4:
        return "L1"
    elif ce_score < 0.55:
        return "L2"
    elif ce_score < 0.7:
        return "L3"
    elif ce_score < 0.85:
        return "L4"
    else:
        return "L5"
