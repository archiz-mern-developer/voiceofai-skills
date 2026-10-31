---
name: manage-contacts
description: "Create, list, inspect, update, delete, or bulk-import CRM contacts in VoiceOfAI using MCP tools. Enriched with call history, lead scores, and sentiment analysis."
license: MIT
compatibility: Requires VoiceOfAI MCP server connection (FastMCP / voiceofai).
metadata:
  mcp:
    server: voiceofai
    tools:
      - list_contacts
      - create_contact
      - get_contact
      - update_contact
      - delete_contact
      - bulk_import_contacts
---

# Manage VoiceOfAI CRM Contacts

## Overview

Manage customer CRM records directly within VoiceOfAI using the `voiceofai` MCP tools. As contacts participate in calls, records are automatically enriched with AI conversation summaries, sentiment analysis, and lead scores.

## Available MCP Tools

### 1. `list_contacts`
Retrieve a paginated list of CRM contacts, including enrichment scores and latest call disposition.

**Arguments:**
- `page` (integer, optional, default `1`).
- `page_size` (integer, optional, default `20`).

**Example Tool Invocation:**
```json
{
  "name": "list_contacts",
  "arguments": {
    "page": 1,
    "page_size": 20
  }
}
```

---

### 2. `create_contact`
Create an individual CRM contact.

**Arguments:**
- `phone` (string, required): Phone number in E.164 format (e.g. `"+14155551234"`).
- `first_name` (string, optional): First name.
- `last_name` (string, optional): Last name.
- `email` (string, optional): Email address.
- `company` (string, optional): Organization name.
- `tags` (string[], optional): Array of category tags (e.g. `["vip", "q4-lead"]`).
- `custom_fields` (object, optional): Key-value pairs for dynamic agent script variables.

**Example Tool Invocation:**
```json
{
  "name": "create_contact",
  "arguments": {
    "phone": "+14155551234",
    "first_name": "Jordan",
    "last_name": "Miller",
    "email": "jordan@example.com",
    "company": "Apex Dynamics",
    "tags": ["vip", "inbound-interest"],
    "custom_fields": {
      "plan": "Enterprise",
      "account_manager": "Sarah"
    }
  }
}
```

---

### 3. `get_contact`
Retrieve full contact details including AI-enriched call history, sentiment trend, and lead score.

**Arguments:**
- `contact_id` (string, required): UUID of the contact.

**Example Tool Invocation:**
```json
{
  "name": "get_contact",
  "arguments": {
    "contact_id": "cnt_123e4567-e89b-12d3-a456-426655440000"
  }
}
```

---

### 4. `update_contact`
Update contact details, custom fields, or pipeline stage. Pass only the fields you wish to modify.

**Arguments:**
- `contact_id` (string, required): UUID of the contact.
- `updates` (object, required): Fields to update (`phone`, `firstName`, `lastName`, `email`, `company`, `tags`, `customFields`, `stage`).

**Example Tool Invocation:**
```json
{
  "name": "update_contact",
  "arguments": {
    "contact_id": "cnt_123e4567-e89b-12d3-a456-426655440000",
    "updates": {
      "stage": "qualified_opportunity",
      "tags": ["vip", "qualified"]
    }
  }
}
```

---

### 5. `bulk_import_contacts`
Import up to 10,000 contacts in a single operation.

**Arguments:**
- `contacts` (array of objects, required): List of contact objects (`phone` required; optional `firstName`, `lastName`, `email`, `company`, `tags`, `customFields`).
- `skip_duplicates` (boolean, optional, default `true`): If `true`, duplicate phone numbers are skipped without throwing an error.

**Example Tool Invocation:**
```json
{
  "name": "bulk_import_contacts",
  "arguments": {
    "contacts": [
      {
        "phone": "+14155551234",
        "firstName": "Alice",
        "lastName": "Walker",
        "email": "alice@example.com"
      },
      {
        "phone": "+14155555678",
        "firstName": "Bob",
        "lastName": "Lee",
        "email": "bob@example.com"
      }
    ],
    "skip_duplicates": true
  }
}
```

---

### 6. `delete_contact`
Permanently delete a CRM contact.

> ℹ️ Call history records are preserved but unlinked from the deleted contact.

**Arguments:**
- `contact_id` (string, required): UUID of the contact.

**Example Tool Invocation:**
```json
{
  "name": "delete_contact",
  "arguments": {
    "contact_id": "cnt_123e4567-e89b-12d3-a456-426655440000"
  }
}
```
