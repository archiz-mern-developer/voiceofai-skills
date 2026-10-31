---
name: setup-webhook
description: "Register, list, update, test, or delete HTTP webhook event subscriptions for real-time call and campaign status notifications using MCP tools."
license: MIT
compatibility: Requires VoiceOfAI MCP server connection (FastMCP / voiceofai).
metadata:
  mcp:
    server: voiceofai
    tools:
      - list_webhooks
      - list_webhook_events
      - create_webhook
      - update_webhook
      - delete_webhook
      - test_webhook
---

# Setup VoiceOfAI Webhooks

## Overview

Use the `voiceofai` MCP tools to configure HTTP webhook subscriptions that receive real-time notifications for call lifecycle changes, campaign events, contact additions, and credit alerts.

## Supported Webhook Events
Query dynamically via `list_webhook_events`, or subscribe to any of:
- `call.started`: Call answered and session started.
- `call.completed`: Call terminated naturally.
- `call.failed`: Call failed or encountered carrier error.
- `campaign.started`: Outbound campaign began dialing.
- `campaign.completed`: All campaign contacts dialed.
- `campaign.paused`: Campaign execution paused.
- `contact.created`: New CRM contact record created.
- `contact.updated`: Existing CRM contact record modified.
- `credits.low`: Account credit balance dropped below warning threshold.
- `credits.depleted`: Account credit balance reached 0.

## Webhook Signature Verification
Delivered HTTP requests contain an `X-Webhook-Signature` header signed with your webhook secret using **HMAC-SHA256**.

## Available MCP Tools

### 1. `list_webhook_events`
List all event types available for subscription.

**Arguments:** None

**Example Tool Invocation:**
```json
{
  "name": "list_webhook_events",
  "arguments": {}
}
```

---

### 2. `list_webhooks`
List all configured webhook subscriptions, their subscribed events, active status, and failure counts.

**Arguments:** None

**Example Tool Invocation:**
```json
{
  "name": "list_webhooks",
  "arguments": {}
}
```

---

### 3. `create_webhook`
Register a new webhook subscription.

**Arguments:**
- `url` (string, required): Destination HTTPS URL (e.g. `"https://api.mycrm.com/webhooks/voiceofai"`).
- `events` (string[], required): List of event strings to subscribe to.
- `description` (string, optional): Human-readable label for the subscription.
- `secret` (string, optional): Custom HMAC-SHA256 secret. If omitted, VoiceOfAI generates one automatically.

**Example Tool Invocation:**
```json
{
  "name": "create_webhook",
  "arguments": {
    "url": "https://api.example.com/webhooks/voiceofai",
    "events": ["call.completed", "call.failed", "credits.low"],
    "description": "Production Call Handler"
  }
}
```

---

### 4. `update_webhook`
Update a webhook's destination URL, subscribed events, active status, or description.

**Arguments:**
- `webhook_id` (string, required): UUID of the webhook.
- `url` (string, optional): New HTTPS URL.
- `events` (string[], optional): New list of event names.
- `is_active` (boolean, optional): Set to `false` to pause deliveries without deleting the record.
- `description` (string, optional): Updated description.

**Example Tool Invocation:**
```json
{
  "name": "update_webhook",
  "arguments": {
    "webhook_id": "whk_123e4567-e89b-12d3-a456-426655440000",
    "is_active": false
  }
}
```

---

### 5. `test_webhook`
Dispatch a synthetic test ping to verify that the destination server is reachable and responds with HTTP 200.

**Arguments:**
- `webhook_id` (string, required): UUID of the webhook to test.

**Example Tool Invocation:**
```json
{
  "name": "test_webhook",
  "arguments": {
    "webhook_id": "whk_123e4567-e89b-12d3-a456-426655440000"
  }
}
```

---

### 6. `delete_webhook`
Permanently remove a webhook subscription.

**Arguments:**
- `webhook_id` (string, required): UUID of the webhook to delete.

**Example Tool Invocation:**
```json
{
  "name": "delete_webhook",
  "arguments": {
    "webhook_id": "whk_123e4567-e89b-12d3-a456-426655440000"
  }
}
```
