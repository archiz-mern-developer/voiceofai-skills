---
name: make-call
description: "Trigger, place, schedule, or test an outbound phone call with a VoiceOfAI voice agent. Use when placing a test call, dialing a recipient, or scheduling a future call."
license: MIT
compatibility: Requires internet access and VOICEOFAI_API_KEY.
metadata:
  openclaw:
    requires:
      env:
        - VOICEOFAI_API_KEY
    primaryEnv: VOICEOFAI_API_KEY
---

# Make Outbound VoiceOfAI Call

## Endpoint

- **Endpoint:** `POST https://voice.voiceofai.co.in/api/v1/calls`
- **Auth:** `Authorization: Bearer $VOICEOFAI_API_KEY`

## Requirements

- `agentId`: UUID of active voice agent.
- `toNumber`: Recipient phone number in E.164 standard format (e.g. `+14155551234`).

## Optional Fields

- `engine`: Telephony provider (`voiceofai`, `elevenlabs`, `plivo`, `twilio-openai`). Default `voiceofai`.
- `fromNumber`: E.164 caller ID number.
- `metadata`: Key-value payload for personalization tokens (e.g. `{"customer_name": "Priya"}`).
- `scheduledAt`: ISO-8601 timestamp string for future calls (e.g. `"2026-08-25T14:30:00Z"`).

## Example Payload

```json
{
  "agentId": "123e4567-e89b-12d3-a456-426655440000",
  "toNumber": "+14155551234",
  "engine": "voiceofai",
  "metadata": {
    "account_id": "ACC987",
    "customer_name": "John Doe"
  }
}
```

## Helper Script

```bash
python3 make-call/scripts/make_call.py \
  --agent-id "123e4567-e89b-12d3-a456-426655440000" \
  --to "+14155551234"
```
