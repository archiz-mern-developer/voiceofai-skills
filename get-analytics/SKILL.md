---
name: get-analytics
description: "Pull aggregated call stats, campaign performance comparison metrics, or account-wide dashboard summaries. Use when evaluating call performance, answer rates, or campaign costs."
license: MIT
compatibility: Requires internet access and VOICEOFAI_API_KEY.
metadata:
  openclaw:
    requires:
      env:
        - VOICEOFAI_API_KEY
    primaryEnv: VOICEOFAI_API_KEY
---

# Get VoiceOfAI Analytics & Metrics

## Endpoints

- **Call Analytics:** `GET https://voice.voiceofai.co.in/api/v1/analytics/calls?days={days}`
- **Campaign Analytics:** `GET https://voice.voiceofai.co.in/api/v1/analytics/campaigns`
- **Dashboard Summary:** `GET https://voice.voiceofai.co.in/api/v1/analytics/summary?days={days}`

## Available Metrics

- Total calls & total minutes called
- Answer rate & completion rate (%)
- Average call duration (seconds)
- Call disposition & outcome distribution (answered, voicemail, busy, failed, no-answer)
- Daily trend comparisons against previous time window

## Helper Script

```bash
python3 get-analytics/scripts/fetch_analytics.py --type summary --days 30
```
