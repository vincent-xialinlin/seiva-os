# core/dispatcher.py

def route_intent(user_input: str, l_vec: dict, phi_state: str) -> dict:
    """根据 Φ 状态与 L 向量路由至对应模块"""
    print(f"[DISPATCH] Φ = {phi_state} → Routing...")

    if phi_state in ["L1", "L2"]:
        from modules.replay_trace import replay_handler
        return replay_handler(user_input)
    elif phi_state in ["L3", "L4"]:
        from modules.scaffold_gen import generate_structure
        return generate_structure(user_input)
    elif phi_state == "L5":
        from modules.prompt_resonator import generate_taoist_style
        return generate_taoist_style(user_input)
    else:
        return {"error": "Invalid Φ state"}
