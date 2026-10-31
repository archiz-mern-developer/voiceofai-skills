# VoiceOfAI Platform Architecture & Core Reference

## Overview

VoiceOfAI is an enterprise voice platform enabling AI voice agents, outbound campaigns, phone number management, webhooks, and real-time CRM integration.

AI assistants interact with VoiceOfAI through the **VoiceOfAI MCP Server** (`voiceofai`), which exposes high-level tools for all platform capabilities.

## MCP Architecture & Authentication

- **Server Name:** `voiceofai`
- **Authentication:** Per-tenant authentication using the caller's VoiceOfAI API key.
- **Transports:** Stdio (local process via `run_stdio.py`) or HTTP/SSE (`run_http.py`).
- **Data Unwrapping:** Tool calls automatically unwrap the standard VoiceOfAI API response envelope `{"data": ...}` to return clean, structured JSON payloads directly to the AI assistant.

## Core Resources & MCP Tool Mapping

### 1. Agents
Voice AI agent configurations (system prompts, TTS voice, LLM model, transfer rules, flow graphs).
- **Tools:** `create_agent`, `list_agents`, `get_agent`, `update_agent`, `delete_agent`, `export_agent_flow`, `import_agent_flow`.

### 2. Calls
Single outbound or inbound call sessions with status, duration, transcripts, AI summaries, and recordings.
- **Tools:** `trigger_call`, `list_calls`, `get_call`, `hangup_call`.

### 3. Campaigns
Bulk calling operations executing an agent across hundreds or thousands of contacts with concurrency controls and calling windows.
- **Tools:** `create_campaign`, `list_campaigns`, `get_campaign`, `add_campaign_contacts`, `upload_campaign_csv`, `start_campaign`, `pause_campaign`.

### 4. Contacts
CRM customer records enriched with lead scores and call history.
- **Tools:** `list_contacts`, `create_contact`, `get_contact`, `update_contact`, `delete_contact`, `bulk_import_contacts`.

### 5. Incoming Connections
Map incoming phone numbers to specific voice agents for inbound IVR / receptionist routing.
- **Tools:** `list_incoming_connections`, `link_incoming_connection`, `unlink_incoming_connection`.

### 6. Credits
Credit-based billing system where **1 credit = 1 minute of call time**.
- **Tools:** `get_credit_balance`, `get_credit_usage`.

### 7. Analytics
Aggregated call stats, cross-campaign performance comparisons, and executive dashboard summaries.
- **Tools:** `get_call_analytics`, `get_campaign_analytics`, `get_analytics_summary`.

### 8. Webhooks
HTTP event subscriptions for real-time lifecycle event notifications with HMAC-SHA256 signature verification.
- **Tools:** `list_webhooks`, `list_webhook_events`, `create_webhook`, `update_webhook`, `delete_webhook`, `test_webhook`.
