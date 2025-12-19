from agent import Agent
from memory import Memory
from tools import GeminiTool

memory = Memory()
tool = GeminiTool()

agent = Agent(
    name="PravallikaAgent",
    role="Helpful AI Assistant",
    memory=memory,
    tool=tool
)

print("Gemini AI Agent is ready. Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    reply = agent.run(user_input)
    print("Agent:", reply)
