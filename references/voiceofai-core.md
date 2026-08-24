# VoiceOfAI Platform Architecture & Core Reference

## Overview

VoiceOfAI is an enterprise voice platform enabling AI voice agents, outbound campaigns, phone number management, webhooks, and real-time CRM integration.

## API Specification

- **Default Base URL:** `https://voice.voiceofai.co.in/api/v1`
- **Testing Base URL:** `https://testing.voiceofai.co.in/api/v1`
- **Authentication Header:** `Authorization: Bearer $VOICEOFAI_API_KEY`
- **Content Type:** `application/json` (except multi-part CSV uploads)

## Standard Response Envelope

Every endpoint returns JSON wrapped in a standard envelope structure:

```json
{
  "success": true,
  "data": { ... },
  "meta": {
    "page": 1,
    "pageSize": 20,
    "total": 150
  }
}
```

When an error occurs:

```json
{
  "error": true,
  "status_code": 401,
  "details": {
    "message": "Invalid API Key"
  }
}
```

## Core Resources

1. **Agents:** Voice AI agent configurations (prompt, TTS voice, LLM model, transfer settings, flow graph).
2. **Calls:** Single outbound/inbound call sessions with status, duration, transcripts, AI summaries, and recordings.
3. **Campaigns:** Bulk calling operations executing an agent across thousands of contacts.
4. **Contacts:** CRM customer records enriched with lead scores and call history.
5. **Incoming Connections:** Map incoming phone numbers to specific voice agents.
6. **Credits:** Usage tracking (1 credit = 1 minute of calling time).
7. **Webhooks:** HTTP subscriptions for real-time lifecycle event notifications.
