---
name: setup-incoming
description: "Link or unlink voice agents to phone numbers to handle incoming inbound calls. Use when configuring IVR receptionist agents, setup inbound routing, or release unused phone numbers."
license: MIT
compatibility: Requires internet access and VOICEOFAI_API_KEY.
metadata:
  openclaw:
    requires:
      env:
        - VOICEOFAI_API_KEY
    primaryEnv: VOICEOFAI_API_KEY
---

# Setup Inbound Call Routing

## Overview

Connect an active `incoming`-type voice agent to a phone number owned by your account so it automatically answers inbound phone calls.

## Endpoints

- **List Connections & Unlinked Numbers:** `GET https://voice.voiceofai.co.in/api/v1/incoming-connections`
- **Link Agent to Phone Number:** `POST https://voice.voiceofai.co.in/api/v1/incoming-connections`
- **Unlink Phone Number:** `DELETE https://voice.voiceofai.co.in/api/v1/incoming-connections/{connection_id}`

## Link Payload

```json
{
  "agentId": "AGENT_UUID",
  "phoneNumberId": "PHONE_NUMBER_UUID"
}
```

## Helper Script

```bash
python3 setup-incoming/scripts/link_incoming.py \
  --agent-id "AGENT_UUID" \
  --phone-number-id "PHONE_NUMBER_UUID"
```
