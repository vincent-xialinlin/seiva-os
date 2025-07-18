# core/dispatcher.py

from modules.replay_trace import run_replay_trace
from modules.scaffold_gen import run_scaffold_gen
from modules.prompt_resonator import run_prompt_resonator

def dispatch_module(level: str, user_input: str) -> str:
    if level in ["L1", "L2"]:
        return run_replay_trace(user_input)
    elif level in ["L3", "L4"]:
        return run_scaffold_gen(user_input)
    elif level == "L5":
        return run_prompt_resonator(user_input)
    else:
        return "[Dispatcher] 未知协同等级"
