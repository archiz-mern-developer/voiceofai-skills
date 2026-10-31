---
name: create-agent
description: "Create a VoiceOfAI voice agent (incoming or flow type) with system prompt, voice, LLM model, language, call controls, and transfer options using the create_agent MCP tool. Use when building, provisioning, or cloning AI voice agents."
license: MIT
compatibility: Requires VoiceOfAI MCP server connection (FastMCP / voiceofai).
metadata:
  mcp:
    server: voiceofai
    tools:
      - create_agent
---

# Create VoiceOfAI Agent

## Overview

Use the `create_agent` tool in the `voiceofai` MCP server to create a new voice agent under your account.

- **MCP Tool:** `create_agent`
- **Agent Types:**
  - `incoming`: Simple prompt-driven agent for inbound calls or automated outbound dialing. Requires `systemPrompt`.
  - `flow`: Multi-turn node-based visual conversation graph agent. Requires `personality`, `voiceTone`, and optionally `flowId`.

## Tool Arguments

The `create_agent` tool takes a single dictionary argument `agent_config`:

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | Yes | Agent display name. |
| `type` | string | Yes | Agent architecture type (`"incoming"` or `"flow"`). Immutable once created. |
| `systemPrompt` | string | Conditional | Complete system prompt instructions (required for `type: "incoming"`). |
| `personality` | string | Conditional | Core persona description (for `type: "flow"`). |
| `voiceTone` | string | Conditional | Tone guidelines e.g. `"friendly, empathetic, professional"` (for `type: "flow"`). |
| `flowId` | string | No | Linked conversation flow identifier (for `type: "flow"`). |
| `firstMessage` | string | No | Initial greeting spoken upon answer. Supports dynamic tokens (e.g. `"Hi {first_name}"`). |
| `language` | string | No | Language ISO code (e.g. `"en"`, `"hi"`, `"es"`, `"fr"`, `"de"`). Default: `"en"`. |
| `llmModel` | string | No | Underlying LLM model (e.g. `"gpt-4o-mini"`, `"gpt-4o"`, `"claude-3-5-sonnet"`). |
| `temperature` | number | No | Creativity parameter between `0.0` and `2.0` (default `0.7`). |
| `elevenLabsVoiceId` | string | No | 20-character ElevenLabs voice ID (e.g. `"21m00Tcm4TlvDq8ikWAM"`). |
| `openaiVoice` | string | No | OpenAI voice (`"alloy"`, `"echo"`, `"shimmer"`, `"ash"`, `"ballad"`, `"coral"`, `"sage"`, `"verse"`, `"cedar"`, `"marin"`). |
| `voiceStability` | number | No | ElevenLabs voice stability (`0.0` - `1.0`). |
| `voiceSimilarityBoost` | number | No | ElevenLabs similarity boost (`0.0` - `1.0`). |
| `voiceSpeed` | number | No | Speech rate multiplier (`0.5` - `2.0`). |
| `telephonyProvider` | string | No | Telephony carrier (`"twilio"`, `"plivo"`, or `"twilio_openai"`). |
| `knowledgeBaseIds` | string[] | No | UUID array of attached RAG knowledge base documents. |
| `transferEnabled` | boolean | No | Enable live call transfer to a human operator. |
| `transferPhoneNumber` | string | No | Target phone number in E.164 format (e.g. `"+14155551234"`). |
| `transferMessage` | string | No | Message spoken to caller before initiating transfer. |
| `detectLanguageEnabled` | boolean | No | Automatically detect and switch languages during call. |
| `endConversationEnabled` | boolean | No | Allow agent to hang up when task is completed. |
| `appointmentBookingEnabled`| boolean | No | Enable integrated appointment booking. |
| `maxDurationSeconds` | integer | No | Maximum call duration in seconds before auto-hangup (default `600`). |

## Example Tool Invocations

### 1. Minimal Incoming Support Agent
```json
{
  "name": "create_agent",
  "arguments": {
    "agent_config": {
      "name": "Customer Support Receptionist",
      "type": "incoming",
      "systemPrompt": "You are a courteous customer support assistant for VoiceOfAI. Assist users with general inquiries and answer questions concisely.",
      "firstMessage": "Hello! Thank you for calling VoiceOfAI support. How can I help you today?",
      "language": "en",
      "llmModel": "gpt-4o-mini",
      "openaiVoice": "alloy",
      "telephonyProvider": "twilio"
    }
  }
}
```

### 2. Advanced Outbound Sales Agent with Transfer
```json
{
  "name": "create_agent",
  "arguments": {
    "agent_config": {
      "name": "Solar Inquiry Follow-up",
      "type": "incoming",
      "systemPrompt": "You are calling to follow up on a solar quote request. Determine if the homeowner qualifies and offer to connect them to a senior specialist.",
      "firstMessage": "Hi {first_name}, this is Alex calling from SunPower. Am I speaking with the homeowner?",
      "language": "en",
      "llmModel": "gpt-4o",
      "elevenLabsVoiceId": "21m00Tcm4TlvDq8ikWAM",
      "temperature": 0.5,
      "maxDurationSeconds": 480,
      "transferEnabled": true,
      "transferPhoneNumber": "+14155559876",
      "transferMessage": "Great! Let me connect you directly with our senior solar engineer. Please hold for just a moment.",
      "endConversationEnabled": true
    }
  }
}
```

## Response

Returns the newly created agent record including its generated `id`:
```json
{
  "id": "ag_123e4567-e89b-12d3-a456-426655440000",
  "name": "Customer Support Receptionist",
  "type": "incoming",
  "status": "active",
  "createdAt": "2026-10-31T12:00:00Z"
}
```
Use this `id` when triggering calls (`trigger_call`), creating campaigns (`create_campaign`), or routing incoming calls (`link_incoming_connection`).
