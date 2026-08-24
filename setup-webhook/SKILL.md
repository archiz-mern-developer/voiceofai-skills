---
name: setup-webhook
description: "Register, update, test, or delete HTTP webhook event subscriptions for real-time call and campaign status notifications."
license: MIT
compatibility: Requires internet access and VOICEOFAI_API_KEY.
metadata:
  openclaw:
    requires:
      env:
        - VOICEOFAI_API_KEY
    primaryEnv: VOICEOFAI_API_KEY
---

# Setup VoiceOfAI Webhooks

## Endpoints

- **List Webhook Events:** `GET https://voice.voiceofai.co.in/api/v1/webhooks/events`
- **List Subscriptions:** `GET https://voice.voiceofai.co.in/api/v1/webhooks`
- **Create Subscription:** `POST https://voice.voiceofai.co.in/api/v1/webhooks`
- **Update Subscription:** `PUT https://voice.voiceofai.co.in/api/v1/webhooks/{webhook_id}`
- **Delete Subscription:** `DELETE https://voice.voiceofai.co.in/api/v1/webhooks/{webhook_id}`
- **Test Webhook Endpoint:** `POST https://voice.voiceofai.co.in/api/v1/webhooks/{webhook_id}/test`

## Supported Events

- `call.started` — Triggered when call picks up
- `call.completed` — Triggered when call ends naturally
- `call.failed` — Triggered on error/network failure
- `campaign.started` — Triggered when campaign starts dialing
- `campaign.completed` — Triggered when all contacts processed
- `campaign.paused` — Triggered when campaign is paused
- `contact.created` — Triggered when new CRM contact added
- `contact.updated` — Triggered on contact detail update
- `credits.low` — Warning when balance drops below threshold
- `credits.depleted` — Alert when balance reaches 0

## Signature Verification

Webhooks deliver payloads with the header `X-Webhook-Signature` signed using your secret token via **HMAC-SHA256**.

## Helper Script

```bash
python3 setup-webhook/scripts/create_webhook.py \
  --url "https://your-domain.com/webhooks/voiceofai" \
  --events "call.completed,call.failed" \
  --description "Production Call Receiver"
```
