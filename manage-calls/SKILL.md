---
name: manage-calls
description: "List call history, inspect call transcripts, review AI summaries and recordings, or terminate active calls using MCP tools. Use when checking call logs, analyzing call output, or terminating in-progress calls."
license: MIT
compatibility: Requires VoiceOfAI MCP server connection (FastMCP / voiceofai).
metadata:
  mcp:
    server: voiceofai
    tools:
      - list_calls
      - get_call
      - hangup_call
---

# Manage & Inspect VoiceOfAI Calls

## Overview

Monitor, inspect, and manage voice calls across your account using the `voiceofai` MCP tools.

## Call Lifecycle Statuses
1. `queued`: Call request accepted; waiting for telephony dispatch.
2. `ringing`: Destination carrier and handset are currently ringing.
3. `in-progress`: Call answered; conversation active between caller and AI agent.
4. `completed`: Call completed normally.
5. `failed` / `busy` / `no-answer`: Call did not connect or encountered an error.

## Available MCP Tools

### 1. `list_calls`
List past and active calls across all telephony engines, paginated.

**Arguments:**
- `page` (integer, optional, default `1`): Page number.
- `page_size` (integer, optional, default `20`): Records per page.

**Example Tool Invocation:**
```json
{
  "name": "list_calls",
  "arguments": {
    "page": 1,
    "page_size": 10
  }
}
```

---

### 2. `get_call`
Fetch comprehensive details for a single call session, including conversational transcript, automated AI summary, sentiment analysis, duration, and audio recording URL.

**Arguments:**
- `call_id` (string, required): UUID of the call.

**Example Tool Invocation:**
```json
{
  "name": "get_call",
  "arguments": {
    "call_id": "call_987e6543-e21b-12d3-a456-426655440000"
  }
}
```

**Returned Data Structure:**
```json
{
  "id": "call_987e6543-e21b-12d3-a456-426655440000",
  "status": "completed",
  "durationSeconds": 142,
  "sentiment": "positive",
  "aiSummary": "Customer confirmed attendance for their appointment tomorrow at 3:00 PM.",
  "recordingUrl": "https://storage.voiceofai.co.in/recordings/call_987e6543.mp3",
  "transcript": [
    {"speaker": "agent", "message": "Hi Emily, this is Alex from SunPower. Am I speaking with the homeowner?", "timestamp": "00:02"},
    {"speaker": "user", "message": "Yes, this is Emily. How can I help you?", "timestamp": "00:06"},
    {"speaker": "agent", "message": "I'm calling to confirm your solar consultation scheduled for tomorrow at 3 PM.", "timestamp": "00:10"}
  ]
}
```

---

### 3. `hangup_call`
Immediately terminate an active call.

> ℹ️ Only functions while the call status is `ringing` or `in-progress`.

**Arguments:**
- `call_id` (string, required): UUID of the active call to terminate.

**Example Tool Invocation:**
```json
{
  "name": "hangup_call",
  "arguments": {
    "call_id": "call_987e6543-e21b-12d3-a456-426655440000"
  }
}
```
