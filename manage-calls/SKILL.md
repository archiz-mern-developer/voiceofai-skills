---
name: manage-calls
description: "List call history, get call details (transcripts, AI summaries, sentiment, recording URLs), or hangup an in-progress call. Use when inspecting call logs, analyzing call output, or terminating active calls."
license: MIT
compatibility: Requires internet access and VOICEOFAI_API_KEY.
metadata:
  openclaw:
    requires:
      env:
        - VOICEOFAI_API_KEY
    primaryEnv: VOICEOFAI_API_KEY
---

# Manage & Inspect VoiceOfAI Calls

## Endpoints

- **List Calls:** `GET https://voice.voiceofai.co.in/api/v1/calls?page={page}&pageSize={pageSize}`
- **Get Call Details:** `GET https://voice.voiceofai.co.in/api/v1/calls/{call_id}`
- **Hangup Active Call:** `POST https://voice.voiceofai.co.in/api/v1/calls/{call_id}/hangup`

## Call Status Lifecycle

1. `queued` — Waiting to be picked up by engine.
2. `ringing` — Target phone device is ringing.
3. `in-progress` — Call connected and conversation taking place.
4. `completed` / `failed` — Final state.

## Helper Script

```bash
python3 manage-calls/scripts/list_calls.py --page 1 --page-size 20
```

## Get Transcript & Recording

```bash
curl -H "Authorization: Bearer $VOICEOFAI_API_KEY" \
  https://voice.voiceofai.co.in/api/v1/calls/CALL_ID
```
Returns:
- `transcript`: Array of spoken turn objects `{speaker, message, timestamp}`
- `aiSummary`: Automated call summary
- `sentiment`: `"positive"`, `"neutral"`, `"negative"`
- `recordingUrl`: URL to MP3/WAV audio recording file
