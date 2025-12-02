class AgentRunner:
    """Orchestrates simple agent workflows for demos."""

    def __init__(self):
        self.history = []

    def run(self, agent, objective: str):
        self.history.append((agent, objective))
        return f"Ran {agent} on objective: {objective}"
