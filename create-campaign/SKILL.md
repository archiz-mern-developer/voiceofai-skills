---
name: create-campaign
description: "Create, configure, populate with contacts, start, pause, or monitor bulk outbound calling campaigns using MCP tools. Use when setting up broadcast campaigns or batch dialing lists."
license: MIT
compatibility: Requires VoiceOfAI MCP server connection (FastMCP / voiceofai).
metadata:
  mcp:
    server: voiceofai
    tools:
      - create_campaign
      - list_campaigns
      - get_campaign
      - add_campaign_contacts
      - upload_campaign_csv
      - start_campaign
      - pause_campaign
---

# Create & Manage VoiceOfAI Campaigns

## Overview

Use the `voiceofai` MCP tools to execute bulk calling campaigns across contact lists. Campaigns start in `draft` status, are populated with contacts, and dial up to your configured concurrency limit once started.

## Campaign Lifecycle Statuses
`draft` ➔ `scheduled` / `running` ➔ `paused` ➔ `completed`

## Available MCP Tools

### 1. `create_campaign`
Create a new calling campaign (initialized in `draft` status).

**Arguments:**
- `name` (string, required): Display name of the campaign.
- `agent_id` (string, required): UUID of the voice agent to execute the calls.
- `engine` (string, optional, default `"voiceofai"`): Telephony provider (`"voiceofai"`, `"elevenlabs"`, `"plivo"`, or `"twilio-openai"`).
- `phone_number_id` (string, optional): Outbound caller ID phone number ID.
- `call_window_start` (string, optional): Calling window start time in 24-hr `"HH:MM"` format (e.g. `"09:00"`).
- `call_window_end` (string, optional): Calling window end time in 24-hr `"HH:MM"` format (e.g. `"18:00"`).
- `max_concurrent_calls` (integer, optional): Maximum simultaneous calls allowed (1 to 100).
- `scheduled_start_time` (string, optional): ISO-8601 timestamp to delay starting calls.
- `timezone` (string, optional): Timezone for the call window (e.g. `"America/New_York"`, `"Asia/Kolkata"`).
- `contacts_csv_base64` (string, optional): Base64-encoded CSV string to import contacts immediately at creation.
- `contacts_csv_filename` (string, optional, default `"contacts.csv"`): Filename for the uploaded CSV.

**Example Tool Invocation:**
```json
{
  "name": "create_campaign",
  "arguments": {
    "name": "Q4 Reactivation Outreach",
    "agent_id": "ag_123e4567-e89b-12d3-a456-426655440000",
    "call_window_start": "09:00",
    "call_window_end": "18:00",
    "max_concurrent_calls": 5,
    "timezone": "America/New_York"
  }
}
```

---

### 2. `add_campaign_contacts`
Add contacts directly as JSON objects (up to 10,000 contacts per request). The campaign must be in `draft` or `paused` status.

**Arguments:**
- `campaign_id` (string, required): UUID of the campaign.
- `contacts` (array of objects, required): Each contact supports:
  - `phoneNumber` (string, required, E.164 format e.g. `"+14155551234"`).
  - `firstName` (string, optional).
  - `lastName` (string, optional).
  - `email` (string, optional).
  - `customFields` (object, optional): Dictionary for dynamic script variables (e.g. `{"due_date": "Nov 5"}`).

**Example Tool Invocation:**
```json
{
  "name": "add_campaign_contacts",
  "arguments": {
    "campaign_id": "cmp_987e6543-e21b-12d3-a456-426655440000",
    "contacts": [
      {
        "phoneNumber": "+14155551234",
        "firstName": "John",
        "lastName": "Doe",
        "customFields": { "account_tier": "Gold" }
      },
      {
        "phoneNumber": "+14155559876",
        "firstName": "Jane",
        "lastName": "Smith",
        "customFields": { "account_tier": "Platinum" }
      }
    ]
  }
}
```

---

### 3. `upload_campaign_csv`
Bulk-import contacts from a base64-encoded CSV file (up to 10MB / 10,000 rows).

**CSV Format:**
- Required column: `phone` or `phone_number` (E.164 format).
- Optional columns: `firstName`/`first_name`, `lastName`/`last_name`, `email`, and custom field columns.

**Arguments:**
- `campaign_id` (string, required): UUID of the campaign.
- `csv_base64` (string, required): Base64-encoded CSV text content.
- `filename` (string, optional, default `"contacts.csv"`).

**Example Tool Invocation:**
```json
{
  "name": "upload_campaign_csv",
  "arguments": {
    "campaign_id": "cmp_987e6543-e21b-12d3-a456-426655440000",
    "csv_base64": "cGhvbmUsZmlyc3RfbmFtZSxhY2NvdW50X3RpZXINCisxNDE1NTU1MTIzNCxKb2huLEdvbGQNCisxNDE1NTU1OTg3NixKYW5lLFBsYXRpbnVt"
  }
}
```

---

### 4. `start_campaign`
Start (or resume) dialing contacts in the campaign according to the concurrency limits and calling window.

**Arguments:**
- `campaign_id` (string, required): UUID of the campaign.

**Example Tool Invocation:**
```json
{
  "name": "start_campaign",
  "arguments": {
    "campaign_id": "cmp_987e6543-e21b-12d3-a456-426655440000"
  }
}
```

---

### 5. `pause_campaign`
Pause a running campaign. In-progress calls finish normally, but no new calls will start until `start_campaign` is called again.

**Arguments:**
- `campaign_id` (string, required): UUID of the campaign.

**Example Tool Invocation:**
```json
{
  "name": "pause_campaign",
  "arguments": {
    "campaign_id": "cmp_987e6543-e21b-12d3-a456-426655440000"
  }
}
```

---

### 6. `get_campaign`
Inspect campaign progress (total contacts, calls completed, remaining, answered rate, active concurrency).

**Arguments:**
- `campaign_id` (string, required): UUID of the campaign.

**Example Tool Invocation:**
```json
{
  "name": "get_campaign",
  "arguments": {
    "campaign_id": "cmp_987e6543-e21b-12d3-a456-426655440000"
  }
}
```

---

### 7. `list_campaigns`
List all bulk calling campaigns, paginated.

**Arguments:**
- `page` (integer, optional, default `1`).
- `page_size` (integer, optional, default `20`).

**Example Tool Invocation:**
```json
{
  "name": "list_campaigns",
  "arguments": {
    "page": 1,
    "page_size": 10
  }
}
```
