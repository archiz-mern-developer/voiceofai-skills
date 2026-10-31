---
name: setup-incoming
description: "Link or unlink voice agents to phone numbers to handle incoming inbound calls using MCP tools. Use when configuring IVR receptionist agents, checking unlinked numbers, setting up inbound routing, or releasing phone numbers."
license: MIT
compatibility: Requires VoiceOfAI MCP server connection (FastMCP / voiceofai).
metadata:
  mcp:
    server: voiceofai
    tools:
      - list_incoming_connections
      - link_incoming_connection
      - unlink_incoming_connection
---

# Setup Inbound Call Routing

## Overview

Use the `voiceofai` MCP tools to connect an active `incoming`-type voice agent to a phone number owned by your account so it automatically answers and processes inbound phone calls.

## Requirements
- The voice agent must have `type: "incoming"` and be in `active` status.
- The phone number must be owned by your account and must not be currently in use by an active outbound campaign.

## Available MCP Tools

### 1. `list_incoming_connections`
List all active agent ↔ phone number connections, available unlinked phone numbers, and eligible `incoming` voice agents.

**Arguments:** None

**Example Tool Invocation:**
```json
{
  "name": "list_incoming_connections",
  "arguments": {}
}
```

**Returned Data Structure:**
```json
{
  "connections": [
    {
      "connectionId": "conn_123e4567-e89b-12d3-a456-426655440000",
      "agentId": "ag_123e4567-e89b-12d3-a456-426655440000",
      "agentName": "Support Receptionist",
      "phoneNumberId": "num_987e6543-e21b-12d3-a456-426655440000",
      "phoneNumber": "+14155551000",
      "createdAt": "2026-10-15T09:00:00Z"
    }
  ],
  "unlinkedPhoneNumbers": [
    {
      "id": "num_555e1234-e21b-12d3-a456-426655440000",
      "phoneNumber": "+14155552000",
      "provider": "twilio"
    }
  ],
  "availableAgents": [
    {
      "id": "ag_444e1234-e21b-12d3-a456-426655440000",
      "name": "Billing Agent",
      "type": "incoming"
    }
  ]
}
```

---

### 2. `link_incoming_connection`
Bind an `incoming` agent to an unlinked phone number to begin receiving calls immediately.

**Arguments:**
- `agent_id` (string, required): UUID of the incoming agent.
- `phone_number_id` (string, required): UUID of the phone number.

**Example Tool Invocation:**
```json
{
  "name": "link_incoming_connection",
  "arguments": {
    "agent_id": "ag_444e1234-e21b-12d3-a456-426655440000",
    "phone_number_id": "num_555e1234-e21b-12d3-a456-426655440000"
  }
}
```

---

### 3. `unlink_incoming_connection`
Remove an agent-to-phone connection. The phone number becomes unlinked and stops answering calls for that agent.

**Arguments:**
- `connection_id` (string, required): UUID of the connection to remove.

**Example Tool Invocation:**
```json
{
  "name": "unlink_incoming_connection",
  "arguments": {
    "connection_id": "conn_123e4567-e89b-12d3-a456-426655440000"
  }
}
```
