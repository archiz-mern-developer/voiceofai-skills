---
name: setup-api-key
description: "Verify, test, and troubleshoot the VoiceOfAI MCP server connection and authentication. Use when starting a VoiceOfAI project, verifying credentials, diagnosing unauthorized errors, or checking platform connectivity."
license: MIT
compatibility: Requires VoiceOfAI MCP server connection (FastMCP / voiceofai).
metadata:
  mcp:
    server: voiceofai
    tools:
      - health_check
      - get_credit_balance
---

# Setup & Verify VoiceOfAI Connection

## Overview

The VoiceOfAI MCP server connects your AI assistant directly to the VoiceOfAI platform. Every MCP tool call is authenticated using your VoiceOfAI API key.

- **MCP Server Name:** `voiceofai`
- **Dashboard:** Retrieve your API key from **VoiceOfAI Dashboard → Settings → Developer**.
- **Credit Value:** 1 credit = 1 minute of call time.

## MCP Tools for Setup & Diagnostics

### 1. `health_check`
Check whether the VoiceOfAI API is online, healthy, and reachable.

**Parameters:** None

**Example Tool Invocation:**
```json
{
  "name": "health_check",
  "arguments": {}
}
```

**Expected Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

---

### 2. `get_credit_balance`
Verify that your API key is authentic and active by querying your account credit balance.

**Parameters:** None

**Example Tool Invocation:**
```json
{
  "name": "get_credit_balance",
  "arguments": {}
}
```

**Expected Response:**
```json
{
  "available": 450.5,
  "reserved": 15.0,
  "total": 465.5
}
```

## Troubleshooting Authentication

- **Error 401 / Unauthorized:** Ensure your API key is properly set in your MCP server environment (`VOICEOFAI_API_KEY`) or in the HTTP `Authorization: Bearer <key>` header.
- **Connection Refused:** Verify internet access and confirm that `https://voice.voiceofai.co.in` is reachable.
- **Credits Depleted:** If credits are `0.0`, outbound calls and campaigns will be paused until topped up.
