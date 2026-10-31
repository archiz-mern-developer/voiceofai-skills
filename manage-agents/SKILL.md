---
name: manage-agents
description: "List, inspect, update, or delete existing VoiceOfAI voice agents using MCP tools. Use when inspecting configured agents, modifying prompts, changing voice settings, or deleting agents."
license: MIT
compatibility: Requires VoiceOfAI MCP server connection (FastMCP / voiceofai).
metadata:
  mcp:
    server: voiceofai
    tools:
      - list_agents
      - get_agent
      - update_agent
      - delete_agent
---

# Manage VoiceOfAI Agents

## Overview

Manage existing voice agents in your VoiceOfAI account using the `voiceofai` MCP tools.

## Available MCP Tools

### 1. `list_agents`
List all voice agents belonging to your account.

**Arguments:**
- `agent_type` (string, optional): Filter by agent type: `"incoming"` or `"flow"`. Omit to return all agents.

**Example Tool Invocation:**
```json
{
  "name": "list_agents",
  "arguments": {
    "agent_type": "incoming"
  }
}
```

---

### 2. `get_agent`
Fetch complete configuration details for a specific agent (prompts, voices, LLM, transfer settings, and flow metadata).

**Arguments:**
- `agent_id` (string, required): UUID of the agent.

**Example Tool Invocation:**
```json
{
  "name": "get_agent",
  "arguments": {
    "agent_id": "ag_123e4567-e89b-12d3-a456-426655440000"
  }
}
```

---

### 3. `update_agent`
Update an existing agent's configuration. Pass only the specific fields you wish to change. Every change is versioned.

> ⚠️ **Note:** An agent's `type` (`incoming` or `flow`) cannot be modified after creation.

**Arguments:**
- `agent_id` (string, required): UUID of the agent.
- `updates` (object, required): Key-value dictionary of updated fields (e.g. `systemPrompt`, `firstMessage`, `temperature`, `voiceSpeed`, `transferPhoneNumber`, etc.).

**Example Tool Invocation:**
```json
{
  "name": "update_agent",
  "arguments": {
    "agent_id": "ag_123e4567-e89b-12d3-a456-426655440000",
    "updates": {
      "systemPrompt": "You are an updated customer support agent. Be concise, polite, and direct.",
      "temperature": 0.5,
      "maxDurationSeconds": 900
    }
  }
}
```

---

### 4. `delete_agent`
Permanently delete an agent.

> ⚠️ **Warning:** Deletion cannot be undone. Any active outbound campaigns using this agent will be automatically paused.

**Arguments:**
- `agent_id` (string, required): UUID of the agent to delete.

**Example Tool Invocation:**
```json
{
  "name": "delete_agent",
  "arguments": {
    "agent_id": "ag_123e4567-e89b-12d3-a456-426655440000"
  }
}
```

## Related Skills
- **`create-agent`**: Provision a new voice agent.
- **`agent-flows`**: Export and import visual flow graphs for `flow`-type agents.
