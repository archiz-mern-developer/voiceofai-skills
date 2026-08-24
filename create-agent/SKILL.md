---
name: create-agent
description: "Create a VoiceOfAI voice agent (incoming or flow type) with system prompt, voice, LLM model, language, call controls, and transfer options. Use when building, provisioning, or cloning AI voice agents."
license: MIT
compatibility: Requires internet access and VOICEOFAI_API_KEY.
metadata:
  openclaw:
    requires:
      env:
        - VOICEOFAI_API_KEY
    primaryEnv: VOICEOFAI_API_KEY
---

# Create VoiceOfAI Agent

## Overview

- **Endpoint:** `POST https://voice.voiceofai.co.in/api/v1/agents`
- **Auth:** `Authorization: Bearer $VOICEOFAI_API_KEY`
- **Agent Types:**
  - `incoming`: Simple prompt-driven voice agent for inbound or simple outbound calls.
  - `flow`: Node-based visual conversation graph agent.

## Request Schema

```json
{
  "name": "Customer Support Agent",
  "type": "incoming",
  "systemPrompt": "You are a professional customer support agent for VoiceOfAI. Keep answers helpful and concise.",
  "firstMessage": "Hello! Thank you for calling VoiceOfAI support. How can I help you today?",
  "language": "en",
  "llmModel": "gpt-4o-mini",
  "temperature": 0.7,
  "maxDurationSeconds": 600,
  "telephonyProvider": "twilio",
  "openaiVoice": "alloy",
  "transferEnabled": false,
  "transferPhoneNumber": "+14155551234",
  "transferMessage": "Transferring you to a live representative now."
}
```

## Common Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | string | Yes | Agent display name. |
| `type` | string | Yes | Agent type (`incoming` or `flow`). |
| `systemPrompt` | string | Conditional | System prompt (required for `incoming`). |
| `personality` | string | Conditional | Voice personality description (for `flow`). |
| `firstMessage` | string | No | Greeting spoken when call is connected. |
| `language` | string | No | Language code (e.g. `en`, `hi`, `es`). Default `en`. |
| `llmModel` | string | No | Underlying LLM model (e.g. `gpt-4o-mini`, `gpt-4o`). |
| `elevenLabsVoiceId` | string | No | 20-char ElevenLabs voice ID string. |
| `openaiVoice` | string | No | OpenAI Realtime voice (`alloy`, `echo`, `shimmer`, etc.). |
| `maxDurationSeconds` | integer | No | Maximum call duration in seconds (default `600`). |

## Helper Script

```bash
python3 create-agent/scripts/create_minimal_agent.py \
  --name "Support Agent" \
  --prompt "You are a friendly support assistant." \
  --first-message "Hi, thanks for calling!"
```
