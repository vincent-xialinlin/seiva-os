import os
from typing import Dict

# -------------------------
# ✅ 结构向量计算函数
def calculate_l_vector(text: str) -> Dict[str, float]:
    """
    根据输入文本估算语言结构向量 L = (Sd, Lh, Pc, Ic)
    """
    sd = round(len(text) / 100, 2)
    lh = round(min(1.0, text.count("、") / 5), 2)
    pc = round(1.0 - sd * 0.2, 2)
    ic = round(0.6 + 0.4 * (1 - abs(0.5 - sd)), 2)

    return {
        "Sd": sd,
        "Lh": lh,
        "Pc": pc,
        "Ic": ic
    }

# -------------------------
# ✅ 协同效率计算函数
def calculate_phi(L: dict) -> tuple:
    """
    根据 L 向量计算协同效率分数（Φ）及其对应 CLADE 等级
    """
    score = round(
        0.25 * L["Sd"] + 0.25 * L["Lh"] + 0.25 * L["Pc"] + 0.25 * L["Ic"], 2
    )

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

# -------------------------
# ✅ 状态总线类
class StateBus:
    """
    SEIVA 状态总线：记录并传递系统运行过程中的结构状态
    """
    def __init__(self):
        self.state = {
            "lang": "en",
            "user_input": "",
            "L_vector": {},
            "phi_score": 0.0,
            "clade": "L1",
            "intent": "",
            "dispatcher_path": "",
            "module_trace": []
        }

    def update(self, key, value):
        self.state[key] = value

    def get(self, key, default=None):  # ✅ 支持默认值
        return self.state.get(key, default)

    def add_trace(self, module_name):
        self.state["module_trace"].append(module_name)

    def dump(self):
        return dict(self.state)

    def snapshot(self):  # ✅ 兼容 graphkit 调用
        return dict(self.state)

# -------------------------
# ✅ 实例化全局状态总线
state_bus = StateBus()
