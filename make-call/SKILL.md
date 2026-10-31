---
name: make-call
description: "Trigger, place, schedule, or test an outbound phone call with a VoiceOfAI voice agent using the trigger_call MCP tool. Supports scheduling with ISO 8601 timezone timestamps and automated retry configurations."
license: MIT
compatibility: Requires VoiceOfAI MCP server connection (FastMCP / voiceofai).
metadata:
  mcp:
    server: voiceofai
    tools:
      - trigger_call
---

# Make Outbound VoiceOfAI Call

## Overview

Use the `trigger_call` tool in the `voiceofai` MCP server to initiate an immediate or scheduled outbound call using an existing agent.

- **MCP Tool:** `trigger_call`
- **Billing:** 1 credit per minute of connected call time.

## Tool Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `agent_id` | string | Yes | UUID of the active voice agent to use. |
| `to_number` | string | Yes | Destination phone number in E.164 format (e.g. `"+14155551234"`). |
| `engine` | string | No | Telephony engine. Options: `"voiceofai"` (default), `"elevenlabs"`, `"plivo"`, or `"twilio-openai"`. |
| `from_number` | string | No | Caller ID number in E.164 format. Omit to use the account's default caller ID. |
| `metadata` | object | No | Custom key-value pairs passed into the call context for personalization tokens (e.g. `{"first_name": "Sarah", "account_id": "ACC-99"}`). |
| `scheduled_at` | string | No | Date and time in **ISO 8601 format with timezone** to schedule the call for the future (e.g. `"2026-10-24T10:33:00+05:30"` or `"2026-11-01T14:30:00Z"`). |
| `retry_config` | object | No | Automated retry configuration for unanswered or failed calls. See schema below. |

---

## Retry Configuration Schema (`retry_config`)

The `retry_config` object controls automated redialing when a call does not connect, encounters an error, or reaches voicemail.

```json
{
  "enabled": true,
  "max_retries": 1,
  "retry_intervals_minutes": [15],
  "retry_on_statuses": ["failed", "error"],
  "retry_on_voicemail": true
}
```

### Constraints & Validation Rules:

- **`enabled`** (`boolean`, required): `true` to enable automatic retries, `false` to disable.
- **`max_retries`** (`integer`, required): Allowed values are strictly **`1`**, **`2`**, or **`3`**.
- **`retry_intervals_minutes`** (`array of integers`, required):
  - The length of the array **must be equal to `max_retries`** (e.g., length `1` if `max_retries: 1`, length `2` if `max_retries: 2`, length `3` if `max_retries: 3`).
  - Each interval value must be an integer between **`15`** and **`1440`** (minutes between retry attempts).
- **`retry_on_statuses`** (`array of strings`, required):
  - May only contain any combination of the following allowed statuses:
    - `"failed"`
    - `"error"`
    - `"no-answer"`
    - `"busy"`
- **`retry_on_voicemail`** (`boolean`, required): `true` to trigger a retry if an answering machine / voicemail is detected, or `false` to treat voicemail as completed without retrying.

---

## Example Tool Invocations

### 1. Immediate Test Call
```json
{
  "name": "trigger_call",
  "arguments": {
    "agent_id": "ag_123e4567-e89b-12d3-a456-426655440000",
    "to_number": "+14155551234"
  }
}
```

### 2. Scheduled Call with Retry Configuration
```json
{
  "name": "trigger_call",
  "arguments": {
    "agent_id": "ag_123e4567-e89b-12d3-a456-426655440000",
    "to_number": "+14155551234",
    "scheduled_at": "2026-10-24T10:33:00+05:30",
    "retry_config": {
      "enabled": true,
      "max_retries": 1,
      "retry_intervals_minutes": [15],
      "retry_on_statuses": ["failed", "error"],
      "retry_on_voicemail": true
    }
  }
}
```

### 3. Multi-Retry Scheduled Call with Metadata
```json
{
  "name": "trigger_call",
  "arguments": {
    "agent_id": "ag_123e4567-e89b-12d3-a456-426655440000",
    "to_number": "+14155551234",
    "engine": "voiceofai",
    "scheduled_at": "2026-11-05T15:00:00+05:30",
    "metadata": {
      "first_name": "Emily",
      "appointment_time": "3:00 PM tomorrow",
      "service_type": "Dental Checkup"
    },
    "retry_config": {
      "enabled": true,
      "max_retries": 2,
      "retry_intervals_minutes": [15, 60],
      "retry_on_statuses": ["failed", "error", "no-answer", "busy"],
      "retry_on_voicemail": false
    }
  }
}
```

---

## Response

Returns the call session object including its generated `call_id` and initial status (`queued`):
```json
{
  "callId": "call_987e6543-e21b-12d3-a456-426655440000",
  "agentId": "ag_123e4567-e89b-12d3-a456-426655440000",
  "toNumber": "+14155551234",
  "status": "queued",
  "scheduledAt": "2026-10-24T10:33:00+05:30",
  "createdAt": "2026-10-31T12:00:00Z"
}
```

Use `get_call` from the `manage-calls` skill to track status, inspect transcripts, or review call recordings.
