# Project 2 — Agentic Assistant

Overview

This project explores agentic assistants capable of using tools, maintaining memory, and performing multi-step tasks. Contains agent implementations, tool adapters, and integration examples.

## Contents

- `src/agents/` — agent implementations
- `src/tools/` — tool adapters (web search, email, calendar)
- `notebooks/` — demos and usage examples
- `tests/` — test suite
- `deployments/` — Dockerfile for deployment

## Setup

```bash
cd project2_agentic_assistant
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run Demo

```bash
cd project2_agentic_assistant
PYTHONPATH=.. python -c "
from src.agent_runner import AgentRunner

runner = AgentRunner()
result1 = runner.run('ResearchAgent', 'Find recent AI papers')
result2 = runner.run('TaskAgent', 'Schedule meeting with team')
result3 = runner.run('EmailAgent', 'Send status update')

print('Agent execution history:')
for agent, obj in runner.history:
    print(f'  - {agent}: {obj}')

print('\\nResults:')
print(f'  {result1}')
print(f'  {result2}')
print(f'  {result3}')
"
```

Expected output:
```
Agent execution history:
  - ResearchAgent: Find recent AI papers
  - TaskAgent: Schedule meeting with team
  - EmailAgent: Send status update

Results:
  Ran ResearchAgent on objective: Find recent AI papers
  Ran TaskAgent on objective: Schedule meeting with team
  Ran EmailAgent on objective: Send status update
```

## Docker

```bash
docker build -t agentic-assistant deployments/
docker run agentic-assistant
```

## Key Concepts

- **Agent Framework**: Extensible base class for specialized agents.
- **Tool Use**: Agents can call tools (web search, email, document loading).
- **Memory**: Short-term (recent interactions) and long-term (persistent facts).
- **Orchestration**: Route tasks to appropriate agents based on objective.
