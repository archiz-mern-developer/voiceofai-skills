---
name: manage-credits
description: "Check available calling credit balance and view daily credit usage history using MCP tools. Use when monitoring call minute quotas, checking billing status, or auditing daily usage."
license: MIT
compatibility: Requires VoiceOfAI MCP server connection (FastMCP / voiceofai).
metadata:
  mcp:
    server: voiceofai
    tools:
      - get_credit_balance
      - get_credit_usage
---

# Manage VoiceOfAI Account Credits

## Overview

VoiceOfAI uses a credit-based billing system where **1 credit equals 1 minute of call time**. Use the `voiceofai` MCP tools to query your balance and monitor consumption trends over time.

## Available MCP Tools

### 1. `get_credit_balance`
Query the current credit balance (available, reserved, and total minutes) for the authenticated account.

**Arguments:** None

**Example Tool Invocation:**
```json
{
  "name": "get_credit_balance",
  "arguments": {}
}
```

**Returned Data Structure:**
```json
{
  "available": 450.5,
  "reserved": 15.0,
  "total": 465.5
}
```
- `available`: Credits immediately available for outbound and inbound calls.
- `reserved`: Credits currently earmarked by in-flight calls or active campaigns.
- `total`: Total balance (`available + reserved`).

---

### 2. `get_credit_usage`
Retrieve day-by-day credit usage history and call counts for a specified historical window.

**Arguments:**
- `days` (integer, optional, default `30`): Lookback period in days (1 to 90).

**Example Tool Invocation:**
```json
{
  "name": "get_credit_usage",
  "arguments": {
    "days": 14
  }
}
```

**Returned Data Structure:**
```json
{
  "history": [
    {
      "date": "2026-10-30",
      "creditsUsed": 42.5,
      "callCount": 18
    },
    {
      "date": "2026-10-29",
      "creditsUsed": 65.0,
      "callCount": 27
    }
  ],
  "totalCreditsUsed": 107.5,
  "totalCalls": 45
}
```
