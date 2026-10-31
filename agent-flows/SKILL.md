---
name: agent-flows
description: "Export visual flow graphs (JSON nodes, edges, variables) from 'flow'-type agents, or replace an existing flow configuration using MCP tools. Use when backing up visual graph agents, editing nodes/edges, or restoring flow templates."
license: MIT
compatibility: Requires VoiceOfAI MCP server connection (FastMCP / voiceofai).
metadata:
  mcp:
    server: voiceofai
    tools:
      - export_agent_flow
      - import_agent_flow
---

# Export & Import Visual Agent Flows

## Overview

Use the `voiceofai` MCP tools to export and import multi-turn conversational flow graphs for `flow`-type voice agents. Flows are represented as structured graphs containing nodes (speech prompts, inputs, conditional logic), directed edges, and variables.

## Flow Graph Object Structure

```json
{
  "name": "Payment Assistance Flow",
  "nodes": [
    {
      "id": "node_start",
      "type": "speak",
      "data": {
        "text": "Hello! I can help you process your invoice payment today. What is your invoice number?"
      }
    },
    {
      "id": "node_collect_invoice",
      "type": "input",
      "data": {
        "variable": "invoice_id"
      }
    }
  ],
  "edges": [
    {
      "id": "edge_1",
      "source": "node_start",
      "target": "node_collect_invoice"
    }
  ],
  "variables": {
    "invoice_id": null
  }
}
```

## Available MCP Tools

### 1. `export_agent_flow`
Export the visual conversation flow graph (nodes, edges, and state variables) for a specified `flow`-type agent.

> ℹ️ The target agent must have `type: "flow"`.

**Arguments:**
- `agent_id` (string, required): UUID of the flow agent.

**Example Tool Invocation:**
```json
{
  "name": "export_agent_flow",
  "arguments": {
    "agent_id": "ag_123e4567-e89b-12d3-a456-426655440000"
  }
}
```

**Returned Data Structure:**
Returns the complete flow object containing `name`, `nodes`, `edges`, and `variables`.

---

### 2. `import_agent_flow`
Replace an agent's visual conversation flow entirely with an updated flow graph.

> ⚠️ **Warning:** This operation completely overwrites the existing flow graph. It is recommended to call `export_agent_flow` first to preserve a backup.

**Arguments:**
- `agent_id` (string, required): UUID of the flow agent.
- `flow` (object, required): Flow definition containing `name` (string), `nodes` (array), `edges` (array), and `variables` (object).

**Example Tool Invocation:**
```json
{
  "name": "import_agent_flow",
  "arguments": {
    "agent_id": "ag_123e4567-e89b-12d3-a456-426655440000",
    "flow": {
      "name": "Updated Flow",
      "nodes": [
        {
          "id": "node_greeting",
          "type": "speak",
          "data": {
            "text": "Thank you for calling customer service. How can I direct your call?"
          }
        }
      ],
      "edges": [],
      "variables": {}
    }
  }
}
```
