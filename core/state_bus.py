# core/state_bus.py

class StateBus:
    """
    SEIVA 状态总线：用于记录和传递任务执行中关键结构状态。
    """
    def __init__(self):
        self.reset()

    def reset(self):
        self.data = {
            "user_input": "",
            "ce": None,
            "phi": None,
            "clade": None,
            "intent": None,
            "dispatcher_path": None,
            "module_trace": [],
            "language_mode": "en"
        }

    def update(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def snapshot(self):
        return dict(self.data)

    def add_trace(self, module_name):
        self.data["module_trace"].append(module_name)
