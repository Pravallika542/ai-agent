class Agent:
    def __init__(self, name, role, memory, tool):
        self.name = name
        self.role = role
        self.memory = memory
        self.tool = tool

    def think(self, user_input):
        prompt = f"""
You are an AI agent.

Role: {self.role}

User question:
{user_input}

Answer clearly and correctly in simple words.
"""
        return prompt

    def act(self, thought):
        return self.tool.run(thought)

    def run(self, user_input):
        self.memory.store(f"User: {user_input}")
        thought = self.think(user_input)
        response = self.act(thought)
        self.memory.store(f"Agent: {response}")
        return response
