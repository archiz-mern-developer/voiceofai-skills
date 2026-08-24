---
name: manage-credits
description: "Check available calling credit balance and view daily credit usage history. Use when monitoring call minute quotas, checking billing status, or auditing daily usage."
license: MIT
compatibility: Requires internet access and VOICEOFAI_API_KEY.
metadata:
  openclaw:
    requires:
      env:
        - VOICEOFAI_API_KEY
    primaryEnv: VOICEOFAI_API_KEY
---

# Manage VoiceOfAI Account Credits

## Overview

VoiceOfAI uses a credit-based billing system where **1 credit equals 1 minute of call time**.

## Endpoints

- **Get Credit Balance:** `GET https://voice.voiceofai.co.in/api/v1/credits/balance`
- **Get Credit Usage History:** `GET https://voice.voiceofai.co.in/api/v1/credits/usage?days={days}`

## Response Examples

### Balance Response
```json
{
  "available": 450.5,
  "reserved": 15.0,
  "total": 465.5
}
```

### Usage Response
```json
{
  "history": [
    {"date": "2026-08-24", "creditsUsed": 32.5, "callCount": 14},
    {"date": "2026-08-23", "creditsUsed": 45.0, "callCount": 20}
  ]
}
```

## Helper Script

```bash
python3 manage-credits/scripts/check_balance.py --days 30
```
